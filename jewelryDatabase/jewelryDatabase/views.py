from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader
from django.db import connection

def index(request):
    print(request.user)
    return render(request, 'index.html')

def customerlist(request):
    template = loader.get_template('customerlist.html')
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT ID, FirstName, LastName, Email FROM Person WHERE Customer = 1")
        row = cursor.fetchall()
        context = {
            'row': row,
        }
    print(row)
    return HttpResponse(template.render(context, request))

def addCustomer(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        email = request.POST.get('email', None)
        customer = 1
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Person (FirstName, LastName, Email, Customer) VALUES (%s, %s, %s, %s)",
                           (firstname, lastname, email, customer))
            return redirect('/customerlist')
    return render(request, 'customers/addcustomer.html')


def findemployee(request):
    if not request.user.is_superuser:
        return redirect('/')

    template = loader.get_template('findemployee.html')
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT Employee.StoreID, Employee.PersonID, Employee.ESSN, Person.FirstName, Person.LastName, Person.Email FROM Employee, Person WHERE Employee.PersonID = ID")
        row = cursor.fetchall()
        context = {
            'row': row,
        }
    print(row)
    return HttpResponse(template.render(context, request))


def purchaseHistory(request):
    template = loader.get_template('purchase.html')
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Purchase JOIN Person ON Person.ID = Purchase.PersonID")
        row = cursor.fetchall()
        context = {
            'row': row,
        }
    print(row)
    return HttpResponse(template.render(context, request))


def items(request):
    template = loader.get_template('items.html')
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT Item.ItemID, Item.Barcode, Item.Weight, Item.Price, Item.Type, SoldAt.StoreID, SoldAt.Stock FROM Item, SoldAt WHERE SoldAt.ItemID = Item.ItemID")
        row = cursor.fetchall()
        context = {
            'row': row,
        }
    print(row)
    return HttpResponse(template.render(context, request))


def filterItem(request):
    searchWord = request.POST.get('system', None)
    template = loader.get_template('items/lookup.html')
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Item WHERE Type = %s", [searchWord])
        row = cursor.fetchall()
        context = {
            'row': row,
        }
    print(row)
    return HttpResponse(template.render(context, request))

def supplier(request):
    if not request.user.is_superuser:
        return redirect('/')
    else:
        template = loader.get_template('supplier.html')
        print(template)
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Supplier")
            row = cursor.fetchall()
            context = {
                'row': row,
            }
        print(row)
        return HttpResponse(template.render(context, request))

def deleteSupplier(request):
    if not request.user.is_superuser:
        return redirect('/')

    if request.method == 'POST':
        supplierID = request.POST.get('deletesupplier', None)
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM Supplier WHERE SupplierID = %s", [supplierID])
            return redirect('/supplier')
    return render(request, 'suppliers/deletesupplier.html')

def store(request):
    template = loader.get_template('store.html')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Store")
        row = cursor.fetchall()
        context = {
            'row': row,
        }
    print(row)
    return HttpResponse(template.render(context, request))


def rawInventory(request):
    template = loader.get_template('rawInventory.html')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Gems")
        row = cursor.fetchall()
        context = {
            'row': row,
        }
    print(row)
    return HttpResponse(template.render(context, request))

def addEmployee(request):
    if not request.user.is_superuser:
        return redirect('/')
    if request.method == 'POST':
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        email = request.POST.get('email', None)
        storeid = request.POST.get('storeid', None)
        ssn = request.POST.get('ssn', None)
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Person (FirstName, LastName, Email, Customer) Values (%s, %s, %s, %s)", (firstname, lastname, email, 0)
            )
            cursor.execute("SELECT ID FROM Person WHERE Person.Email = %s", [email])
            val = cursor.fetchone()
            output = int (val[0])
            print(output)
            cursor.execute("INSERT INTO Employee (StoreID, PersonID, ESSN) Values (%s, %s, %s)", (storeid, output, ssn))
            return redirect('/employee')
    return render(request,'employees/addemployee.html')

def deleteEmployee(request):
    if not request.user.is_superuser:
        return redirect('/')
    if request.method == 'POST':
        id = request.POST.get('personid', None)
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Employee WHERE Employee.PersonID = %s", [id])
            cursor.execute("UPDATE Person SET Customer = 1 WHERE ID = %s", [id])
            return redirect('/findemployee')
    return render(request, 'employees/deleteEmployee.html')

def updateEmail(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        email = request.POST.get('email')
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Person SET Email = %s WHERE ID = %s", (email,id))
            return redirect('/customerlist')
    return render(request, 'customers/updateemail.html')

def updateEmployeeEmail(request):
    if not request.user.is_superuser:
        return redirect('/')
        
    if request.method == 'POST':
        id = request.POST.get('id')
        email = request.POST.get('email')
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Person SET Email = %s WHERE ID = %s", (email,id))
            return redirect('/findemployee')
    return render(request, 'customers/updateemail.html')

def addItem(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode', None)
        weight = request.POST.get('weight', None)
        price = request.POST.get('price', None)
        type = request.POST.get('type', None)
        stock = request.POST.get('stock', None)
        store = request.POST.get('store', None)
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Item (Barcode, Weight, Price, Type) VALUES (%s, %s, %s, %s)", (barcode, weight, price, type))
            cursor.execute("SELECT ItemID FROM Item WHERE Item.Barcode = %s", [barcode])
            val = cursor.fetchone()
            output = int (val[0])
            print(output)
            cursor.execute("INSERT INTO SoldAt(StoreID, ItemID, ItemBarcode, Stock) VALUES (%s, %s, %s, %s)", (store, output, barcode, stock))
            return redirect('/items')
    return render(request, 'items/additem.html')

def changeInventory(request):
    if request.method == 'POST':
        itemid = request.POST.get('itemid', None)
        storeid = request.POST.get('storeid', None)
        amount = request.POST.get('amount', None)
        with connection.cursor() as cursor:
            cursor.execute("UPDATE SoldAt SET Stock = %s WHERE StoreID = %s AND ItemID = %s", (amount, storeid, itemid))
            return redirect('/items')
    return render(request, 'items/changeinventory.html')

# def deleteItem(request):
#     if request.method == 'POST':
#         itemid = request.POST.get('deleteitem', None)
#         with connection.cursor() as cursor:
#             cursor.execute("DELETE FROM Item WHERE Item.ItemID = %s", [itemid])
#             return redirect('/items')
#     return render(request, 'items/deleteitem.html')

def addSupplier(request):
    if not request.user.is_superuser:
        return redirect('/')
    if request.method == 'POST':
        suppliername = request.POST.get('SupplierName')
        supplierEmail = request.POST.get('SupplierEmail')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Supplier(SupplierName, SupplierEmail) Values (%s, %s)", (suppliername, supplierEmail))
            return redirect('/supplier')
    return render(request, 'suppliers/addsupplier.html')