from django.shortcuts import render

from .models import Pizza, PizzaType, Order

# Get pizzas and dislay them


def index(request):
    pizzas = PizzaType.objects.all()
    context = {'pizzas': pizzas}
    return render(request, "orders/index.html", context)

