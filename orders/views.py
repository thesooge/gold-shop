from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic


from .models import Order
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
        order_form = OrderForm()
        return redirect("order-list")
    

    
    return render(request, 'orders/order_create.html', {'form' : order_form, })
       
class OrderList(generic.ListView):
    model = Order
    template_name = "orders/order_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.all()
        return context


class OrderDelete(generic.DeleteView):
    model = Order
    success_url ="/"
    def post(self, request, *args, **kwargs):
        messages.info(request, "Order Deleted Successfully")
        return super().post(request, *args, **kwargs)
    

class OrderUpdate(generic.UpdateView):
    model = Order
    template_name = "orders/order_create.html"  
    fields = ["first_name", "last_name", "email", "address"] 
