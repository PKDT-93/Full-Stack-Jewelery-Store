from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader
from .models import Item
from django.db import connection

def index(request):
    print(request.user)
    return render(request, 'index.html')

def customerlist(request):
    return render(request, 'customerlist.html')

def findemployee(request):
    template = loader.get_template('findemployee.html')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Employee")
        row = cursor.fetchall()
        context = {
            'row': row,
        }
    print(row)
    return HttpResponse(template.render(context, request))
    #return render(request, 'findemployee.html')

# def items(request):
#     return render(request, 'items.html')

def items(request):
    template = loader.get_template('items.html')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Item")
        row = cursor.fetchall()
        context = {
            'row': row,
        }
    print(row)
    return HttpResponse(template.render(context, request))


# def employees(request):
#     print("Hello here")
#     template = loader.get_template('findemployee.html')
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM Employee")
#         row = cursor.fetchall()
#         context = {
#             'employee': row,
#         }
#     print(row)
#     return HttpResponse(template.render(context, request))

