from django import forms
from django.forms import ModelForm
from .models import AuthUser, Supplier
from .models import Item

class addEmployeeForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = ('username', 'first_name', 'password', 'email', 'is_staff', 'is_superuser')

class addItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class addSupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
