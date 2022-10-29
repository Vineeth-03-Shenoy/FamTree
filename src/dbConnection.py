import mysql.connector

def connection():
    try:
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'VineethMYSQL@123',
            port='3307'
        )
        print("CONNECTION SUCCESFULL")
        return mydb
    except mysql.connector.errors.ProgrammingError:
        print("CONNECTION ERROR, CANNOT CONNECT TO SERVER")


def DBcreate():
    db_cursor = mydb.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS FamTree")
    db_cursor.execute("USE FamTree")
    mydb.commit()
