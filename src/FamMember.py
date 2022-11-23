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
    mycursor.execute("CREATE TABLE IF NOT EXISTS Family_Member(ID VARCHAR(18) PRIMARY KEY, First_Name VARCHAR(20) NOT NULL, Name VARCHAR(20) NOT NULL, Last_Name VARCHAR(20) NOT NULL, DoB DATE NOT NULL, DoD DATE)")

def ID_Creator(Fname,name,Lname,Dob,coll_val):
    firname = Fname[0]+Fname[(len(Fname)//2)-1]+Fname[len(Fname)-1]
    lastname = Lname[0]+Lname[(len(Lname)//2)-1]+Lname[len(Lname)-1]
    if coll_val==0:                                                                     #for the first time
        midname = name[0]+name[(len(name)//2)-1]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID
    elif coll_val==1:
        midname = name[0]+name[(len(name)//2)-2]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID
    elif coll_val==2:
        midname = name[0]+name[(len(name)//2)]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID 
    elif coll_val==3:
        midname = name[0]+name[(len(name)//2)+1]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID
    elif coll_val==4:
        midname = name[0]+name[(len(name)//2)+2]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID
    else: 
        return Exception

'''def ID_Collison_Detection(ID):
    mycursor.execute("SELECT ID FROM family_member")
    myresult = mycursor.fetchall()
    if ID in myresult:
        return True'''

def FM_Insert():
    fam_MemberTable()    
    Fname = input("Enter the first name: ")
    name = input("Enter the Middle Name: ")
    Lname = input("Enter the Last Name: ")
    DoB = input("Enter the Date of Birth (YYYY-MM-DD): ")
    coll_val = 0                                                            #tracks no of times the collision occured
    while True:
        try:
            ID = ID_Creator(Fname.capitalize(),name.capitalize(),Lname.capitalize(),DoB,coll_val)
            sqlcmd = 'INSERT INTO family_member(ID,First_Name,Name,Last_Name,Dob,Dod) VALUES (%s,%s,%s,%s,%s,NULL)'
            values = (ID,Fname,name,Lname,DoB,)
            mycursor.execute(sqlcmd,values)
        except mysql.connector.errors.IntegrityError:
            coll_val+=1
        except Exception:
            print("COULD NOT INSERT")
            break
        else:
            print("Successfully Inserted Value")
            break
    mydb.commit()