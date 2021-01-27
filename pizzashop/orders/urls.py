from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path('', views.ordersIndex, name='index'),
    path('ordersFilter', views.ordersFilter, name="ordersFilter")
]
