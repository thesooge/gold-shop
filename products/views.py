from django.shortcuts import render
from django.views import generic

from .models import Product, ProductComment, Category
# Create your views here.

class ProductList(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'