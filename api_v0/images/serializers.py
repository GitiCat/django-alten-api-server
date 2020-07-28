from rest_framework import serializers
from .models import Gallery, Images

class GallerySerialize(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = [
            'id',
            'name',
            'descriptor',
            'head_image',
            'created_at'
        ]

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = [
            'id',
            'image',
            'descriptor',
            'gallery',
            'created_at'
        ]