from django.shortcuts import render
from . import forms
from django.contrib.auth import login, authenticate
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.conf import settings


def logout_user(request):
    logout(request)
    return redirect('login')
    
def index(request):
    now = datetime.now()

    return render(
        request,
        "authentication/index.html", 
        {
            'title': "Page of a website",
            'message': "Wahoo! It's a me, a website! ",
            'content': "Right now its " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Login failed!'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

