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
         
    path('', include(router.urls))
]