import sqlite3

conn = sqlite3.connect("test_data.sqlite")
curs = conn.cursor()

create_study_table = """
    CREATE TABLE Students (
        student VARCHAR(20),
        studied VARCHAR(5),
        grade INT,
        age INT,
        sex VARCHAR(6)
    ) """

curs.execute(create_study_table)

fill_in_table = """
    INSERT INTO Students VALUES
        ()"""

curs.execute(fill_in_table)

conn.commit()

query = "SELECT AVG(age) FROM Students;"
result = curs.execute(query).fetchone()
# copy-paste in the question - make things easier on michael
print("The average age is:", result[0])
