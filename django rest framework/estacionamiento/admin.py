from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

"""
@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass
"""
    
#admin.site.register(CustomUser)
admin.site.register(Clientes)
admin.site.register(Vehiculos)
admin.site.register(Parcela)
admin.site.register(sector_estacionamiento)
