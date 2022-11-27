from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    print(request.user)
    return render(request, 'index.html')

def customerlist(request):
    return render(request, 'customerlist.html')

def findemployee(request):
    return render(request, 'findemployee.html')
    