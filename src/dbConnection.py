import mysql.connector

def connection():
    try:
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'VineethMYSQL@123',
            port='3307'
        )
        print("CONNECTION SUCCESSFULL")
        return mydb
    except mysql.connector.errors.ProgrammingError:
        print("CONNECTION ERROR, CANNOT CONNECT TO SERVER")


def DBcreate():
    mydb=connection()
    db_cursor = mydb.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS dummy")
    db_cursor.execute("USE dummy")
    mydb.commit()
