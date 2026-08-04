import sqlite3

# Connect to database (creates user_data.db if it doesn't exist)
conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()

# Create table matching the HTML form fields
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    gender TEXT,
    skills TEXT,          -- Stored as a comma-separated string (e.g., "Python, HTML")
    password TEXT NOT NULL,
    are_you_ok TEXT
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")