from django.db import models, transaction
from django.contrib.auth.models import User
from django.db import connection



class Item(models.Model):
    item_cost = models.IntegerField(models.DecimalField(max_digits=6, decimal_places=2), default=0)
    item_price = models.IntegerField(models.DecimalField(max_digits=6, decimal_places=2), default=0)


class Inventory(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_stock = models.IntegerField(default=0)
    units_sold = models.IntegerField(default=0)



class Customer(models.Model):
    name = models.CharField(max_length=40, null = True)
    address = models.CharField(max_length=100, null=True)

    
    


class Customer_rewards(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rewards_points = models.IntegerField(default=0)
    has_rewards = models.BooleanField(default=False)


class Employee(models.Model):
    name = models.CharField(max_length=40, null=True)


class Employee_bonus(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    total_profit_sold = models.IntegerField(models.DecimalField(max_digits=6, decimal_places=2), default=0)
    number_items_sold = models.IntegerField(default=0)
    bonus = models.IntegerField(models.DecimalField(max_digits=6, decimal_places=2))


class Order(models.Model):
    item1 = models.ForeignKey(Item, on_delete=models.CASCADE)
    item1_q = models.IntegerField(default=0)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)



# class Order_info(models.Model):
#     order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
#     total_cost = models.IntegerField(models.DecimalField(max_digits=6, decimal_places=2))
#     total_price = models.IntegerField(models.DecimalField(max_digits=6, decimal_places=2))



class Profit(models.Model):
    month = models.CharField(max_length = 10, null=True)
    profit = models.IntegerField(default = 0)

# Create your models here.
