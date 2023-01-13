import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Family_Member, Personal_Info, Couple_Family, Parents, Families
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
            ID, FamID = ID_Creator(Fname.upper(),Name.upper(),Lname.upper(),DoB,collval)
            try:
                obj=Family_Member.objects.get(FamMemberID=ID)
                collval+=1
            except Family_Member.DoesNotExist:
                FamMemberID=ID
                break

        if collval==5:
            print("ID could not be genrated, please contact admin",Fname,Name,Lname,DoB,Gender)

        ins = Family_Member(FamMemberID=FamMemberID, Fname=Fname,Name=Name,Lname=Lname,DoB=DoB,Gender=Gender)
        if Families.objects.filter(Family_ID=FamID).exists():
            ins2 = Families.objects.get(Family_ID=FamID)
            ins2.Members+=1
            ins2.save()
            ins.save()
        else:
            ins2=Families(Family_ID=FamID, Fam_Name=Fname+' '+Lname, Members=1)
            ins2.save()
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
    if request.method=='POST':
        Hus=request.POST['Hus']
        Wife=request.POST['Wife']
        Wed_ann=request.POST['Wed_ann']
        Couple_ID = Wed_ann[0:4]+Hus[7:10]+Wife[7:10]+Wed_ann[5:7]+Wed_ann[8:10]
        print(Couple_ID)
        try:
            FamMember=Family_Member.objects.get(FamMemberID=Hus)
            FamMember=Family_Member.objects.get(FamMemberID=Wife)
            ins=Couple_Family(Couple_ID=Couple_ID, Hus_id=Hus, Wife_id=Wife, Wed_ann=Wed_ann)
            ins.save()
            data = Couple_Family.objects.get(Couple_ID=Couple_ID)
            Husband = Family_Member.objects.get(FamMemberID=Hus)
            Wife__ = Family_Member.objects.get(FamMemberID=Wife)
            return render(request,"Couple/insertCsuccess.html",{ 'data':data,'Husband':Husband,'Wife':Wife__} )
        except Family_Member.DoesNotExist:
            return render(request,"Couple/insertCfail.html")
    return render(request, "Couple/insertCouple.html")
    
def ViewCoupleDB(request):
    FamMember=Couple_Family.objects.all().order_by('Couple_ID')
    return render(request, "Couple/viewCoupleDB.html", { 'FamMember' : FamMember })
    
def insertParentsInfo(request):
    if request.method=='POST':
        child_ID_id=request.POST['child_ID_id']
        parents_ID_id=request.POST['parents_ID']
        try:
            ID=Couple_Family.objects.get(Couple_ID=parents_ID_id)
            ID=Family_Member.objects.get(FamMemberID=child_ID_id)
            ins = Parents(child_ID_id=child_ID_id,  parents_ID_id=parents_ID_id)
            ins.save()
            data = Couple_Family.objects.get(Couple_ID=parents_ID_id)
            Father = Family_Member.objects.get(FamMemberID=data.Hus_id)
            Mother = Family_Member.objects.get(FamMemberID=data.Wife_id)
            Child = Family_Member.objects.get(FamMemberID=child_ID_id)
            return render(request,"Parents/insertSuccess.html",{ 'data':data,'Father':Father,'Mother':Mother,'Child':Child})
        except Couple_Family.DoesNotExist or Family_Member.DoesNotExist:
            return render(request,"Parents/insertFail.html")
    return render(request,"Parents/insertParents.html")

def ViewParentsDB(request):
    FamMember=Parents.objects.all().order_by('parents_ID_id')
    return render(request, "Parents/viewParentsDB.html", { 'FamMember' : FamMember })

def ViewSearchParents(request):
    if request.method=='POST':
        child_ID_id=request.POST['child_ID_id']
        data = Parents.objects.get(child_ID_id=child_ID_id)
        data2 = Couple_Family.objects.get(Couple_ID=data.parents_ID_id)
        Father = Family_Member.objects.get(FamMemberID=data2.Hus_id)
        Mother = Family_Member.objects.get(FamMemberID=data2.Wife_id)
        Child = Family_Member.objects.get(FamMemberID=child_ID_id)
        return render(request,"Parents/insertSuccess.html",{ 'data':data2,'Father':Father,'Mother':Mother,'Child':Child})
    return render(request, "Parents/searchID.html" )

