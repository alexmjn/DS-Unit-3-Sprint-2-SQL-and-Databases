import os
import sqlite3

#database_file = "rpg_db.sqlite3"
#DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", database_file)
#print(DB_FILEPATH)

#connection = sqlite3.connect(DB_FILEPATH)
connection = sqlite3.connect("rpg_db.sqlite3")
connection.row_factory = sqlite3.Row
#print("CONNECTION:", connection)

cursor = connection.cursor()

#How many total characters?
query = "SELECT count(distinct character_id) FROM charactercreator_character"
result = cursor.execute(query).fetchall()
print(f"There are {result[0][0]} characters")

#How many of each type of character?
for database in ["mage", "thief", "cleric", "fighter"]:
    database_name = "charactercreator_" + database
    query = f"""
    SELECT
        count(distinct character_ptr_id) as character_count
    FROM {database_name}
    """
    result = cursor.execute(query).fetchall()
    print(database, result[0][0])
