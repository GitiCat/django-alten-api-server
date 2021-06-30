from django.contrib import admin
from .models import Document, CategoryDocuments

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')

@admin.register(CategoryDocuments)
class CategoryDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'root_category', 'created_at')