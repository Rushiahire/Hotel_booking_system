from django.db import models

class Customer_model(models.Model):
    customer_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=12)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    check_in = models.DateField()
