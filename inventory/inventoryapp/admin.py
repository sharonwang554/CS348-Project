from django.contrib import admin
from inventoryapp.models import Store
from inventoryapp.models import Customer
from inventoryapp.models import Purchase
from inventoryapp.models import Item
from inventoryapp.models import Inventory
from inventoryapp.models import Order

admin.site.register(Store)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(Order)

# Register your models here.
