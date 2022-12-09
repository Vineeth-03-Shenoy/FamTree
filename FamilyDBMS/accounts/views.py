from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages  
#from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
  
# Create your views here.

#signup_view method to handle HTTP requests for sign up
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form = form.save()
            #login(request, user)
            return render(request, 'login.html')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


#Login_view method to handle HTTP response for logging into website
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'base.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'signup.html')