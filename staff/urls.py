from django.urls import path
from . import views
from customer.views import New_customer,Details


urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('add_customer',New_customer.as_view(),name='new_customer'),
    path('customer_details/',Details.as_view(),name='details'),
    path('login/',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name="logout"),
    path('booking',views.Booking.as_view(),name='booking')
]