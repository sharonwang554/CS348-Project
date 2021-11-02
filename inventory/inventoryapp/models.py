from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    store_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 42, default='store')
    address = models.TextField()


class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    customer_points = models.IntegerField(default=0)
    redeemed_points = models.IntegerField(default=0)


class Purchase(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    total_cost = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)


class Item(models.Model):
    item_id = models.IntegerField(default=0, primary_key=True)
    item_cost = models.IntegerField(default=0)
    item_points = models.IntegerField(default=0)


class Inventory(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(default=0)
    item_unit_cost = models.DecimalField(max_digits=6, decimal_places=2)
    last_ordered_date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_cost = models.DecimalField(max_digits=7, decimal_places=2)
    delivery_date = models.DateTimeField(auto_now_add=True)

# Create your models here.
