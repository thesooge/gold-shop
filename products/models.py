from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models import F

import requests
# Create your models here.

def get_price_from_api():
    url = "http://api.navasan.tech/latest/?api_key=freep3Td2IxL96F6BzJ2axfrB4CdxUhs"
    response = requests.get(url)
    return (int(response.json()['18ayar']['value']))


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    amount = models.FloatField()
    description = models.TextField()
    iamge = models.ImageField(upload_to='prodcts_cover/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def get_absolute_url(self):
        return reverse("product-list", kwargs={"pk": self.pk})
    
    def get_category(self):
        return self.category.title
    
    def __str__(self):
        return self.title
    
    @property
    def unit_price(self):
        # get live price for gold
        # because of the api limit, we will use a fixed price
        try:
            return (get_price_from_api() * self.amount)
        except:
            return self.amount * 7900000


class ProductComment(models.Model):
    STATUS = (
        ('C', 'Checked'),
        ('NC', 'Not-Checked'),
    )

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=255, default='NC')

    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.product.pk})
    