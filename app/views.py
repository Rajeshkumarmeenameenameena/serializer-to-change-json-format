from django.shortcuts import render,HttpResponse,redirect
from .models import *
from rest_framework import viewsets
from .serializers import *
# Create your views here.
class studentviewset(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=studentserializer