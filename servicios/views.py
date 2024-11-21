from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class aprendiz_viewset(viewsets.ModelViewSet):
    queryset = Aprendiz.objects.all() # SELECT * FROM aprendiz;
    serializer_class = aprendiz_serializer

class ciudad_viewset(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = ciudad_serializer

class rol_viewset(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = rol_serializer