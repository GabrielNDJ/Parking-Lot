from django.urls import path, include
from rest_framework import routers
from estacionamiento import views


router=routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'vehiculo', views.VehiculoViewSet)
router.register(r'parcela', views.ParcelaViewSet)
router.register(r'sector', views.SectorViewSet)


urlpatterns =[
    path('', include(router.urls))
]