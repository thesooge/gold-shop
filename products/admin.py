from django.contrib import admin
from .models import Product, Category, ProductComment

# Register your models here.


class ProductCommentsAdmin(admin.TabularInline):
    model = ProductComment
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductCommentsAdmin]


admin.site.register(Category)