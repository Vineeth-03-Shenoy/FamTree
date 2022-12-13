import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def insertNewMember(request):
    today = datetime.datetime.now().date()
    return render(request, "famapp.html", {"today":today})


def personalInfoInsert():
    return None

def insertParentsInfo():
    return None
