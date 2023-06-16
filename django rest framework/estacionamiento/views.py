from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculos.objects.all()
    serializer_class = VehiculoSerializer 

class ParcelaViewSet(viewsets.ModelViewSet):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer  

class SectorViewSet(viewsets.ModelViewSet):
    queryset = sector_estacionamiento.objects.all()
    serializer_class = SectorSerializer 