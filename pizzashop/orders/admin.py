from django.contrib import admin

from .models import PizzaType, Pizza, Order

admin.site.site_header = "Pizza Shop Admin"
admin.site.site_title = "Pizza Shop Admin Area"
admin.site.index_title = "Welcome to the Pizza Shop admin area"

admin.site.register(PizzaType)
admin.site.register(Pizza)
admin.site.register(Order)
