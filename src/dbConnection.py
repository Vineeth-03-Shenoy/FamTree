import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'VineethMYSQL@123',
        port='3307'
    )
    print("CONNECTION SUCCESFULL")
except mysql.connector.errors.ProgrammingError:
    print("CONNECTION ERROR, CANNOT CONNECT TO SERVER")

print(mydb)

db_cursor = mydb.cursor()

db_cursor.execute("CREATE DATABASE IF NOT EXISTS Dummy")

#db_cursor.execute("SHOW DATABASES")
#for db in db_cursor : 
#   print(db[0])

db_cursor.execute("USE DUMMY")

db_cursor.execute("CREATE TABLE IF NOT EXISTS Person (Name VARCHAR(25), Age INTEGER(3) NOT NULL)")
#db_cursor.execute("SHOW TABLES")
#for tbl in db_cursor:
#    print(tbl)

name=input("Enter Name")
age=int(input("Enter age:"))
table_value = "INSERT INTO Person (Name, Age) VALUES (%s, %s)"
record_value = (name, age)
db_cursor.execute(table_value, record_value)

mydb.commit()
