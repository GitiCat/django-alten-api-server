from rest_framework import serializers
from .models import Product, CategoryProduct
from ..images.serializers import ImagesSerializer

class ProductSerializer(serializers.ModelSerializer):
    main_image = ImagesSerializer()
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'title',
            'category',
            'descriptor',
            'feature',
            'main_image',
            'file',
            'created_at'
        ]

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = [
            'id',
            'name',
            'title',
            'descriptor',
            'created_at'
        ]