from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from products.models import Products
from .cart_moduls import Cart
from django.views.generic import DetailView


# Create your views here.

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'carts/cart_detail.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Products, id=pk)
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        return redirect('cart:cart_detail')
