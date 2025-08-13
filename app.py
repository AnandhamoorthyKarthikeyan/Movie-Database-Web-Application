from flask import Flask, request, jsonify, render_template, abort, redirect, url_for
from db import get_conn, init_db, seed_db, DB_PATH
from pathlib import Path

app = Flask(__name__)

# Initialize DB automatically on first run
if not Path(DB_PATH).exists():
    init_db()
    seed_db()

@app.get("/")
def home():
    # A simple search page (JS will call /api/movies)
    return render_template("index.html")

@app.get("/movie/<int:movie_id>")
def movie_detail(movie_id: int):
    with get_conn() as conn:
        movie = conn.execute(
            "SELECT * FROM Movies WHERE movie_id = ?",
            (movie_id,)
        ).fetchone()
        if not movie:
            abort(404)

        actors = conn.execute("""
            SELECT a.actor_id, a.name
            FROM Actors a
            JOIN Movie_Actors ma ON ma.actor_id = a.actor_id
            WHERE ma.movie_id = ?
            ORDER BY a.name ASC
        """, (movie_id,)).fetchall()

    return render_template("movie_detail.html", movie=movie, actors=actors)

# -------- API (JSON) -------- #

@app.get("/api/movies")
def api_movies():
    """
    Filters:
      - title (partial, LIKE)
      - min_year (release_year > ?)
      - min_rating (rating >= ?)
      - genre (exact match)
      - order (one of: title_asc/title_desc/year_asc/year_desc/rating_asc/rating_desc)
      - page, page_size (pagination)
    """
    title = request.args.get("title", "").strip()
    genre = request.args.get("genre", "").strip()
    min_year = request.args.get("min_year", type=int)
    min_rating = request.args.get("min_rating", type=float)
    order = request.args.get("order", "year_desc").strip().lower()
    page = max(request.args.get("page", default=1, type=int), 1)
    page_size = min(max(request.args.get("page_size", default=10, type=int), 1), 100)

    # Whitelist ordering to prevent SQL injection
    order_map = {
        "title_asc": "title ASC",
        "title_desc": "title DESC",
        "year_asc": "release_year ASC",
        "year_desc": "release_year DESC",
        "rating_asc": "rating ASC",
        "rating_desc": "rating DESC",
    }
    order_clause = order_map.get(order, "release_year DESC")

    where = []
    params = []

    if title:
        where.append("title LIKE ?")
        params.append(f"%{title}%")

    if genre:
        where.append("genre = ?")
        params.append(genre)

    if min_year is not None:
        where.append("release_year > ?")
        params.append(min_year)

    if min_rating is not None:
        where.append("rating >= ?")
        params.append(min_rating)

    where_clause = f"WHERE {' AND '.join(where)}" if where else ""
    limit = page_size
    offset = (page - 1) * page_size

    base_sql = f"""
        SELECT movie_id, title, release_year, genre, rating
        FROM Movies
        {where_clause}
        ORDER BY {order_clause}
        LIMIT ? OFFSET ?;
    """

    count_sql = f"SELECT COUNT(*) as total FROM Movies {where_clause};"

    with get_conn() as conn:
        total = conn.execute(count_sql, tuple(params)).fetchone()["total"]
        rows = conn.execute(base_sql, tuple(params) + (limit, offset)).fetchall()

    return jsonify({
        "page": page,
        "page_size": page_size,
        "total": total,
        "items": [dict(r) for r in rows],
    })

@app.get("/api/movie/<int:movie_id>")
def api_movie(movie_id: int):
    with get_conn() as conn:
        movie = conn.execute(
            "SELECT * FROM Movies WHERE movie_id = ?", (movie_id,)
        ).fetchone()
        if not movie:
            return jsonify({"error": "Not found"}), 404

        actors = conn.execute("""
            SELECT a.actor_id, a.name
            FROM Actors a
            JOIN Movie_Actors ma ON ma.actor_id = a.actor_id
            WHERE ma.movie_id = ?
            ORDER BY a.name ASC
        """, (movie_id,)).fetchall()

    return jsonify({
        "movie": dict(movie),
        "actors": [dict(a) for a in actors]
    })

# Optional SSR list page (not required since index uses JS)
@app.get("/movies")
def movies_page():
    # Simple server-side render pass-through of filters, reuses /api for data
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
