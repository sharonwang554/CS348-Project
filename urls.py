from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('form/', views.order_form, name='form'),
    path('customer/', views.customerInfoPage, name='cust'),
    path('customerRewards/', views.customerRewards, name='custRewards')
]