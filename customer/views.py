from django.shortcuts import redirect, render
from django.views import View
from . import forms
from .import models

class New_customer(View):
    def get(self,request):
        content = {
            'add_customer' : forms.Customer_form(),
            'customer_details' : models.Customer_model.objects.all() 
        }
        return render(request,'add_customer.html',content)
    
    def post(self,request):
        customer_name = request.POST['customer_name']
        contact_no = request.POST['contact_no']
        state = request.POST['state']
        city = request.POST['city']
        check_in = request.POST['check_in']
        new_customer = models.Customer_model(
            customer_name = customer_name,
            contact_no = contact_no,
            state = state,
            city = city,
            check_in = check_in,
        )
        new_customer.save()
        print('Done')
        return redirect('/')

class Details(View):
    def get(self,request):
        customer_id = request.GET['customer_id']
        content = {
            'detail': models.Customer_model.objects.get(id=customer_id)
        }
        return render(request,'customer_details.html',content)

