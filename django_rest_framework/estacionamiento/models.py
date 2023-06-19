from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


"""
class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
"""

class Clientes(models.Model):
    dni_cliente = models.IntegerField(primary_key=True)
    numero_cliente = models.IntegerField(blank=False)
    nombre= models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=70)
    class Meta:
        db_table = 'cliente'
        verbose_name = 'clientes de estacionamiento'
        verbose_name_plural = 'clientes'
    def __unicode__(self):
        return self.nombre
    def __str__(self) :
        return self.nombre


class sector_estacionamiento(models.Model):
    idsector =models.AutoField(primary_key=True)
    descrpcion_sector= models.CharField(max_length=80)
    class Meta:
        db_table = 'sector_estacionamiento'
        verbose_name = 'sector estacionamiento'
        verbose_name_plural = 'sectores de estacionamiento'
    def __unicode__(self):
        return self.descrpcion_sector
    def __str__(self):
        return str(self.descrpcion_sector)


class Parcela(models.Model):
    idparcela =models.AutoField(primary_key=True)
    descripcion_parcela= models.CharField(max_length=60)
    idsector= models.ForeignKey(sector_estacionamiento, to_field='idsector', on_delete=models.CASCADE)
    class Meta:
        db_table = 'parcela'
        verbose_name = 'parcela estacionamiento'
        verbose_name_plural = 'parcelas'
    def __unicode__(self):
        return self.descripcion_parcela
    def __str__(self):
        return str(self.descripcion_parcela)


class Vehiculos(models.Model):
    idvehiculos=models.AutoField(primary_key=True)
    patente=models.CharField(max_length=45, blank=False)
    marca = models.CharField(max_length=45, blank=False)
    modelo = models.CharField(max_length=45, blank=False)
    dni_cliente = models.ForeignKey(Clientes, to_field='dni_cliente', on_delete=models.CASCADE)
    idparcela = models.ForeignKey(Parcela, to_field='idparcela', on_delete=models.CASCADE)
    class Meta:
        db_table = 'vehiculos'
        verbose_name = 'vehiculos estacionados'
        verbose_name_plural = 'vehiculos'
    def __unicode__(self):
        return self.patente
    def __str__(self):
        return str(self.patente)