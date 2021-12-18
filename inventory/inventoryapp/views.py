from django.shortcuts import render
from django.http import HttpResponse
from inventoryapp.models import Item, Inventory, Customer, Customer_rewards, Employee, Employee_bonus, Order, Profit
from django.db.models import Avg, Max, Min, Sum, Count
from django.db import transaction
# Create your views here.

@transaction.atomic
def profitpage(response):
    profit_query = '''
    
        select ord.id, monthname(date) as month,count(item1_q) as num_item_sold, 
            sum(item_cost) as total_expenses, sum(item_price) as total_revenue, sum(item_price-item_cost) as total_profit
        from inventoryapp_item itm join inventoryapp_order ord on itm.id = ord.item1_id
        group by month;
        '''
    profit_by_month = Profit.objects.raw(profit_query)

    profit_query_item = '''
            select itm.id, count(item1_q) as num_item_sold,
                sum(item_cost) as total_expenses, sum(item_price) as total_revenue, sum(item_price-item_cost) as total_profit
            from inventoryapp_item itm join inventoryapp_order ord on itm.id = ord.item1_id
            group by itm.id;
            '''
    profit_by_item = Profit.objects.raw(profit_query_item)



    profit_query = '''

            select ord.id, monthname(date) as month,sum(item1_q) as num_item_sold, 
                sum(item_cost) as total_expenses, sum(item_price) as total_revenue, sum(item_price-item_cost) as total_profit
            from inventoryapp_item itm join inventoryapp_order ord on itm.id = ord.item1_id
            group by month;
            '''
    profit_month_overview_b = Profit.objects.raw(profit_query)

    return render(response, 'inventoryapp/profitpage.html', {'ProfitMonth': profit_by_month, 'ProfitItem':profit_by_item, 'ProfitMonthOverviewB': profit_month_overview_b})


