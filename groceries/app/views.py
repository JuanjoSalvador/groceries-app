from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def product_view(request, pk=None):
    return render(request, "product.html")
