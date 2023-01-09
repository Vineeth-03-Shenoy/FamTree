import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Family_Member, Personal_Info
import time

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
        return render(request, "insert_member/insert successfull.html", { 'FamMemberID': FamMemberID })
    return render(request, "insert_member/insertdb.html")

def DeleteMember(request):
    if request.method=='POST':
        FamMemberID=request.POST['FamMemberID']
        try:
            ins=Family_Member.objects.get(FamMemberID=FamMemberID)
            print(ins)
            ins.delete()
            return render(request, "delete_member/delete successfull.html", { 'FamMemberID': FamMemberID+' Deleted' })
        except Family_Member.DoesNotExist:
            return render(request, "delete_member/delete successfull.html", { 'FamMemberID': FamMemberID+' Does Not Exist.!! If you think it exists, Check ID and enter again (make sure the ID is in Uppercase while entering.).' })
        
    return render(request, "delete_member/deletemember.html") 

def ViewPage(request):
    return render(request, "view_member/mainviewpage.html")

def ViewSearchIDPage(request):
    if request.method=='POST':
        FamMemberID=request.POST['FamMemberID']
        try:
            FamMember=[Family_Member.objects.get(FamMemberID=FamMemberID)]
            return render(request, "view_member/searchOutput.html", { 'FamMember' : FamMember })
        except Family_Member.DoesNotExist:
            return render(request, "view_member/searchOutput.html")
    return render(request, "view_member/searchID.html")

def ViewSearchNamePage(request):
    if request.method=='POST':
        Name=request.POST['Name']
        try:
            FamMember=Family_Member.objects.filter(Name=Name).order_by('DoB')
            return render(request, "view_member/searchOutput.html", { 'FamMember' : FamMember })
        except Family_Member.DoesNotExist:
            return render(request, "view_member/searchOutput.html")
    return render(request, "view_member/searchName.html")

def ViewDBPage(request):
    FamMember=Family_Member.objects.all().order_by('FamMemberID')
    return render(request, "view_member/searchOutput.html", { 'FamMember' : FamMember })

def UpdateDetails(request):
    if request.method=='POST':
        FamMemberID=request.POST['FamMemberID']
        DoD = request.POST['DoD']
        Gender = request.POST['Gender']
        FamMember=Family_Member.objects.get(FamMemberID=FamMemberID)
        if len(DoD)>1:
            FamMember.DoD=DoD
        if len(Gender)==1:
            FamMember.Gender=Gender    
        FamMember.save()
        FamMember=[Family_Member.objects.get(FamMemberID=FamMemberID)]
        return render(request, "update_member/updateSuccessfull.html", { 'FamMember': FamMember })
    return render(request, "update_member/updatedetails.html")

def personalInfoInsert(request):
    if request.method=='POST':
        member_ID_id=request.POST['FamMemberID']
        Email=request.POST['Email']
        Address=request.POST['Address']
        Ph_prefix=request.POST['Ph_prefix']
        Phone=request.POST['Phone']
        City=request.POST['City']
        Country=request.POST['Country']
        Pincode=request.POST['pincode']
        Job_or_student=request.POST['Job_or_student']
        Company_or_School=request.POST['Company_or_School']
        try:
            FamMember=Family_Member.objects.get(FamMemberID=member_ID_id)
            ins = Personal_Info(member_ID_id=member_ID_id, 
                                Ph_prefix=Ph_prefix,
                                Phone=Phone,
                                Address=Address,
                                City=City,
                                Country=Country,
                                Pincode=Pincode,
                                Email=Email,
                                Job_or_student=Job_or_student,
                                Company_or_School=Company_or_School)
            ins.save()
            FamMember=Family_Member.objects.get(FamMemberID=member_ID_id)
            MemberPersonal=Personal_Info.objects.get(member_ID_id=member_ID_id)
            return render(request, "personal_info/Output.html", { 'FamMember' : FamMember ,'info' : MemberPersonal })
        except Family_Member.DoesNotExist:
            return render(request, "personal_info/Output.html")
    return render(request, "personal_info/personalinfo.html")

def personalInfoSearch(request):
    if request.method=='POST':
        FamMemberID=request.POST['FamMemberID']
        try:
            FamMember=Family_Member.objects.get(FamMemberID=FamMemberID)
            MemberPersonal=Personal_Info.objects.get(member_ID_id=FamMemberID)
            return render(request, "personal_info/Output.html", { 'FamMember' : FamMember ,'info' : MemberPersonal })
        except Family_Member.DoesNotExist:
            return render(request, "personal_info/Output.html")
    return render(request, "personal_info/searchID.html")


def insertCoupleInfo(request):
    return render(request, "Couple&parents/insertCouple.html")
    

def insertParentsInfo():

    return None


def eventmanager(request):
    return render(request, "Event_manager/eventmanager.html")

def Newevent(request):
    return render(request, "Event_manager/eventregister.html")

def Invitees(request):
    return render(request, "Event_manager/inviteesevent.html")

def ViewEvent(request):
    return render(request, "Event_manager/viewevent.html")

def ID_Creator(Fname,name,Lname,Dob,coll_val):
    firname = Fname[0]+Fname[(len(Fname)//2)]+Fname[len(Fname)-1]
    lastname = Lname[0]+Lname[(len(Lname)//2)]+Lname[len(Lname)-1]
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