from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('products/<int:pk>',views.ProductDetailsView.as_view(), name='details'),
    path('login',views.LoginInterfaceView.as_view(), name='login'),
path('logout',views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup',views.SignupInterfaceView.as_view(), name='signup'),
]