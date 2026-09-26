import sqlite3

connection = sqlite3.connect("pocketsmart.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_type TEXT,
    budget REAL,
    details TEXT
)
""")

connection.commit()
connection.close()

print("Database created successfully!")