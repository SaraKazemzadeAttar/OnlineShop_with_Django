from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Banner(models.Model):
    image = models.ImageField()
    description = models.TextField()

    # Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()