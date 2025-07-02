from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

class BannerView(TemplateView):
    template_name = 'home/banner_swipper.html'

class CategoryView(TemplateView):
    template_name = 'home/category.html'

class ProductsView(TemplateView):
    template_name = 'home/product.html'