from django.db import models

# Create your models here.

#tabla clientes

class clientes(models.Model):
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
    
#clase Vehiculos

class vehiculos(models.Model):
    idvehiculos= models.AutoField(primary_key=True)
    patente = models.CharField(max_length=30)
    marca = models.CharField(max_length=45, blank=False)
    modelo = models.CharField(max_length=45, blank=False)
    dni_cliente = models.ForeignKey(clientes, to_field='dni_cliente', on_delete=models.CASCADE)
    class Meta:
        db_table = 'vehiculos'
        verbose_name = 'vehicuñlos estacionados'
        verbose_name_plural = 'vehiculos'
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre