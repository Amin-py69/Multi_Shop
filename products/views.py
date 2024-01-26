from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, TemplateView, ListView
from .models import Products, Image, Category


# Create your views here.


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Products


class ImageView(DetailView):
    template_name = 'products/product_detail.html'
    model = Image


class NavbarPartialView(TemplateView):
    template_name = 'includes/navbar.html'

    def get_context_data(self, **kwargs):
        context = super(NavbarPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class CategoryStyleView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryStyleView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductListView(ListView):
    template_name = 'products/products_list.html'
    queryset = Products.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        request = self.request
        color = request.GET.getlist('color')
        size = request.GET.getlist('size')
        min_price = request.GET.get('price_min')
        max_price = request.GET.get('price_max')
        queryset = Products.objects.all()
        if color:
            queryset = queryset.filter(color__title__in=color).distinct()

        if size:
            queryset = queryset.filter(size__title__in=size).distinct()

        if min_price and max_price:
            queryset = queryset.filter(price__lte=max_price, price__gte=min_price)
        context = super(ProductListView, self).get_context_data()
        context['products'] = queryset
        return context
