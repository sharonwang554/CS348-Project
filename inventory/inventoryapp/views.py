from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.
def order_form(request):
  if request.method == "POST":
    form = OrderForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = OrderForm()
  return render(request, 'order.html', {'form': form})