from django.shortcuts import render


def cart_home(request):
    # key = request.session.session_key
    # print(f"key : {key}")
    request.session["cart_id"] = 12  # Setter fun
    request.session.save()
    return render(request, "carts/home.html", {})
