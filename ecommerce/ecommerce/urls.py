"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from itertools import product
from django.conf import settings
from django.conf.urls.static import static

# Above fucntion is used fro serving file in STATIC_URL and MEDIA_URL

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("about/", views.about_page, name="about_page"),
    path("contact/", views.contact_page, name="contact_page"),
    path("login/", views.Login_page, name="login_page"),
    path("register/", views.Register_page, name="register_page"),
    path("old", views.home_page_old, name="home_page_old"),
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
