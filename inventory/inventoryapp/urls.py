from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('form/', views.order_form, name='form')
]