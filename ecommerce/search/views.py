from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class SearchProductView(ListView):
    template_name = "search/view.html"  # Ensure the correct template path

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get("q")  # Fixed typo (Get → GET)
        context["query"] = query
        # SearchQuery.objects.create(query=query)  # Uncomment if using SearchQuery model
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get("q", None)  # More concise way of getting the query
        print(query)
        if query:
            return Product.objects.search(query)
        return (
            Product.objects.none()
        )  # Fixed: Previously calling .featured(), which doesn't exist
