import sqlite3

connection = sqlite3.connect("buddymove_holidayiq.sqlite3")
print(connection.execute("SELECT * FROM review LIMIT 10").fetchall())
