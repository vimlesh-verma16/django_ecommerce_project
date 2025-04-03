from django.db import models
from django.conf import settings

from products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            print("Cart ID exists")
            cart_obj = qs.first()
            new_obj = False
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            new_obj = True
            cart_obj = self.new(user=request.user)
            request.session["cart_id"] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_object = user_obj
        return self.model.objects.create(user=user_obj)


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return f"Cart {self.id} - {self.user.username if self.user else 'Guest'}"


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    # print(action)
    # print(instance.total)
    # print(instance.products.all())
    if action == "post_add" or action == "post_clear" or action == "post_remove":
        products = instance.products.all()
        total = 0
        for product in products:
            total += product.price
        # print(total)
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, action, *args, **kwargs):
    instance.total = instance.subtotal


pre_save.connect(pre_save_cart_receiver, sender=Cart)
