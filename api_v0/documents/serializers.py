from rest_framework import serializers
from .models import Document, CategoryDocuments
from ..files.serializers import FileSerializer

class DocumentSerializer(serializers.ModelSerializer):
    file = FileSerializer()

    class Meta:
        model = Document
        fields = [
            'id',
            'name',
            'title',
            'subtitle',
            'text',
            'file',
            'created_at'
        ]

class CategoryDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDocuments
        fields = '__all__'