from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def customerlist(request):
    return render(request, 'customerlist.html')

def findemployee(request):
    return render(request, 'findemployee.html')
