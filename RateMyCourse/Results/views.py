from django.shortcuts import render
from django.http import HttpResponse

from Accounts.views import logout_view

def results(request):
    return render(request, 'results.html')
