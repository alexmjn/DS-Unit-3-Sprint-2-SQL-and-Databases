import sqlite3

# Part 1: Create a new database file call study_part1.sqlite3
conn = sqlite3.connect('study_part1.sqlite3')
curs = conn.cursor()

# Part 2: Create a table with the following columns
create_study_table = '''
    CREATE TABLE Students (
        student VARCHAR(20),
        studied VARCHAR(5),
        grade INT,
        age INT,
        sex VARCHAR(6))'''
curs.execute(create_study_table)

# Part 3: Fill the table with the following data
study_insert = '''
    INSERT INTO Students VALUES
        ('Lion-O', 'True', 85, 24, 'Male'),
        ('Cheetara', 'True', 95, 22, 'Female'),
        ('Mumm-Ra', 'False', 65, 153, 'Male'),
        ('Snarf', 'False', 70, 15, 'Male'),
        ('Panthro', 'True', 80, 30, 'Male')'''
curs.execute(study_insert)
conn.commit()

# Part 4: Check in DB Browswer

# Part 5: Write the following queries to check your work
# What is the average age? Expected Result - 48.8
query = 'SELECT AVG(age) FROM Students;'
result = curs.execute(query).fetchone()
print('\nWhat is the average age?', result[0])

# What are the name of the female students? Expected Result - 'Cheetara'
query = "SELECT student FROM Students WHERE sex = 'Female';"
result = curs.execute(query).fetchall()
print('\nWhat are the name of the female students?', result[0][0])

# How many students studied? Expected Results - 3
query = 'SELECT COUNT(studied) FROM Students WHERE studied = "True";'
result = curs.execute(query).fetchone()
print('\nHow many students studied?', result[0])

# Return all students and all columns, sorted by student names
# in alphabetical order.
query = 'SELECT * FROM Students ORDER BY student;'
result = curs.execute(query).fetchall()
print('\nReturn all students and all columns, sorted by student names \
in alphabetical order.')
for row in result:
    print(row)
