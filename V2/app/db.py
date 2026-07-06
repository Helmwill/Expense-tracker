import os
import sqlite3
from datetime import date
from pathlib import Path

DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "tracker.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    tier TEXT NOT NULL,
    target_amount REAL NOT NULL,
    icon_path TEXT,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS contributions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    goal_id INTEGER NOT NULL REFERENCES goals(id) ON DELETE CASCADE,
    amount REAL NOT NULL,
    note TEXT,
    date TEXT NOT NULL
);
"""

SEED_GOALS = [
    ("Clear overdraft", "essential", 500.0, "icons/overdraft.svg"),
    ("Emergency buffer", "important", 1000.0, "icons/emergency-buffer.svg"),
    ("Holiday", "bonus", 800.0, "icons/holiday.svg"),
]


def get_db_path() -> Path:
    return Path(os.environ.get("DATABASE_PATH", str(DEFAULT_DB_PATH)))


def connect() -> sqlite3.Connection:
    path = get_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    conn = connect()
    try:
        conn.executescript(SCHEMA)
        empty = conn.execute("SELECT COUNT(*) FROM goals").fetchone()[0] == 0
        if empty:
            today = date.today().isoformat()
            conn.executemany(
                "INSERT INTO goals (name, tier, target_amount, icon_path, created_at) "
                "VALUES (?, ?, ?, ?, ?)",
                [(n, t, amt, icon, today) for n, t, amt, icon in SEED_GOALS],
            )
        conn.commit()
    finally:
        conn.close()
