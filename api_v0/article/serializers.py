from rest_framework import serializers
from .models import Article, CategoryArticle

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'name',
            'title',
            'subtitle',
            'category',
            'text',
            'created_at'
        ]

class CategoryArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryArticle
        fields = [
            'id',
            'name',
            'descriptor',
            'created_at'
        ]