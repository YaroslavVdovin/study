from django.contrib import admin
from .models import Product, Review

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display = (
        'name',
        'SKU_code',
        'description',
        'tags'
    )

@admin.register(Review)
class ProductModel(admin.ModelAdmin):
    list_display = (
        'product',
        'rev_text'
    )

# Register your models here.
