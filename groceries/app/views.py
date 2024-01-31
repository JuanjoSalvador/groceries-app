from typing import Any

from django.db.models import Q
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView, DetailView

from .models import Product


class IndexView(TemplateView):
    template_name = "index.html"


class SearchView(ListView):
    model = Product
    template_name = "search.html"

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get("q")
        return Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(SearchView, self).get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        context["search_results"] = self.get_queryset()

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.filter(pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["product"] = self.get_queryset().first()

        return context
