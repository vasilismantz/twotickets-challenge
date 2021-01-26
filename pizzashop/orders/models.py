from django.db import models
from django.utils.translation import gettext_lazy as _


class Pizza(models.Model):

    class PizzaSize(models.TextChoices):
        SMALL = 'S', _('Small')
        MEDIUM = 'M', _('Medium')
        LARGE = 'L', _('Large')

    pizza_name = models.CharField(max_length=200)
    pizza_size = models.CharField(
        max_length=1,
        choices=PizzaSize.choices,
        default=PizzaSize.MEDIUM,
    )

    def __str__(self):
        return "%s, %s" % (self.pizza_name, self.pizza_size)


class Order(models.Model):

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)
    customer_phone = models.CharField(max_length=14)

    def __str__(self):
        return "%s, %s, %s, %s" % (self.pizza, self.customer_name, self.customer_email, self.customer_phone)
