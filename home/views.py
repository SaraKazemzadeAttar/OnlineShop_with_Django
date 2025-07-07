from collections import defaultdict
from django.views.generic import TemplateView
from .models import Product, Category, Banner

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
