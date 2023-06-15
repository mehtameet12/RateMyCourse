from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.forms.utils import ErrorList
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

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
            messages.error(request, 'You already have an account with us, please Log In instead')
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
    return render(request, 'index.html')
