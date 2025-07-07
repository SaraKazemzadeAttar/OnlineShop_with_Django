from django.shortcuts import render


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order , OrderItem
from home.models import  Product



@login_required
def order_list_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_cart.html', {'orders': orders})

