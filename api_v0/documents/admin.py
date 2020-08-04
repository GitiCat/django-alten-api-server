from django.contrib import admin
from .models import Document, CategoryDocuments

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_at')

@admin.register(CategoryDocuments)
class CategoryDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')