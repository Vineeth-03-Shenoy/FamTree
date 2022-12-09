from django.shortcuts import render
from login.forms import LoginForm

# Create your views here.
def login_action(request):
    username = "not logged in"
    if request.method=="POST":
        MyLoginForm  = LoginForm(request.POST)
        
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
        
    else:
        MyLoginForm = LoginForm()

    return render(request, 'loggedin.html', {"username": username})

