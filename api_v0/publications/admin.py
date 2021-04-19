from django.contrib import admin
from .models import Publication, CategoryPublication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'created_at']

@admin.register(CategoryPublication)
class CategoriesPublicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']