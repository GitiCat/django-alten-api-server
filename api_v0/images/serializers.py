from rest_framework import serializers
from .models import Gallery, Images

class GallerySerialize(serializers.Serializer):
    class Meta:
        model = Gallery
        fields = [
            'id',
            'name',
            'descriptor',
            'head_image',
            'created_at'
        ]

class ImagesSerializer(serializers.Serializer):
    class Meta:
        model = Images
        fields = [
            'id',
            'image',
            'descriptor',
            'gallery',
            'created_at'
        ]