from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView


# Create your views here.

class CartDetailView(View):
    def get(self, request):
        return render(request, 'carts/cart_detail.html', {})


class CartAddView(View):
    def post(self, request, pk):
        size, color = request.POST.get('size'), request.POST.get('color')
        print(size, color)
        return redirect('cart:cart_detail')
