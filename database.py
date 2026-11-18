import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "chat_history.db"

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id TEXT NOT NULL,
                user_message TEXT NOT NULL,
                bot_response TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def save_message(chat_id, user_message, bot_response):
    with get_connection() as connection:
        connection.execute(
            """INSERT INTO conversations
               (chat_id, user_message, bot_response)
               VALUES (?, ?, ?)""",
            (chat_id, user_message, bot_response)
        )

def get_history(chat_id):
    with get_connection() as connection:
        rows = connection.execute(
            """SELECT user_message, bot_response, created_at
               FROM conversations WHERE chat_id = ?
               ORDER BY id ASC LIMIT 100""",
            (chat_id,)
        ).fetchall()
    return [dict(row) for row in rows]

def clear_history(chat_id):
    with get_connection() as connection:
        connection.execute(
            "DELETE FROM conversations WHERE chat_id = ?", (chat_id,)
        )
