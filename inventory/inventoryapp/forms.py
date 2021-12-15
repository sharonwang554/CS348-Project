from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["item1", "item1_q", "customer_id", "employee_id"]
        labels = {"item1": "Item", "item1_q": "Quantity", "customer_id": "Customer ID", "employee_id": "Employee ID"}
