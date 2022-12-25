import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewMemberForm, DeleteMemberForm, SearchMemberForm
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
        form = NewMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(FamHome)
    form = NewMemberForm()
    return render(request, "insertdb.html", {'form': form})

def DeleteMember(request):
    if request.method=='GET':
        form = DeleteMemberForm(request.GET)
        if form.is_valid():
            instance = Family_Member.objects.filter(FamMemberID=form.FamMemberID)
            instance.delete() 
            return render(FamHome)
    form = DeleteMemberForm()
    return render(request, "deletemember.html", {'form':form}) 

def ViewPage(request):
    return render(request, "mainviewpage.html")

def ViewSearchPage(request):
    questions=None
    if request.GET.get('FamMemberID'):
        search = request.GET.get('FamMemberID')
        member = Family_Member.objects.filter(query__icontains=search)

        '''name = request.GET.get('name')
        query = Queries.object.create(query=search, user_id=name)
        query.save()'''

    return render(request, 'searchmember.html',{
        'questions': questions,
    })

def ViewDBPage(request):
    return render(request, "ViewDB.html")

def personalInfoInsert():
    return None

def insertParentsInfo():
    return None
