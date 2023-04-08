from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class addform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']        