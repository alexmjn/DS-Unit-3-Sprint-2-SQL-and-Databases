import sqlite3

conn = sqlite3.connect("chinook.db")
conn.row_factory = sqlite3.Row
curs = conn.cursor()

query = """
SELECT CustomerId, ROUND(avg(Total), 3) AS Average
FROM Invoices
GROUP BY CustomerId
Limit 5"""

result = curs.execute(query).fetchall()
for row in result:
    print(dict(row))

query = """
    SELECT *
    FROM Customers
    WHERE Country = "USA"
    LIMIT 5"""

result = curs.execute(query).fetchall()
for row in result:
   print(dict(row))

import pandas as pd
df = pd.read_sql_query(query, conn)
print(df.head().T)

query = """
SELECT EmployeeId, FirstName, LastName
FROM employees
WHERE ReportsTo IS NULL
"""
df = pd.read_sql_query(query, conn)
print(df.head())

query = """
    SELECT t.name, a.title
    FROM Tracks t
        JOIN Albums a ON t.albumid = a.albumid
        JOIN Artists art ON art.ArtistId = a.ArtistId
    WHERE art.Name = "Black Sabbath"
"""
df = pd.read_sql_query(query, conn)
print(df.head())
result = curs.execute(query).fetchall()
for row in result:
    print(dict(row))
