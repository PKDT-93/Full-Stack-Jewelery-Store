"""jewelryDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from codecs import register
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('addresses', views.address, name='adresses'),
    path('purchase', views.purchaseHistory, name='purchase'),
    path('purchase/addPurchase', views.addpurchase, name='addPurchase'),
    path('rawInventory', views.rawInventory, name='rawInventory'),
    path('rawInventory/addGem', views.addGem, name='addGem'),
    path('rawInventory/addMetal', views.addMetal, name='addMetal'),
    path('store', views.store, name='store'),
    path('supplier', views.supplier, name='supplier'),
    path('customerlist', views.customerlist, name='customerlist'),
    path('findemployee', views.findemployee, name='findemployee'),
    path('managers', views.managers, name='managers'),
    path('items', views.items, name='items'),
    path('services', views.services, name='services'),
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name="logout"),
    path('items/lookup', views.filterItem, name='filterItem'),
    path('items/additem', views.addItem, name='addItemForm'),
    path('suppliers/addsupplier', views.addSupplier, name='addSupplier'),
    path('suppliers/deletesupplier', views.deleteSupplier, name='deleteSupplier'),
    path('customers/addcustomer', views.addCustomer, name='addCustomer'),
    path('employees/addemployee', views.addEmployee, name='addEmployee'),
    path('employees/deleteEmployee', views.deleteEmployee, name='deleteEmployee'),
    path('customers/updateemail', views.updateEmail, name='updateEmail'),
    path('employees/updateemail', views.updateEmployeeEmail, name='updateEmployeeEmail'),
    path('items/changeinventory', views.changeInventory, name='changeInventory'),
]
