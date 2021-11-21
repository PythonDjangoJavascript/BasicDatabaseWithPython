import MySQLdb
from datetime import datetime
from datetime import date


db = MySQLdb.connect(
    host="localhost",
    user="root",
    password="BrownFox1234",
    database="testdatabase"
)

cursor = db.cursor()

# execute query Only for the first time to create database
# cursor.execute("CREATE DATABASE testdatabase")

# now create table person
# cursor.execute(
#     "CREATE TABLE person (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age SMALLINT UNSIGNED)")

# cursor.execute("DESCRIBE person")

# for x in cursor:
#     print(x)

# insert data to the newly created table
# cursor.execute("INSERT INTO person (name, age) VALUES (%s, %s)", ("Sayed", 25))
# db.commit()  # commit these changes

# get all data
# cursor.execute("SELECT * FROM person")
# for x in cursor:
#     print(x)

# create new table
# cursor.execute("CREATE TABLE Test (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL)")

# insert data to Test
# cursor.execute(
#     "INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ('Syeed', datetime.now(), 'M'))
# cursor.execute(
#     "INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ('Nuruddin', datetime.now(), 'M'))
# cursor.execute(
#     "INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ('Juba', datetime.now(), 'M'))
# cursor.execute(
#     "INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ('Summayea', datetime.now(), 'F'))
# db.commit()

# Retreave specific data from Test
# cursor.execute(
#     "SELECT ID, NAME FROM Test WHERE gender = 'M' ORDER BY ID DESC;")
# for x in cursor:
#     print(x)


# Alter Table add column
# cursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL;")

# cursor.execute("SELECT * FROM Test")
# check table column
# cursor.execute("DESCRIBE Test;")
# # print(cursor.fetchone())
# for x in cursor:
#     print(x)

# Change column name
# cursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50);")


# Create table with datetime.date
# cursor.execute("CREATE TABLE TestOne (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL)")
# cursor.execute(
#     "INSERT INTO TestOne (name, created, gender) VALUES (%s, %s, %s)", ('GHI', date.today(), 'F'))
# cursor.execute(
#     "INSERT INTO TestOne (name, created, gender) VALUES (%s, %s, %s)", ('ABC', date.today(), 'F'))
# cursor.execute(
#     "INSERT INTO TestOne (name, created, gender) VALUES (%s, %s, %s)", ('DEF', date.today(), 'F'))
# db.commit()
# cursor.execute("SELECT * FROM TestOne")
# # check table column
# cursor.execute("DESCRIBE Test;")
# # print(cursor.fetchone())
# for x in cursor:
#     print(x)

# # Get table column name
# des_list = [x[0] for x in cursor.description]
# print(des_list)


# OneToOne Relation
users = [
    ("Sayed", "supersecretpassword", "sayed@email.com"),
    ("Nuruddin", "nuruddinpassword", "Nuruddin@email.com"),
    ("Rafi", "supersecretrafi", "rafid@email.com")
]
user_scores = [
    (223, 245),
    (250, 190),
    (220, 200)
]

# Creating table
# test_user_crate_talbe = "CREATE TABLE TestUser (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(60), email VARCHAR(50));"
# test_score_create_table = "CREATE TABLE TestUserScores(userID INT PRIMARY KEY, FOREIGN KEY(userID) REFERENCES TestUser(id), game1 INT DEFAULT 0, game2 INT DEFAULT 0);"

# cursor.execute(test_user_crate_talbe)
# cursor.execute(test_score_create_table)

# user_insert_query = "INSERT INTO TestUser(name, password, email) VALUES (%s, %s, %s)"
# user_scores_insert_query = "INSERT INTO TestUserScores (userID, game1, game2) VALUES (%s, %s, %s)"

# for i, user in enumerate(users):
#     print(f"i {i} user {user}")
#     cursor.execute(user_insert_query, user)
#     last_id = cursor.lastrowid
#     # bellow line will create add last id and user score and create a touple
#     cursor.execute(user_scores_insert_query, (last_id, ) + user_scores[i])
# db.commit()


# check all data
# cursor.execute("SELECT * FROM TestUser")
# for x in cursor:
#     print(x)
# cursor.execute("SELECT * FROM TestUserScores")
# for x in cursor:
#     print(x)
