import sqlite3
import pandas as pd

def get_chat_history():

    conn = sqlite3.connect(
        "chat_history.db"
    )

    df = pd.read_sql_query(
        "SELECT * FROM chats ORDER BY id DESC",
        conn
    )

    conn.close()

    return df