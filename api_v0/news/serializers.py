from rest_framework import serializers

from .models import News

class NewsSerializer(serializers.Serializer):
    Model = News
    fields = [
        'id',
        'name',
        'title',
        'subtitle',
        'text',
        'main_image',
        'gallery',
        'original_url',
        'created_at'
    ]