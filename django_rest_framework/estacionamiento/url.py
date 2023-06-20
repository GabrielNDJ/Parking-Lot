from django.urls import path, include
from rest_framework import routers
from estacionamiento import views
from .views import *


router=routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'vehiculo', views.VehiculoViewSet)
router.register(r'parcela', views.ParcelaViewSet)
router.register(r'sector', views.SectorViewSet)




urlpatterns =[
     path('auth/login/',
         LoginView.as_view(), name='auth_login'),

     
    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

     path('retornarPagado/',
         retornarPagado.as_view(), name='retornarPagado'),

     path('agregarCarrito/',
          agregarCliente.as_view(), name='agregarCliente'),      

     path('carrito/',
         CarritoComprasVista.as_view(), name='carritodecompras'),
         
     path('', include(router.urls))
]