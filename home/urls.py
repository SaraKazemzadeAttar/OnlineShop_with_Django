from django.urls import path
from . import views
from .views import HomeView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('products/<int:pk>',views.ProductDetailsView.as_view(), name='details'),
    path('login',views.LoginInterfaceView.as_view(), name='login'),
path('logout',views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup',views.SignupInterfaceView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/change-password/', auth_views.PasswordChangeView.as_view(
        template_name='profile_password.html',
        success_url='/profile/'
    ), name='change_password'),
]