import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Family_Member, Personal_Info, Couple_Family, Parents, Families, Events, MemberInvited, FamilyInvited, CoupleInvited
import time
from django.db.models import Q

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
            FamID = ins.Fname+' '+ins.Lname
            ins2 = Families.objects.get(Fam_Name=FamID)
            ins2.Members-=1
            ins2.save()
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

def ViewFamilies(request):
    Family=Families.objects.all().order_by('-Members')
    return render(request, "view_member/FamiliesinDB.html", { 'Family' : Family })

def eventmanager(request):
    return render(request, "Event_manager/eventmanager.html")

def Newevent(request):
    if request.method=="POST":
        Event_Name=request.POST['Event_Name']
        Venue=request.POST['Venue']
        Date=request.POST['Date']
        ins=Events(Event_Name=Event_Name, Venue=Venue, Date=Date)
        ins.save()
        return render(request, "Event_manager/InviteesOutput.html", { 'info' : ins })

    return render(request, "Event_manager/eventregister.html")

def DeleteEvent(request):
    if request.method=='POST':
        Event_ID=request.POST['Event_ID']
        try:
            ins=Events.objects.get(Event_ID=Event_ID)
            print(ins)
            ins.delete()
            return render(request, "Event_manager/delete successfull.html", { 'Event_ID': Event_ID+' Deleted' })
        except Family_Member.DoesNotExist:
            return render(request, "Event_manager/delete successfull.html", { 'Event_ID': Event_ID+' Does Not Exist.!! If you think it exists, Check ID and enter again' })
    return render(request, "Event_manager/deleteEvent.html")

def AlleventsDisplay(request):
    ins = Events.objects.all().order_by('Date')
    return render(request, "Event_manager/AllEvents.html", {'Event':ins})

def Invited(request):
    if request.method=='POST':
        Event_code=request.POST['Event_code']
        Member_Invited = request.POST['Member_Invited']
        Couple_invited = request.POST['Couple_invited']
        Family_invited = request.POST['Family_invited']
        print(Event_code," ",Member_Invited," ",Couple_invited," ",Family_invited)
        ins=Events.objects.get(Event_ID=Event_code)
        if len(Member_Invited)==17:
            ins2 = MemberInvited(Event_code_id=Event_code, Member_Invited_id=Member_Invited)
            ins2.save()
        if len(Couple_invited)==14:
            ins3 = CoupleInvited(Event_code_id=Event_code, Couple_invited_id=Couple_invited)
            ins3.save()
        if len(Family_invited)==6:
            ins3 = FamilyInvited(Event_code_id=Event_code, Family_invited_id=Family_invited)
            ins3.save()
        return render(request, "Event_manager/inviteesevent.html")
    return render(request, "Event_manager/inviteesevent.html")

def ViewInvitees(request):
    if request.method=='POST':
        event_id=request.POST['Event_code']
        try:
            instance = Events.objects.get(Event_ID=event_id)
        except Events.DoesNotExist:
            return render(request, 'Event_manager/searchID.html')
    # Retrieve all individual members invited to the event
        member_invites = MemberInvited.objects.filter(Event_code=event_id)
        members = []
        for invite in member_invites:
            member = invite.Member_Invited
            try:
                personal_info = member.personal_info
                members.append({
                    'name': member.Fname+" "+member.Name+" "+member.Lname,
                    'phone': personal_info.Phone,
                    'address': personal_info.Address
                })
            except Personal_Info.DoesNotExist:
                members.append({
                    'name': member.Fname+" "+member.Name+" "+member.Lname,
                    'phone': None,
                    'address': None
                })

    # Retrieve all families invited to the event
        family_invites = FamilyInvited.objects.filter(Event_code=event_id)
        families = []
        for invite in family_invites:
            family = invite.Family_invited
            try:
                familyname = Families.objects.get(Family_ID=family.pk)
                FNAME, LNAME = familyname.Fam_Name.split(" ")
                try:
                    family_members = Family_Member.objects.filter(Q(Fname=FNAME) & Q(Lname=LNAME))
                    members_details = []
                    for family_member in family_members:
                        try:
                            personal_info = family_member.personal_info
                            members_details.append({
                                'name': family_member.Name,
                                'phone': personal_info.Phone,
                                'address': personal_info.Address
                            })
                        except Personal_Info.DoesNotExist:
                            members_details.append({
                                'name': family_member.Name,
                                'phone': None,
                                'address': None
                            })
                    families.append({
                        'name': family.Fam_Name,
                        'members': members_details
                    })
                except Family_Member.DoesNotExist:
                    families.append({
                        'name': family.Fam_Name,
                        'members': []
                    })
            except Families.DoesNotExist:
                print("Family does not exist")

    # Retrieve all couples invited to the event
        couple_invites = CoupleInvited.objects.filter(Event_code=event_id)
        couples = []
        for invite in couple_invites:
            couple = invite.Couple_invited
            husband = couple.Hus
            wife = couple.Wife
            try:
                husband_personal_info = husband.personal_info
                husband_details = {
                    'name': husband.Fname+" "+husband.Name+" "+husband.Lname,
                    'phone': husband_personal_info.Phone,
                    'address': husband_personal_info.Address
                }
            except Personal_Info.DoesNotExist:
                husband_details = {
                    'name': husband.Fname+" "+husband.Name+" "+husband.Lname,
                    'phone': None,
                    'address': None
                }
            try:
                wife_personal_info = wife.personal_info
                wife_details = {
                    'name': wife.Fname+" "+wife.Name+" "+wife.Lname,
                    'phone': wife_personal_info.Phone,
                    'address': wife_personal_info.Address
                }
            except Personal_Info.DoesNotExist:
                wife_details = {
                    'name': wife.Fname+" "+wife.Name+" "+wife.Lname,
                    'phone': None,
                    'address': None
                }
            couples.append({
                'husband': husband_details,
                'wife': wife_details
            })
        context = {'info' : instance, 'members': members, 'families': families, 'couples': couples}
        return render(request, 'Event_manager/InviteesOutput.html', context)
    return render(request, 'Event_manager/searchID.html')

def About(request):
    return render(request, "About.html")

def Contact(request):
    return render(request, "contact.html")

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
