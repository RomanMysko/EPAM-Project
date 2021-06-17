from django.shortcuts import render

# Create your views here.
from .models import Reservation, Price, Order


def order_addition(orders, key, value, a):
    """
    function checks if there's already an object we want to make relation with.
    if there is we make relation with the existing object else create a new object
    Parameters:
        orders (dict):dict of Order objects in database
        key(str):name of dish
        value(str):quantity of dishes
        a(Reservation):Reservation object we make relations with
    """
    tmp = 0
    for order_el in orders:
        if key == order_el.dish and int(value) == order_el.quantity:
            a.orders.add(order_el)
            tmp = 1
            break
    if tmp == 0:
        my_order = Order(dish=key, quantity=value)
        my_order.save()
        a.orders.add(my_order)


def index(request):
    """
    Creates Reservation object with relation to multiple Order objects and counting
    total price of the Reservation.
    """
    if request.method == 'POST':
        mydate = request.POST.get('dat')
        mytime = request.POST.get('tim')
        myparty = request.POST.get('party')
        myname = request.POST.get('name')
        myemail = request.POST.get('email')
        myphone = request.POST.get('phone')
        orders = Order.objects.all()
        prices = Price.objects.all()
        total = 0
        temp = 0
        a = Reservation(date=mydate, email=myemail, time=mytime, party=myparty, name=myname, phone=myphone,
                        total_price=0)
        a.save()
        for key, value in request.POST.items():
            if key == "phone":
                temp = 1
                continue
            if temp == 0:
                continue
            if int(value) != 0:
                for el in prices:
                    if key == el.dish:
                        total += float(el.price) * float(value)
                        order_addition(orders, key, value, a)
        a.total_price = total
        a.save()
    return render(request, 'mysite/index.html')
