import sqlite3

def create_db():
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            mode TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_chat(question, answer, mode):
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats(question, answer, mode) VALUES (?, ?, ?)",
        (question, answer, mode)
    )

    conn.commit()
    conn.close()