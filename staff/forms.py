from django import forms
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput

class Login_form(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=PasswordInput())