from django.contrib import admin

from .models import Article, CategoryArticle

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')

@admin.register(CategoryArticle)
class CategoryArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')