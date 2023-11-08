from rest_framework import viewsets, generics
from .serializer import FacultadSerializer, NomenclaturaSerializer
from .models import Facultad, Nomenclatura
from rest_framework import generics
from rest_framework import filters


class FacultadView(viewsets.ModelViewSet):
    serializer_class = FacultadSerializer
    queryset = Facultad.objects.all()


class NomenclaturaView(viewsets.ModelViewSet):
    serializer_class = NomenclaturaSerializer
    queryset = Nomenclatura.objects.all()


class NomenclaturaListView(generics.ListAPIView):
    queryset = Nomenclatura.objects.all()
    serializer_class = NomenclaturaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["plan_carrera", "nombre_carrera", "codigo_titulo"]
