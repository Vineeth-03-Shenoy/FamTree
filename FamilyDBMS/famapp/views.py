import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Family_Member

# Create your views here.
def home(request):
    return render(request, "home.html")

def FamHome(request):
    return render(request, "familyHOME.html")

def DataBase(request):
    return render(request, "database.html")

def NewMember(request):
    if request.method=='POST':
        Fname = request.POST['Fname']
        Name = request.POST['Name']
        Lname = request.POST['Lname']
        DoB = request.POST['DoB']
        Gender = request.POST['Gender']

        collval=0
        while collval!=5:
            ID = ID_Creator(Fname.upper(),Name.upper(),Lname.upper(),DoB,collval)
            try:
                obj=Family_Member.objects.get(FamMemberID=ID)
                collval+=1
            except Family_Member.DoesNotExist:
                FamMemberID=ID
                break

        if collval==5:
            print("ID could not be genrated, please contact admin",Fname,Name,Lname,DoB,Gender)

        ins = Family_Member(FamMemberID=FamMemberID, Fname=Fname,Name=Name,Lname=Lname,DoB=DoB,Gender=Gender)
        ins.save()
        return render(request, "insert successfull.html", { 'FamMemberID': FamMemberID })
    return render(request, "insertdb.html")

def DeleteMember(request):
    if request.method=='POST':
        FamMemberID=request.POST['FamMemberID']
        try:
            ins=Family_Member.objects.get(FamMemberID=FamMemberID)
            print(ins)
            ins.delete()
            return render(request, "delete successfull.html", { 'FamMemberID': FamMemberID+' Deleted' })
        except Family_Member.DoesNotExist:
            return render(request, "delete successfull.html", { 'FamMemberID': FamMemberID+' Does Not Exist.!! If you think it exists, Check ID and enter again (make sure the ID is in Uppercase while entering.).' })
        
    return render(request, "deletemember.html") 

def ViewPage(request):
    return render(request, "mainviewpage.html")

def ViewSearchPage(request):
    if request.method=='POST':
        FamMemberID=request.POST['FamMemberID']
        try:
            FamMember=Family_Member.objects.get(FamMemberID=FamMemberID)
            return render(request, "searchOutput.html", { 'FamMember' : FamMember })
        except Family_Member.DoesNotExist:
            return render(request, "searchOutput.html", { 'FamMemberID': FamMemberID +' Does Not Exist.!! If you think it exists, Check ID and enter again (make sure the ID is in Uppercase while entering.).' })
    return render(request, "searchmember.html")

def ViewDBPage(request):
    return render(request, "ViewDB.html")

def personalInfoInsert():
    return None

def insertParentsInfo():
    return None




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