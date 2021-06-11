from rest_framework import serializers

from .models import Vacancies, Employment

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vacancies
        fields = '__all__'

class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'