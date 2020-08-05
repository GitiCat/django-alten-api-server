from django.contrib import admin
from .models import Product, CategoryProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_at')

@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')