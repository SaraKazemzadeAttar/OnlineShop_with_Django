from collections import defaultdict
from django.views.generic import TemplateView
from .models import Product, Category, Banner
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.forms import UserCreationForm
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()
        context['categories'] = categories

        # Create a dictionary to hold products grouped by category
        category_products = {}

        for category in categories:
            category_products[category] = Product.objects.filter(category=category)

        context['category_products'] = category_products
        context['banners'] = Banner.objects.all()

        return context


class ProductDetailsView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = "product"
    login_url = '/login'

class LoginInterfaceView(LoginView):
    template_name = 'login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'

class SignupInterfaceView(TemplateView):
    form_class = UserCreationForm
    template_name = 'register.html'