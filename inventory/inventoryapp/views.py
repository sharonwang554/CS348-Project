from django.shortcuts import render
from django.http import HttpResponse
from inventoryapp.models import Item, Inventory, Customer, Customer_rewards, Employee, Employee_bonus, Order, Profit
from django.db.models import Avg, Max, Min, Sum, Count

# Create your views here.

def employeepage(response): 
    report_query = '''select 1 as id, employee_id_id as employee_id, name, item1_id, item_price, sum(item1_q) as quantity, sum(item_price * item1_q) as total_profit
    from inventoryapp_item i join inventoryapp_order o on i.id = o.item1_id join inventoryapp_employee e on e.id=o.employee_id_id 
    group by employee_id_id;
    '''
    all_employee = Employee.objects.raw(report_query)

    most_sales_query = '''select 1 as id, employee_id_id as employee_id, name, item1_id, item_price, sum(item1_q) as quantity, sum(item_price * item1_q) as total_profit
    from inventoryapp_item i join inventoryapp_order o on i.id = o.item1_id join inventoryapp_employee e on e.id=o.employee_id_id 
    group by employee_id_id
    having total_profit = (select max(total_profit_sold) from inventoryapp_employee_bonus);
    '''
    most_sales_employee = Employee.objects.raw(most_sales_query)

    bonus_query = '''select e.id, e.name, b.bonus from inventoryapp_employee e join inventoryapp_employee_bonus b on
    e.id=b.employee_id_id;'''
    employee_bonus = Employee.objects.raw(bonus_query)

    return render(response, "inventoryapp/employeepage.html", {'Employee': all_employee, 'Most_Sales': most_sales_employee, 'Bonus': employee_bonus})