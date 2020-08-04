from django.contrib import admin

from .models import File, ListFiles

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'list_files', 'created_at')

@admin.register(ListFiles)
class ListFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')