from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Products, Image


# Create your views here.


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Products


class ImageView(DetailView):
    template_name = 'products/product_detail.html'
    model = Image

