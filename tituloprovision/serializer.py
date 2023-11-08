from rest_framework import serializers
from .models import Facultad, Nomenclatura

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = "__all__"

class NomenclaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclatura
        fields = "__all__"