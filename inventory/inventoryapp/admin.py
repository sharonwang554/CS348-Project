from django.contrib import admin
from inventoryapp.models import Item
from inventoryapp.models import Inventory
from inventoryapp.models import Order
#from inventoryapp.models import Order_info
from inventoryapp.models import Employee
from inventoryapp.models import Employee_bonus
from inventoryapp.models import Customer
from inventoryapp.models import Customer_rewards
from inventoryapp.models import Profit

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(Order)
#admin.site.register(Order_info)
admin.site.register(Employee)
admin.site.register(Employee_bonus)
admin.site.register(Customer_rewards)
admin.site.register(Profit)

# Register your models here.
