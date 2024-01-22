from django.shortcuts import render

from .models import Product


def index(request):
    return render(request, "index.html")

def search(request):
    query = request.POST['searchbar']
    queryset = Product.objects.filter(name__contains=query)

    values = {"search": query, "queryset": queryset}

    return render(request, "search.html", values)

def product_view(request, pk=None):
    queryset = Product.objects.get(pk=pk)
    context = {"product": queryset}

    return render(request, "product.html", context)
