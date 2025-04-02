from django.shortcuts import render
from .models import Cart


def create_cart(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("New Cart Created")
    return cart_obj


def cart_home(request):
    request.session["cart_id"] = "12"
    cart_id = request.session.get("cart_id", None)
    # if cart_id is None:
    #     cart_obj = create_cart()
    #     request.session["cart_id"] = cart_obj.id  # Setter fun
    # else:
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        print("Cart ID Exist")
        cart_obj = qs.first()
    else:
        cart_obj = create_cart()
        request.session["cart_id"] = cart_obj.id

        cart_obj = Cart.objects.get(id=cart_id)
    return render(request, "carts/home.html", {})
