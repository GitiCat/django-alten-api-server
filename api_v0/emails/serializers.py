from rest_framework import serializers
from .models import EmailModel

class EmailSerializer(serializers.ModelSerializer):
    Model = EmailModel,
    fields = [
        'id',
        'full_name',
        'email',
        'phone',
        'message',
    ]