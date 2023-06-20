from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import models
from .models import *

class CarritoCompraSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(max_length=200)
    producto_precio = serializers.FloatField()
    producto_cantidad = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CarritoCompras
        fields = ('__all__')

class dueñosSerializer(serializers.ModelSerializer):
    id_categoria = serializers.SlugRelatedField(
        queryset=Clientes.objects.all(), slug_field="nombre"
    )

    class Meta:
        model = Vehiculos
        fields = '__all__'
                

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
    def validate_password(self, value):
        return make_password(value)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = '__all__'

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sector_estacionamiento
        fields = '__all__'
        