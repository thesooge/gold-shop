from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    address = models.CharField(max_length=1000)
    is_paid = models.BooleanField(default=False)

    order_date = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.product.title} * {self.quantity}"