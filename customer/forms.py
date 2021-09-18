from django import forms

class Customer_form(forms.Form):
    customer_name = forms.CharField(max_length=30)
    contact_no = forms.CharField(max_length=12)
    state = forms.CharField(max_length=20)
    city = forms.CharField(max_length=30)
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))