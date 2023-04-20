
from .models import *
from rest_framework import serializers

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'
        