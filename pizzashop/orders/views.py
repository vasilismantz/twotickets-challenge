from django.shortcuts import render
import logging

from .models import Pizza, PizzaType, Order

logger = logging.getLogger(__name__)

# Get pizzas and dislay them


def index(request):
    pizzas = PizzaType.objects.all()

    for pizza in pizzas:
        pizza.sizes = Pizza.objects.filter(pizza__pizza_type=pizza).values('pizza_size')

    context = {'pizzas': pizzas}
    return render(request, "index.html", context)

def completeForm(request):
    if request.method == "POST":
        pizza = request.POST["pizza_name"]
        size = request.POST["pizza_size"]

        pizzaInstance = Pizza.objects.filter(pizza__pizza_type=pizza, pizza_size=size).values_list("id", flat=True)

        for p in pizzaInstance:
            id = p

        context = {
            "pizza": pizza,
            "size" : size,
            "id" : id
        }

        return render(request, "completeForm.html", context)

def result(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]


        pizza = Pizza.objects.get(pk=id)

        pizza.order_set.create(customer_name=name, customer_email=email, customer_phone=phone)

        context = {
            "result": "success"
        }

        return render(request, "result.html", context)

def ordersIndex(request):
    orders = Order.objects.all()

    context = {
        "orders": orders
    }

    return render(request, "orders/ordersIndex.html", context)

def ordersFilter(request):
    if request.method == "POST":
        search = request.POST["search"]
        field = request.POST["field"]

        if field == "name":
            orders = Order.objects.filter(customer_name=search)
        elif field == "email":
            orders = Order.objects.filter(customer_email=search)

        context = {
            "orders": orders
        }

        return render(request, "orders/ordersFilter.html", context)