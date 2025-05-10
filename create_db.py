import sqlite3

def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Create the students table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            Course TEXT,
            Mobile TEXT
        )
    """)

    # You can add some sample data here if you want
    # cursor.execute("INSERT INTO students (Id, Name, Course, Mobile) VALUES (?, ?, ?, ?)", (1, "Alice", "Math", "123-456-7890"))
    # cursor.execute("INSERT INTO students (Id, Name, Course, Mobile) VALUES (?, ?, ?, ?)", (2, "Bob", "Science", "987-654-3210"))

    conn.commit()
    conn.close()
    print("Database 'database.db' and table 'students' created successfully.")

if __name__ == "__main__":
    create_database()