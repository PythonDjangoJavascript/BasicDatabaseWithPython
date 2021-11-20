import MySQLdb
from datetime import datetime


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

# check table column
# cursor.execute("DESCRIBE Test;")
# # print(cursor.fetchone())
# for x in cursor:
#     print(x)

# Change column name
# cursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50);")
