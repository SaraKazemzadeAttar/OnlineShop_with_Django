from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    seller_name = models.CharField(max_length=100)
    image_right = models.ImageField(upload_to='products/right/' , blank=True , null=True)
    image_left = models.ImageField(upload_to='products/left/' , blank=True , null=True)
    image_center = models.ImageField(upload_to='products/center/', blank=True , null=True)

    def __str__(self):
        return self.name


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Banner {self.id}"