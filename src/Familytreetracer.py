import dbConnection
import mysql.connector

try:
    mydb = dbConnection.connection()
    dbConnection.DBcreate()
except mysql.connector.errors.ProgrammingError:
    print("CONNECTION ERROR")

mycursor = mydb.cursor()