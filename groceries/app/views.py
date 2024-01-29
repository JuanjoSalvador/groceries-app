from django.shortcuts import render
from django.db.models import Q

from .models import Product


def index(request):
    return render(request, "index.html")

def search(request):
    query = request.GET['q']
    queryset = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )

    values = {"search": query, "queryset": queryset}

    return render(request, "search.html", values)

def product_view(request, pk=None):
    queryset = Product.objects.get(pk=pk)
    context = {"product": queryset}

    return render(request, "product.html", context)
