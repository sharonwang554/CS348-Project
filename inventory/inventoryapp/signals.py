from django.db.models.signals import post_save
from django.dispatch import receiver
from inventoryapp.models import Item, Inventory, Customer, Customer_rewards, Employee, Employee_bonus, Order, Profit
from django.db.models import F
from django.db import connection

@receiver(post_save, sender=Order)
def update_bonus(sender, instance=None, created=False, **kwargs):
    if created:
        with connection.cursor() as cursor:
            cursor.execute("select (o.item1_q*i.item_price) as profit from inventoryapp_order o  join inventoryapp_item i on o.item1_id = i.id where o.id = (select max(id) from inventoryapp_order)")
            # get a single line from the result
            row = cursor.fetchone()
            # get the value in the first column of the result (the only column)
            new_order_profit = row[0]

        for e in Employee_bonus.objects.filter(employee_id_id=instance.employee_id_id):
         e.total_profit_sold += new_order_profit
         e.bonus = e.total_profit_sold*0.1
         e.number_items_sold += instance.item1_q
         e.save()