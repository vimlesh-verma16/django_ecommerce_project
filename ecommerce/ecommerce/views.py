import re
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Home Page -> from home.html",
        "content": "Welcome to home page",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAHhhhhhhh!"
    return render(request, "home.html", context)


def about_page(request):
    context = {
        "title": "about Page -> from home.html",
        "content": "Welcome to about page",
    }
    return render(request, "home.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page -> from view.html",
        "content": "Welcome to contact page",
        "form": contact_form,
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    return render(request, "contact/view.html", context)


def Login_page(request):
    form = LoginForm(request.POST or None)
    print(
        "üser logged in :", request.user.is_authenticated
    )  # to check if user is logged in or not
    context = {
        "form": form,
    }
    if form.is_valid():
        print("üser logged in :", request.user.is_authenticated)
        print(form.cleaned_data)  # cleaned_data is a dictionary
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Here we are attaching the user to the request
            print("üser logged in :", request.user.is_authenticated)
            form = LoginForm()
            # context["form"] = LoginForm()  # to clear the form after submit
            print("Ërror some thing is wrong")
            return redirect("/login")  # Goes to same page
    return render(request, "auth/login.html", context)


User = get_user_model()


def Register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        print("Post Data:", form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        User.objects.create_user(username, email, password)

    return render(request, "auth/register.html", context)


def home_page_old(request):
    html_ = """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
      </head>
      <body>
        <div class='text-center'>
            <h1>Hello, world old home Page!</h1>
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
      </body>
    </html>
    """
    return HttpResponse(html_)
