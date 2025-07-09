from django.urls import path
from . import views

urlpatterns = [
path('cart/',views.order_list_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('finalize-order/', views.finalize_order, name='finalize_order'),
    path('order-complete/<int:order_id>/', views.order_complete_view, name='order_complete'),
    path('prev', views.PrevView.as_view(), name='previous_orders'),
]