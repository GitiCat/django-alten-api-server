from rest_framework import serializers

from .models import Vacancies

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vacancies
        fields = [
            'id',
            'name',
            'title',
            'subtitle',
            'descriptor',
            'is_active',
            'created_at'
        ]