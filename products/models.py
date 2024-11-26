from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    unit_price = models.PositiveIntegerField()
    description = models.TextField()
    iamge = models.ImageField(upload_to='prodcts_cover/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def get_absolute_url(self):
        return reverse("product-list", kwargs={"pk": self.pk})
    
    def get_category(self):
        return self.category.title
    



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
    