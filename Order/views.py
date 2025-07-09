from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Order, OrderItem
from .forms import AddToCartForm , FinalizeOrderForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            order, created = Order.objects.get_or_create(
                user=request.user,
                delivered=False,
                payment_status='pending',
            )

            item, created = OrderItem.objects.get_or_create(
                order=order,
                product=product,
                defaults={'quantity': quantity, 'price': product.price}
            )
            if not created:
                item.quantity += quantity
                item.save()

            return redirect('cart')

    else:
        form = AddToCartForm(initial={'product_id': product_id})

    return render(request, 'buy_product.html', {'form': form, 'product': product})

@login_required
def order_complete_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == 'POST':
        order.payment_status = 'paid'
        order.save()
        return render(request, 'payment_success.html', {'order': order})


    return render(request, 'pay.html', {'order': order})

@login_required
def order_list_view(request):
    all_orders = Order.objects.filter(user=request.user).order_by('-created_at')
    paid_orders = Order.objects.filter(
        user=request.user,
        payment_status='paid'
    ).order_by('-created_at')

    pending_order = Order.objects.filter(
        user=request.user,
        payment_status='pending',
        delivered=False,
        items__isnull=False
    ).order_by('-created_at').first()

    failed_orders = all_orders.filter(payment_status='failed')


    return render(request, 'order_cart.html', {
        'paid_orders': paid_orders,
        'pending_order': pending_order,
        'failed_orders': failed_orders,
    })
@login_required
def finalize_order(request):
    try:
        order = Order.objects.get(user=request.user, delivered=False, payment_status='pending')
    except Order.DoesNotExist:
        return redirect('cart')

    if request.method == 'POST':
        form = FinalizeOrderForm(request.POST)
        if form.is_valid():
            order.address = form.cleaned_data['address']
            order.save()
            return redirect('order_complete', order_id=order.id)

    else:
        form = FinalizeOrderForm(initial={'address': order.address})

    return render(request, 'finalize_order.html', {'form': form, 'order': order})


class PrevView(LoginRequiredMixin, TemplateView):
    template_name = 'last_orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paid_orders'] = Order.objects.filter(
            user=self.request.user,
            payment_status='paid'
        ).order_by('-created_at')
        return context