from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(requets):
    text="""<h1>welcome to my famapp !</h1>"""
    return HttpResponse(text)