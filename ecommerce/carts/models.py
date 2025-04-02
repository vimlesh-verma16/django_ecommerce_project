from django.db import models
from django.conf import settings

from products.models import Product

User = settings.AUTH_USER_MODEL


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} - {self.user.username if self.user else 'Guest'}"
