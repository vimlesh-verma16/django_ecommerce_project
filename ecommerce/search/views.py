from django.shortcuts import render

from products.models import Product
from django.views.generic import CreateView, ListView


class SearchProductView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.GET)
        method_dict = request.GET
        query = method_dict.get("q", None)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.none

    """
    __icontains = When fields contains this
    __iexact = When fields contains this 
    """
