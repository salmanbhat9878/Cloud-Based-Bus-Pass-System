import sqlite3

def get_connection():
    return sqlite3.connect("bus_pass.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll_number TEXT,
            email TEXT,
            phone TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bus_passes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            route TEXT,
            pass_type TEXT,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()