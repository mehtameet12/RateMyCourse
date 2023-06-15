# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect

# # Create your views here.
# def signup(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,email=email, password=password1)
#         user.save()
#         print('User Created')
#         return redirect('/')
#     else:
#         return render(request, 'index.html')


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             # User credentials are valid
#             login(request, user)
#             return redirect('home')  # Replace 'home' with the URL name of your homepage
#         else:
#             # User credentials are invalid
#             error_message = "Invalid username or password."
#             return render(request, 'index.html', {'error_message': error_message})
    
#     return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')
