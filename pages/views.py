from django.shortcuts import render, redirect
from orders.models import Order
from .forms import UserEditForm

# Create your views here.


def home_page(request):
    return render(request, 'pages/homepage.html')

def profile(requset):
    orders = Order.objects.all()
    return render(requset, "pages/profile.html", {"orders" : orders})

def edit_user_profile(request):
    user = request.user
    form = UserEditForm(request.POST or None, instance=user)
    
    if form.is_valid():
        form.save()
        return redirect('profile') 

    return render(request, 'pages/edit_user_profile.html', {'form': form})
