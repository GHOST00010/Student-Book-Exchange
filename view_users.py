# view_users.py
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("📋 Registered Users:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Address: {row[3]}, Time: {row[5]}")

conn.close()
