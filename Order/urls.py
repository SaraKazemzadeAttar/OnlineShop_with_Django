from django.urls import path
from . import views

urlpatterns = [
path('cart/',views.order_list_view, name='cart'),

]