from django.db.models.signals import post_save
from django.dispatch import receiver
from inventoryapp.models import Item, Inventory, Customer, Customer_rewards, Employee, Employee_bonus, Order, Profit
from django.db.models import F
from django.db import connection, transaction


# TRANSACTION RUNS AFTER AN ORDER IS SUBMITTED
@transaction.atomic
@receiver(post_save, sender=Order)
def update_rwdPoints(sender, instance=None, created=False, **kwargs):
    for e in Customer_rewards.objects.filter(customer_id_id=instance.customer_id):
        e.rewards_points += 15
        if e.rewards_points > 99:
            e.has_rewards = 1
    e.save()

