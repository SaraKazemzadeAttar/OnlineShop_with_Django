from django.urls import path
from . import views

urlpatterns = [
    path('banner', views.BannerView.as_view(), name='banner'),
    path('categories', views.CategoryView.as_view(), name='categories'),
    path('products', views.ProductsView.as_view(), name='products'),
]