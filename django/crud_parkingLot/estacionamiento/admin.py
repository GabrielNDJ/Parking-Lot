from django.contrib import admin
from .models import clientes, vehiculos


# Register your models here.

class clienteAdmin(admin.ModelAdmin):
    list_display = ('dni_cliente', 'numero_cliente', 'nombre', 'apellido', 'telefono', 'email')

class vehiculosAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'modelo', 'dni_cliente')

admin.site.register(clientes, clienteAdmin)
admin.site.register(vehiculos, vehiculosAdmin)    