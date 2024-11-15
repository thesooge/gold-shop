from django.shortcuts import render, get_object_or_404, reverse, redirect

from .cart import Cart
from .forms import AddToCartForm
from products.models import Product

# Create your views here.

def cart_list(request):
    cart = Cart(request)

    return render(request, 'cart/cart_list.html', {'cart': cart,})


def cart_add(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        quantity = data['quantity']
        cart.add(product, quantity)
    
    return redirect('cart_list')

def cart_remove(request, product_id):
    cart = Cart(request)
    cart.delete(product_id)
    return redirect('cart_list')

