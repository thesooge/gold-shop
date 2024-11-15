
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_list, name='cart_list'),
    path('add/<int:pk>', views.cart_add, name='cart_add'),
    path('remove/<int:pk>', views.cart_remove, name='cart_remove'),
    
    
]
