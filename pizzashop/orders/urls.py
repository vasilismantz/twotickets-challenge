from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path('', views.index, name='index'),
    path('complete_form', views.completeForm, name="complete-form"),
    path('result', views.result, name="result")
]
