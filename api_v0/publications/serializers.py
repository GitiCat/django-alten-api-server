from rest_framework import serializers
from .models import Publication
from ..images.serializers import ImagesSerializer

class PublicationSerializer(serializers.ModelSerializer):
    main_image = ImagesSerializer()

    class Meta:
        model = Publication
        fields = [
            'id',
            'name',
            'title',
            'subtitle',
            'descriptor',
            'main_image',
            'url',
            'is_active'
        ]