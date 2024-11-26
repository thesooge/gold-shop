from django.shortcuts import render, redirect
from django.contrib import messages



from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem

# Create your views here.

def order_create(request):
    cart = Cart(request)
    order_form = OrderForm()

    if len(cart) == 0:
        messages.warning(request, "Your Cart Is Empty, Add Item To Cart.")
        return redirect('product-list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

        for item in cart:
            product = item['product_obj']
            OrderItem.objects.create(
                order = order_obj,
                product = product,
                quantity = item['quantity'],
                price = product.unit_price,
            )
        
        cart.clear()
        messages.info(request, "Your order craeted succesfully")
    
    return render(request, 'orders/order_create.html', {'form' : order_form, })
       

