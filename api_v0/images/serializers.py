from rest_framework import serializers
from .models import Gallery, Images

class GallerySerialize(serializers.Serializer):
    class Meta:
        model = Gallery
        fields = [
            'id',
            'name',
            'descriptor',
            'created_at'
        ]

class ImagesSerializer(serializers.Serializer):
    class Meta:
        model = Images
        fields = [
            'id',
            'image',
            'descriptor',
            'created_at'
        ]