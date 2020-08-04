from rest_framework import serializers

from .models import File, ListFiles

class ListFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListFiles
        fields = [
            'id',
            'name',
            'descriptor',
            'created_at'
        ]

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'id',
            'file',
            'descriptor',
            'list_files',
            'created_at'
        ]