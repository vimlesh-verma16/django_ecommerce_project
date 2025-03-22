from django.shortcuts import get_object_or_404, render
from .models import Product
from django.http import Http404

# Create your views here.
from django.views.generic import CreateView, ListView, DeleteView, DetailView


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get("slug")
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def product_detail_view(request, pk=None):
    instance = get_object_or_404(Product, pk=pk)
    context = {"object": instance}
    return render(request, "products/detail.html", context)
