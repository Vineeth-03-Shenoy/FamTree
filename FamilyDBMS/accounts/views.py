from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages  
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
  
# Create your views here.

#signup_view method to handle HTTP requests for sign up
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data.get("username")
            #password = form.cleaned_data.get("password1")
            #email = form.cleaned_data.get("email")
            form = form.save()
            messages.success(request, 'Account created successfully')
            #new_user = authenticate(username=username)
            #if new_user is not None:
            #login(request, form)
            return render(request, 'login.html')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


#Login_view method to handle HTTP response for logging into website
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'logged in successfully')
            return render(request, 'base.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'signup.html')