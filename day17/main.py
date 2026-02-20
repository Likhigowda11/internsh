import sqlite3


def create_connection():
    return sqlite3.connect("internship.db")


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interns (
        id INTEGER PRIMARY KEY,
        name TEXT,
        track TEXT,
        stipend INTEGER
    )
    """)
    conn.commit()
    print("Table checked/created successfully.")


def insert_data(conn):
    cursor = conn.cursor()
    intern_data = [
        (1, "Aisha", "Data Science", 15000),
        (2, "Rahul", "Web Dev", 12000),
        (3, "Meena", "Data Science", 18000),
        (4, "Arjun", "Cyber Security", 16000),
        (5, "Priya", "Web Dev", 14000)
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO interns VALUES (?, ?, ?, ?)",
        intern_data
    )
    conn.commit()
    print("Sample data inserted.")


def query_interns(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name, track FROM interns")
    rows = cursor.fetchall()

    print("\nIntern Name and Track:")
    for row in rows:
        print(row)


def main():
    conn = create_connection()
    create_table(conn)
    insert_data(conn)
    query_interns(conn)
    conn.close()


if __name__ == "__main__":
    main()
