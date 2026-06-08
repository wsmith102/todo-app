import sqlite3
from pathlib import Path

DB_PATH = Path("ai_data.db")

class SQLiteDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS training_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                f1 REAL, f2 REAL, f3 REAL, f4 REAL,
                label INTEGER
            )
        """)
        self.conn.commit()

    def insert_sample(self, features, label):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO training_data (f1, f2, f3, f4, label) VALUES (?, ?, ?, ?, ?)",
            (*features, label)
        )
        self.conn.commit()

    def load_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT f1, f2, f3, f4, label FROM training_data")
        rows = cur.fetchall()

        if not rows:
            return [], []

        X = [row[:4] for row in rows]
        y = [row[4] for row in rows]
        return X, y
