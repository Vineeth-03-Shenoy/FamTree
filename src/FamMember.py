import dbConnection
import mysql.connector

try:
    mydb = dbConnection.connection()
    dbConnection.DBcreate()
except mysql.connector.errors.ProgrammingError:
    print("CONNECTION ERROR")

mycursor = mydb.cursor()

def fam_MemberTable():
    mycursor.execute("USE FamTree")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Family_Member(ID VARCHAR(18) NOT NULL, First_Name VARCHAR(20) NOT NULL, Name VARCHAR(20) NOT NULL, Last_Name VARCHAR(20) NOT NULL, DoB DATE NOT NULL, DoD DATE)")

def ID_Creator(Fname,name,Lname,Dob):
    firname = Fname[0]+Fname[(len(Fname)//2)-1]+Fname[len(Fname)-1]
    midname = name[0]+name[(len(name)//2)-1]+name[len(name)-1]
    lastname = Lname[0]+Lname[(len(Lname)//2)-1]+Lname[len(Lname)-1]
    ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
    if ID_Collison_Detection(ID):
        midname = name[0]+name[(len(name)//2)-2]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        if ID_Collison_Detection(ID):
            midname = name[0]+name[(len(name)//2)]+name[len(name)-1]
            ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
            if ID_Collison_Detection(ID):
                midname = name[0]+name[(len(name)//2)+1]+name[len(name)-1]
                ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
    return ID

def ID_Collison_Detection(ID):
    mycursor.execute("USE FamTree")
    sql_cmd = "SELECT ID FROM family_member WHERE ID=%s"
    value = (ID,)
    mycursor.execute(sql_cmd,value)
    myresult = mycursor.fetchall()
    if ID in myresult:
        return True

def FM_Insert():
    fam_MemberTable()
    try:
        Fname = input("Enter the first name: ")
        name = input("Enter the Middle Name: ")
        Lname = input("Enter the Last Name: ")
        DoB = input("Enter the Date of Birth (YYYY-MM-DD): ")
        ID = ID_Creator(Fname.capitalize(),name.capitalize(),Lname.capitalize(),DoB)
        sqlcmd = 'INSERT INTO family_member(ID,First_Name,Name,Last_Name,Dob,Dod) VALUES (%s,%s,%s,%s,%s,NULL)'
        values = (ID,Fname,name,Lname,DoB)
        mycursor.execute(sqlcmd,values)
    except Exception:
        print("COULD NOT INSERT")
    else:
        print("Successfully Inserted Value")
    mydb.commit()