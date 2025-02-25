from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.forms.utils import ErrorList
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import json
from .forms import LoginForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Welcome back, please LogIn')
            return redirect('/')
        elif password1!=password2:
            messages.error(request, 'Passwords do not match! Please try again!')
            return redirect('/')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,email=email, password=password1)
            user.save()
            print('User Created')
            return redirect('/') 
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged In')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            form = LoginForm()
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return render(request, 'index.html', {'user': request.user})
        else:
            form = LoginForm()
            return render(request, 'index.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/')