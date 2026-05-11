import sqlite3

def get_db():
    conn = sqlite3.connect('database.db', check_same_thread=False, timeout=10)

    conn.row_factory = sqlite3.Row
    return conn