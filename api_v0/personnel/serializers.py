from rest_framework import serializers
from .models import Personnel, Department, CommunicationMethod

class CommunicationMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationMethod
        fields = [
            'id',
            'is_visible',
            'name',
            'descriptor',
            'responsible',
            'position',
            'phone',
            'is_phone_visible',
            'fax',
            'is_fax_visible',
            'email',
            'is_email_visible',
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

class PersonnelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = [
            'id',
            'name',
            'position',
            'department',
            'communication_method',
            'phone',
            'is_phone_visible',
            'email',
            'is_email_visible',
            'created_at'
        ]