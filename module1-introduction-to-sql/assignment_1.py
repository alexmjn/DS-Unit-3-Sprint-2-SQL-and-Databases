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

query = "SELECT count(distinct item_id) FROM armory_item"
result = cursor.execute(query).fetchall()
n_items = result[0][0]
print(f"There are {n_items} items")

query = "SELECT count(distinct item_ptr_id) FROM armory_weapon"
result = cursor.execute(query).fetchall()
n_weapons = result[0][0]
print(f"The percentage of weapons is {n_weapons/n_items:.2f}")

#need to join to get character names
query = """
SELECT
    character_id,
    count(distinct id) as total_items
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""
result = cursor.execute(query).fetchall()
for row in result:
    print(row[0], row[1])

query = """
SELECT
    charactercreator_character_inventory.character_id,
    count(distinct charactercreator_character_inventory.id)
FROM charactercreator_character_inventory
JOIN armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
LIMIT 20
"""
result = cursor.execute(query).fetchall()
for row in result:
    print(row[0], row[1])
