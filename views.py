from django.shortcuts import render
from inventoryapp.models import Item, Inventory, Customer, Customer_rewards, Employee, Employee_bonus, Order, Profit
from .forms import OrderForm
from django.db.models import Avg, Max, Min, Sum, Count
from django.http import HttpResponse


# Create your views here.
def order_form(request):
  if request.method == "POST":
    form = OrderForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = OrderForm()

  return render(request, 'order.html', {'form': form})



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
  

