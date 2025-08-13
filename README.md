# Movie Database Web Application

## Aim
The aim of this project is to develop a full-stack Movie Database web application where users can search, filter, and view details of movies and their actors. The project demonstrates the integration of Python Flask backend with HTML, CSS, and JavaScript frontend, and an SQLite database for data management.

---

## Features
-  Search movies by partial title  
-  Filter movies released after a certain year  
-  Find movies with rating above a specific value  
-  Sort results by title, year, or rating (ascending/descending)  
-  View detailed movie information, including genre and actors  
-  REST API endpoints for integration with other services  

---

## Tech Stack
**Frontend:** HTML5, CSS3, JavaScript  
**Backend:** Python (Flask)  
**Database:** SQLite  
**Deployment:** Render (Gunicorn + Flask)  

---

## Procedure**
1. **Design Database Schema**  
   - Tables: `Movies`, `Actors`, `Movie_Actors`
   - Fields:  
     - `Movies` → `movie_id`, `title`, `release_year`, `genre`, `rating`  
     - `Actors` → `actor_id`, `name`  
     - `Movie_Actors` → `movie_id`, `actor_id`

2. **Create Backend API with Flask**  
   - Routes for homepage, movie search, movie details, and API endpoints.

3. **Build Frontend Pages**  
   - `base.html` → Common layout and design  
   - `index.html` → Search interface and movie list  
   - `movie_detail.html` → Movie info and cast list

4. **Integrate Database Queries**  
   - Use SQL queries for filtering, searching, and ordering results.

5. **Test Locally**  
   - Run `python app.py` to launch the development server.  
   - Access at `http://127.0.0.1:5000`.

6. **Deploy Online**  
   - Push code to GitHub.  
---

## **Setup Instructions**
### Clone Repository
git clone https://github.com/yourusername/movie-database.git
cd movie-database
### Create Virtual Environment & Install Requirements
python -m venv .venv
. .venv/Scripts/Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
###  Run the Application
python app.py
Visit: http://127.0.0.1:5000
### API Examples
Search movies by title:

GET /api/movies?title=star
Movies released after 2010:

GET /api/movies?year=2010
Movies with rating above 8.0:

GET /api/movies?min_rating=8.0
## OUTPUT
<img width="1890" height="921" alt="Screenshot 2025-08-13 171718" src="https://github.com/user-attachments/assets/bd6d1ee1-c83b-457b-bfd1-519b04dd945d" />

