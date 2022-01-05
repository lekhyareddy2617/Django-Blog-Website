from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): #inherits user creation from
    email=forms.EmailField()
    class Meta: #model that will be affected is User model and the fields are the fields we want in the form and the order
        model=User 
        fields=['username','email','password1','password2'] #password1 is password and password2 is the confirmation