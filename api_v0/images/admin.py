from django.contrib import admin
from .models import Gallery, Images

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'descriptor')