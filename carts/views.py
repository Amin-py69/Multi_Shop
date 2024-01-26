from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from products.models import Products
from .models import Order, OrderItem, DiscountCode
from .cart_moduls import Cart
from django.views.generic import DetailView
from .forms import AddressCreationForm
from django.contrib.messages.api import *  # NOQA
from django.contrib.messages.constants import *  # NOQA


# Create your views here.

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'carts/cart_detail.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Products, id=pk)
        size, color, quantity = request.POST.get('size', 'empty'), request.POST.get('color', 'empty'), request.POST.get(
            'quantity')
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        return redirect('cart:cart_detail')


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart_detail')


class AddAddressView(View):
    def get(self, request):
        form = AddressCreationForm()
        return render(request, 'carts/add_address.html', {'form': form})

    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)

            if len(address.user) > 3:
                del AddAddressView[4:]
        return render(request, 'carts/add_address.html', {'form': form})


class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, 'carts/order_detail.html', {'order': order})


class OrderCreationView(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'],
                                     quantity=item['quantity'], price=item['price'])
        cart.remove_cart()
        return redirect('cart:order_detail', order.user.id)


class ApplyDiscountView(View):
    def post(self, request, pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order, id=pk)
        discount_code = get_object_or_404(DiscountCode, name=code)
        if discount_code.quantity == 0:
            # raise add_message(request,discount_code, 'your code is timeout or not true')
            return redirect('cart:order_detail', order.id)
        order.total_price -= order.total_price * discount_code.discount_code/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect('cart:order_detail', order.id)
