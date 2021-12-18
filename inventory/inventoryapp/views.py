from django.shortcuts import render
from .forms import OrderForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from inventoryapp.models import Item, Inventory, Customer, Customer_rewards, Employee, Employee_bonus, Order, Profit
from django.db.models import Avg, Max, Min, Sum, Count
from django.db import transaction


# Create your views here.
def order_form(request):
    query = '''select 1 as id, (item_price*item1_q) as total from inventoryapp_order t1 
    join inventoryapp_item t2 on t1.item1_id = t2.id order by t1.id desc limit 1;'''
    total = Order.objects.raw(query)

    submitted = False
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventoryapp/form?submitted=True')
    else:
        form = OrderForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'order.html', {'form': form, 'submitted':submitted, 'total':total})


@transaction.atomic
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

    return render(response, "employeepage.html", {'Employee': all_employee, 'Most_Sales': most_sales_employee, 'Bonus': employee_bonus})


@transaction.atomic
def profitpage(response):
    profit_query = '''

        select ord.id, monthname(date) as month,sum(item1_q) as num_item_sold, 
            sum(item_cost) as total_expenses, sum(item_price) as total_revenue, sum(((item_price-item_cost) * item1_q)) as total_profit
        from inventoryapp_item itm join inventoryapp_order ord on itm.id = ord.item1_id
        group by month;
        '''
    profit_by_month = Profit.objects.raw(profit_query)

    profit_query_item = '''
            select itm.id, sum(item1_q) as num_item_sold,
                sum(item_cost) as total_expenses, sum(item_price) as total_revenue, sum(((item_price-item_cost) * item1_q)) as total_profit
            from inventoryapp_item itm join inventoryapp_order ord on itm.id = ord.item1_id
            group by itm.id;
            '''
    profit_by_item = Profit.objects.raw(profit_query_item)

    profit_query = '''
            select ord.id, monthname(date) as month,sum(item1_q) as num_item_sold, 
                sum(item_cost) as total_expenses, sum(item_price) as total_revenue, sum(((item_price-item_cost) * item1_q)) as total_profit
            from inventoryapp_item itm join inventoryapp_order ord on itm.id = ord.item1_id
            group by month;
            '''
    profit_month_overview_b = Profit.objects.raw(profit_query)

    return render(response, 'profitpage.html',
                  {'ProfitMonth': profit_by_month, 'ProfitItem': profit_by_item,
                   'ProfitMonthOverviewB': profit_month_overview_b})


def customerInfoPage(request):

  custInfoQuery = '''
  SELECT inventoryapp_customer.id, inventoryapp_customer.name, inventoryapp_customer.address, 
  COUNT(inventoryapp_order.customer_id_id) AS numPurchases, SUM(inventoryapp_item.item_price) AS totalSpent
  FROM inventoryapp_customer
  JOIN inventoryapp_order ON inventoryapp_customer.id = inventoryapp_order.customer_id_id
  JOIN inventoryapp_item ON inventoryapp_order.item1_id = inventoryapp_item.id
  GROUP BY customer_id_id;
  '''

  custInfo = Customer.objects.raw(custInfoQuery)


  custPurchasesQuery = '''
      SELECT inventoryapp_customer.id, inventoryapp_customer.name, inventoryapp_order.item1_id, inventoryapp_order.date
      FROM inventoryapp_customer JOIN inventoryapp_order ON inventoryapp_customer.id = inventoryapp_order.customer_id_id
      ORDER BY inventoryapp_customer.id ASC;
                    '''

  custPurch = Customer.objects.raw(custPurchasesQuery)

  return render(request, "custInfo.html", {'All_Customers': custInfo, 'CustomerPurchases': custPurch})


def customerRewards(request):

  currentRewardsQuery = ''' SELECT inventoryapp_customer.id, name, rewards_points, has_rewards
                            FROM inventoryapp_customer JOIN inventoryapp_customer_rewards
                            ON inventoryapp_customer.id = inventoryapp_customer_rewards.customer_id_id;
                        '''
  custRewards = Customer.objects.raw(currentRewardsQuery)

  return render(request, "custRewards.html", {'CustomerRewards': custRewards})