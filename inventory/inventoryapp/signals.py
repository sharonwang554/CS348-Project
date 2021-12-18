from django.db.models.signals import post_save
from django.dispatch import receiver
from inventoryapp.models import Item, Inventory, Customer, Customer_rewards, Employee, Employee_bonus, Order, Profit
from django.db.models import F
from django.db import connection
from django.db import connections
from django.db import transaction


@transaction.atomic
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


@transaction.atomic
@receiver(post_save, sender=Order)
def update_monthly_profit(sender, instance=None, created=False, **kwargs):
    if created:
        with connection.cursor() as cursor:
            cursor.execute('''
                            select ord.id, monthname(date) as month,sum(item1_q) as num_item_sold, 
                            sum(item_cost) as total_expenses, sum(item_price) as total_revenue, sum(item_price-item_cost) as total_profit
                            from inventoryapp_item itm join inventoryapp_order ord on itm.id = ord.item1_id 
                            group by month
                            having max(ord.item1_id);
                            ''')

            # get a single line from the result
            row = cursor.fetchone()
            # get the value in the first column of the result (the only column)
            month = row[1].strftime('%B')
            total_profit = row[6]

            for rec in Profit.objects(date=instance.date):
                rec.profit += total_profit
                rec.save()


@transaction.atomic
@receiver(post_save, sender=Order)
def update_rwdPoints(sender, instance=None, created=False, **kwargs):
    for e in Customer_rewards.objects.filter(customer_id_id=instance.customer_id):
        e.rewards_points += 15
        if e.rewards_points > 99:
            e.has_rewards = 1
    e.save()
