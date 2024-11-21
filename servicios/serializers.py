from rest_framework import serializers
from .models import *

class aprendiz_serializer(serializers.ModelSerializer):
    class Meta:
        model = Aprendiz 
        fields = ['id','nombre', 'edad', 'vivo', 'foto', 'ciudad', 'rol']

class ciudad_serializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad 
        fields = ['nombre']

class rol_serializer(serializers.ModelSerializer):
    class Meta:
        model = Rol 
        fields = ['nombre']