from rest_framework import serializers
from .models import Personnel, Department

class PersonnelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = [
            'id',
            'name',
            'position',
            'department',
            'phone',
            'created_at'
        ]

class DepartmentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id',
            'name',
            'descriptor',
            'created_at'
        ]