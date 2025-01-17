
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_list, name='cart_list'),
    path('add/<int:product_id>', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('clear-cart/', views.clear_cart, name='cart_clear'),
    
    
]
