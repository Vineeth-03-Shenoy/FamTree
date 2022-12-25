import dbConnection
import mysql.connector

try:
    mydb = dbConnection.connection()
    dbConnection.DBcreate()
except mysql.connector.errors.ProgrammingError:
    print("CONNECTION ERROR")

mycursor = mydb.cursor()

def fam_MemberTable():
    mycursor.execute("USE dummy")
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

def ID_Collison_Detection(ID):
    mycursor.execute("SELECT ID FROM family_member")
    myresult = mycursor.fetchall()
    if ID in myresult:
        return True

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

'''def Famtree(target1, maintarget):
    mycursor.execute('USE dummy')
    mycursor.execute('SELECT * FROM parents')
    L=mycursor.fetchall()
    findsource = False
    findtarget = False
    findtree = False
    T=[]
    print(L,"\n")

    while findtree==False:
        #while findsource==False:
        source1,T,L,findsource = findSourceMethod(target1,L,T)
        print(source1,"\n",T,"\n",L)
        #while findtarget==False:
        T,target1,target2=findTargetMethod(source1,T,L)
        if maintarget in T:
            findtree=True
        source2,T,L,findsource=findSourceMethod(target2,L,T)
        print(source2,"\n",T,"\n",L)    
                
            #findtarget=True

        #findtree=True
    return T

def findSourceMethod(source,L,T):
    for i in L:
        for j in i:
            if j==source:
                if j not in T:
                    T.append(j)
                    L.remove(i)
                    return j,T,L,True
                else: return j,T,L,True

def findTargetMethod(source,T,L):
    sql_cmd = "SELECT * FROM parents WHERE ID=%s OR Father_ID=%s OR Mother_ID=%s " 
    values = (source,source,source)
    mycursor.execute(sql_cmd,values)
    U=mycursor.fetchall()
    m=[]
    for i in L:
        for j in i:
            if j==source:
                m=list(i)
                m.remove(source)
                T.extend(m)
    target1=m[0]
    target2=m[1]
    return T,target1,target2
            
def FamList(source, Target):
    mycursor.execute('USE dummy')
    Famtree = []
    Famtree.append(extractParents(source))
    Famtree.append(extractParents(Target))
    return Famtree


def extractParents(Son):
    dict={"Child":Son,}
    mycursor.execute("SELECT Father_ID FROM parents WHERE ID=%s",(Son,))
    T = mycursor.fetchone()
    F=''.join(T)
    mycursor.execute("SELECT Mother_ID FROM parents WHERE ID=%s",(Son,))
    T = mycursor.fetchone()
    M=''.join(T)
    dict["Parents"]=F+" & "+M
    return dict'''

'''class family_member:
    def __init__(self,ID,name):
        self.ID=ID
        self.name=name'''

def tupleToString(Tup):
    st=''
    for item in Tup:
        st = st + item
    return st

def parentsFinder(source):
    mycursor.execute('USE dummy')
    mycursor.execute("SELECT Father_ID from parents WHERE ID=%s",(source,))
    targetID=mycursor.fetchone()
    targetID1=tupleToString(targetID)
    if len(targetID)!=0:
        targetID1=tupleToString(targetID)
        return 'Child',True
    else:
        mycursor.execute("SELECT Mother_ID from parents WHERE ID=%s",(source,))
        targetID=mycursor.fetchone()
        targetID2=tupleToString(targetID)
        if target==targetID2:
            return 'Mother',True
    return targetID1+targetID2,False


def childFinder(source,target):
    mycursor.execute('USE dummy')
    mycursor.execute("SELECT ID from parents WHERE Father_ID=%s OR Mother_ID=%s",(source,source,))
    targetID=mycursor.fetchone()
    if len(targetID)!=0:
        targetID1=tupleToString(targetID)
        if target==targetID1:
            return 'Child',True
    return targetID1,False


def relationFinder(source,target):
    mycursor.execute('USE dummy')
    foundTarget=False
    relationship=''
    while foundTarget==False:
        relationship,sourceParents=parentsFinder(source)
        if foundTarget==True:
            print(source+'<---'+relationship+'---'+target) 
            break
        relationship,foundTarget=childFinder(source,target)
        if foundTarget==True:
            print(source+'<---'+relationship+'---'+target) 
            break

        
