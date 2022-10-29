import dbConnection
import mysql.connector

try:
    mydb = dbConnection.connection()
    dbConnection.DBcreate()
except mysql.connector.errors.ProgrammingError:
    print("CONNECTION ERROR")

mycursor = mydb.cursor()

def fam_MemberTable():
    mycursor.execute("CREATE TABLE IF NOT EXISTS Family_Member(ID VARCHAR(18) NOT NULL, First_Name VARCHAR(20) NOT NULL, Name VARCHAR(20) NOT NULL, Last_Name VARCHAR(20) NOT NULL, DoB INT(8) NOT NULL, DoD INT(8)")

def FM_Insert()