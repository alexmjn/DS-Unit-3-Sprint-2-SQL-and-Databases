import sqlite3


# Add a connection to the database
conn = sqlite3.connect('chinook.db')
curs = conn.cursor()

# 1. Find the average invoice total for each customer, return
# the details for the first 5 ID's
query = '''
    SELECT CustomerID, AVG(Total)
    FROM Invoices
    GROUP BY CustomerId
    LIMIT 5;
    '''
result = curs.execute(query).fetchall()
print('\nFind the average invoice total for each customer')
for row in result:
    print(row)

# 2. Return all columns in Customer for the first 5 customers
# residing in the United States
query = '''
    SELECT *
    FROM Customers
    WHERE Country = 'USA'
    LIMIT 5;
    '''
result = curs.execute(query).fetchall()
print('\nReturn all the columns in Customer for any customers \
residing in the United States')
for row in result:
    print(row)

# 3. Which employee does not report to anyone?
query = '''
    SELECT FirstName, LastName
    FROM Employees
    WHERE ReportsTo IS Null;
    '''
result = curs.execute(query).fetchone()
print('\nWhich employee does not report to anyone?', ' '.join(result))

# 4. Find the number of unique composers
query = '''
    SELECT COUNT(DISTINCT(Composer))
    FROM Tracks;
    '''
result = curs.execute(query).fetchone()
print('\nNumber of unique composers:', result[0])

# 5. How many rows are in the Track table?
query = '''
    SELECT COUNT(*)
    FROM Tracks;
    '''
result = curs.execute(query).fetchone()
print('\nNumber of rows in the Track table:', result[0])

# 6. Get the name of all Black Sabbath tracks and the albums they came off of
query = '''
    SELECT Tracks.Name AS 'Track Name', Albums.Title as 'Album Title'
    FROM Tracks
        JOIN Albums ON Tracks.AlbumId = Albums.AlbumId
        JOIN Artists ON Albums.ArtistId = Artists.ArtistId
    WHERE Artists.Name = 'Black Sabbath';
    '''
result = curs.execute(query).fetchall()
print('\nThe name of all Black Sabbath tracks and the albums they came off of')
for row in result:
    print(row)

# 7. What is the most popular genre by number of tracks?
query = '''
    SELECT Genres.Name
    FROM Tracks
        JOIN Genres ON Tracks.GenreId = Genres.GenreId
    GROUP BY Tracks.GenreId
    ORDER BY COUNT(Tracks.GenreId) DESC
    LIMIT 1;
    '''
result = curs.execute(query).fetchone()
print('\nMost popular genre:', result[0])

# 8. Find all customers that have spent over $40
query = '''
    SELECT Customers.FirstName, Customers.LastName
    FROM Customers
        JOIN Invoices ON Customers.CustomerId = Invoices.CustomerId
    GROUP BY Customers.CustomerId
    HAVING SUM(Invoices.Total) > 45;
    '''
result = curs.execute(query).fetchall()
print('\nAll customers that have spent over $40')
for row in result:
    print(' '.join(row))

# 9. Find the first and last name, title, and the number of customers
# each employee has helped. If the customer count is 0 for an employee,
# it doesn't need to be displayed. Order the employees
# from most to least customers.
query = '''
    SELECT e.FirstName, e.LastName, e.Title,
           COUNT(Customers.SupportRepID) as 'Customer Count'
    FROM Employees AS e
        JOIN Customers ON e.EmployeeId = Customers.SupportRepId
    GROUP BY e.EmployeeId
    ORDER BY 'Customer Count'
    '''
result = curs.execute(query).fetchall()
print('\nEmployees who have helped customers')
for row in result:
    print(row)

# 10. Return the first and last name of each employee and who they report to
query = '''
    SELECT e1.FirstName, e1.LastName, e2.FirstName, e2.LastName
    FROM Employees AS e1
        JOIN Employees as e2 ON e1.EmployeeId = e1.EmployeeId
    WHERE e1.ReportsTo = e2.EmployeeId;
    '''
result = curs.execute(query).fetchall()
print('\nEmployees and who they report to')
for row in result:
    print(' '.join(row[:2]), 'reports to', ' '.join(row[2:]))
