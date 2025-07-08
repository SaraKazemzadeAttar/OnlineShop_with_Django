from django.db import models
from django.contrib.auth.models import User
from home.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    delivered = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed')
    ], default='pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    @property
    def total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # price at purchase time

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"

    @property
    def total_price(self):
        return self.price * self.quantity