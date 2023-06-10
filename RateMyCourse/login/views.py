# from django.shortcuts import render
# from django.http import HttpResponse

# def login(request):
#     return render(request, 'login.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User credentials are valid
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your homepage
        else:
            # User credentials are invalid
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')
