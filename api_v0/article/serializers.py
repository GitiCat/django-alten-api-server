from rest_framework.parsers import JSONParser
from rest_framework import serializers
from .models import Article, CategoryArticle
from ..images.serializers import ImagesSerializer

class ArticleSerializer(serializers.ModelSerializer):
    main_image = ImagesSerializer()
    
    class Meta:
        model = Article
        fields = [
            'id',
            'name',
            'title',
            'subtitle',
            'text',
            'main_image',
            'created_at'
        ]

class CategoryArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryArticle
        fields = [
            'id',
            'name',
            'title',
            'descriptor',
            'created_at'
        ]