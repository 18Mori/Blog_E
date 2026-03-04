from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
  
  class Meta:
    model = User
    fields = [ 'email','username', 'password1', 'password2']
    widget = {
      'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
      'email': forms.TextInput(attrs={'class':'form-control','placeholder':'...@gmail.com'}),
      'password1': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
      'password2': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),
    }
    