def ViewSearchChildren(request):
    if request.method=='POST':
        parents_ID_id=request.POST['parents_id']
        try:
            data2 = Couple_Family.objects.get(Couple_ID=parents_ID_id)
            Father = Family_Member.objects.get(FamMemberID=data2.Hus_id)
            Mother = Family_Member.objects.get(FamMemberID=data2.Wife_id)
            list = Parents.objects.filter(parents_ID_id=parents_ID_id)
            print(list)
            list2=[]
            for child in list:
                list2+=[Family_Member.objects.get(FamMemberID=child.child_ID_id)]
            return render(request, "Parents/children.html", { 'data':data2,'Father':Father,'Mother':Mother,'list':list2})
        except Family_Member.DoesNotExist:
            return render(request, "Parents/children.html")
    return render(request, "Parents/searchByParent.html")

def eventmanager(request):
    return render(request, "Event_manager/eventmanager.html")

def Newevent(request):
    return render(request, "Event_manager/eventregister.html")

def Invitees(request):
    return render(request, "Event_manager/inviteesevent.html")

def ViewEvent(request):
    return render(request, "Event_manager/viewevent.html")

def Famtree(request):
    if request.method=='POST':
        start_id=request.POST['sourceMember']
        end_id=request.POST['targetMember']
        path = trace_path(start_id, end_id)
        path.reverse()
        path = list(dict.fromkeys(path))
        path.reverse()
        print(path)
    return render(request, "treetrace.html")

def ID_Creator(Fname,name,Lname,Dob,coll_val):
    firname = Fname[0]+Fname[(len(Fname)//2)]+Fname[len(Fname)-1]
    lastname = Lname[0]+Lname[(len(Lname)//2)]+Lname[len(Lname)-1]
    FamID = firname+lastname
    if coll_val==0:                                                                     #for the first time
        midname = name[0]+name[(len(name)//2)-1]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID,FamID
    elif coll_val==1:
        midname = name[0]+name[(len(name)//2)-2]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID,FamID
    elif coll_val==2:
        midname = name[0]+name[(len(name)//2)]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID,FamID
    elif coll_val==3:
        midname = name[0]+name[(len(name)//2)+1]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID,FamID
    elif coll_val==4:
        midname = name[0]+name[(len(name)//2)+2]+name[len(name)-1]
        ID = Dob[:4]+firname+midname+lastname+Dob[5:7]+Dob[8:10]
        return ID,FamID


def find_children(fam_member_id):
    children = Parents.objects.filter(parents_ID__Hus=fam_member_id) | Parents.objects.filter(parents_ID__Wife=fam_member_id)
    children_id = [child.child_ID.FamMemberID for child in children]
    return children_id

def trace_path(start, end):
    # Base case: if start and end are the same, return the path
    if start == end:
        return [start]
    path = []
    try:
        # check if the start member is a child
        child = Parents.objects.get(child_ID=start)
        # get the parent couple
        couple = child.parents_ID
        # check if the end member is a parent
        if couple.Hus.FamMemberID == end or couple.Wife.FamMemberID == end:
            return [start, couple.Hus.FamMemberID, couple.Wife.FamMemberID, end]
        else:
            # check if the end member is a child
            path = trace_path(couple.Hus.FamMemberID, end)
            if not path:
                path = trace_path(couple.Wife.FamMemberID, end)
            if path:
                path.insert(0, start)
            else:
                # check if the end member is a grandchild
                children = find_children(start)
                for child in children:
                    path = trace_path(child, end)
                    if path:
                        path.insert(0, start)
                        break
    except Parents.DoesNotExist:
        # check if the start member is a parent
        couple = Couple_Family.objects.get(Hus=start)
        if couple.Wife.FamMemberID == end:
            return [start, end]
        else:
            # check if the end member is a child
            path = trace_path(couple.Wife.FamMemberID, end)
            if path:
                path.insert(0, start)
            else:
                # check if the end member is a grandchild
                children = find_children(start)
                for child in children:
                    path = trace_path(child, end)
                    if path:
                        path.insert(0, start)
                        break
    except Couple_Family.DoesNotExist:
        pass
    return path
