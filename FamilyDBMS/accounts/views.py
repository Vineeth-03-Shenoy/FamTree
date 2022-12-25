
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages  
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from famapp.views import home, FamHome

# Create your views here.

#signup_view method to handle HTTP requests for sign up
def signup_view(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Account created successfully')
            login(request, form)
            return redirect(FamHome)
    return render(request, 'signup.html', {'form': form})


#Login_view method to handle HTTP response for logging into website
def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(FamHome)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(signup_view)