from django.urls import path, include
from .views import LoginVista, LogoutVista, SignupView, ProfileView, ListarUsuarios, agregarCliente


path('auth/login/',
         LoginVista.as_view(), name='auth_login'),

path('auth/logout/',
         LogoutVista.as_view(), name='auth_logout'),
path('auth/reset/',
     include('django_rest_passwordreset.urls',
             namespace='password_reset')),
path('auth/registro/',
    SignupView.as_view(), name='auth_signup'),
path('user/profile/',
    ProfileView.as_view(), name='user_profile'),
path('usuarios/',
    ListarUsuarios.as_view(), name='listar_usuarios'),
path('agregarproducto/',
    agregarCliente.as_view(), name='agregar_producto'),