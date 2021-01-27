from django.shortcuts import render
import logging

from .models import Pizza, PizzaType, Order

logger = logging.getLogger(__name__)

# Get pizzas and dislay them


def index(request):
    pizzas = PizzaType.objects.all()

    for pizza in pizzas:
        pizza.sizes = Pizza.objects.filter(pizza__pizza_type=pizza).values('pizza_size')
        logger.info(pizza.id)
        logger.info(pizza)
        logger.info(pizza.sizes)

    logger.info(pizzas)

    context = {'pizzas': pizzas}
    return render(request, "orders/index.html", context)

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

        return render(request, "orders/completeForm.html", context)

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

        return render(request, "orders/result.html", context)
