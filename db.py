import sqlite3
from pathlib import Path

DB_PATH = Path("movies.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn, open("schema.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())

def seed_db():
    with get_conn() as conn, open("seed.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())
