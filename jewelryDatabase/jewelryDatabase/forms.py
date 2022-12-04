from django.forms import ModelForm
from .models import AuthUser

class addEmployeeForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = ('username', 'first_name', 'password', 'email', 'is_staff', 'is_superuser')