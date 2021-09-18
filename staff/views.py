from typing import ContextManager
from django.contrib.auth import models
from django.shortcuts import redirect, render
from django.views import View
from customer.models import Customer_model
from customer.forms import Customer_form
from . import forms
from django.contrib.auth.models import auth


class Home(View):
    def get(self,request):
        content = {
            'add_customer':Customer_form(),
            'customer_details':Customer_model.objects.all()
        }
        return render(request,'index.html',content)

class Login(View):
    def get(self,request):
        content = {
            'login_form': forms.Login_form()
        }
        return render(request,'login_page.html',content)
    
    def post(self,request):
        user_name = request.POST['username']
        password  = request.POST['password']

        user = auth.authenticate(username=user_name,password=password)
        if user is not None:
            print("done")
            auth.login(request,user)
        return redirect('/')

class Logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')

class Booking(View):
    def get(self,request):
        if request.user.is_authenticated:
            content = {
                'display': Customer_model.objects.all()
            }
            return render(request,'display.html',content)
        else:
            return redirect('/')