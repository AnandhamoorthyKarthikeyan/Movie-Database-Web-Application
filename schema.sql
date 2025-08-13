PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Movie_Actors;
DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Actors;

CREATE TABLE Movies (
  movie_id     INTEGER PRIMARY KEY AUTOINCREMENT,
  title        TEXT NOT NULL,
  release_year INTEGER NOT NULL,
  genre        TEXT NOT NULL,
  rating       REAL NOT NULL CHECK (rating >= 0 AND rating <= 10)
);

CREATE TABLE Actors (
  actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name     TEXT NOT NULL
);

CREATE TABLE Movie_Actors (
  movie_id INTEGER NOT NULL,
  actor_id INTEGER NOT NULL,
  PRIMARY KEY (movie_id, actor_id),
  FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE,
  FOREIGN KEY (actor_id) REFERENCES Actors(actor_id) ON DELETE CASCADE
);

-- Helpful indexes for filtering
CREATE INDEX idx_movies_title ON Movies(title);
CREATE INDEX idx_movies_year ON Movies(release_year);
CREATE INDEX idx_movies_rating ON Movies(rating);
CREATE INDEX idx_movies_genre ON Movies(genre);
CREATE INDEX idx_actors_name ON Actors(name);
