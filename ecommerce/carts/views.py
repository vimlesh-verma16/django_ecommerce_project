from django.shortcuts import render


def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        print("Create new cart")
        request.session["cart_id"] = 12  # Setter fun
        pass
    else:
        print("cart already exists")

    # key = request.session.session_key
    # print(f"key : {key}")

    request.session.save()
    return render(request, "carts/home.html", {})
