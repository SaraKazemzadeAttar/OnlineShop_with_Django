from collections import defaultdict
from django.views.generic import TemplateView
from .models import Product, Category, Banner , UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.views.generic.base import TemplateView
from django.shortcuts import render , redirect
from .forms import UserInfoForm , UserProfileForm , CustomUserForm
from django.contrib.auth.decorators import login_required
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
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserInfoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = UserInfoForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            return render(request, 'home.html', {'data': cleaned_data})
        return render(request, self.template_name, {'form': form})

@login_required
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = CustomUserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = CustomUserForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })