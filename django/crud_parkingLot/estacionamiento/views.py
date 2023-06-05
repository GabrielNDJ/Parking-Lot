from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import vehiculos, clientes, CustomUser
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import clienteSerializer
from .serializers import vehiculoSerializer
from rest_framework import viewsets

# Create your views here.

class LoginVista(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        email = request.data.get('email', None)
        contraseña = request.data.get('contraseña', None)
        user = authenticate(email=email, contraseña=contraseña)
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        return Response(
            status=status.HTTP_404_NOT_FOUND)
    

    


class LogoutVista(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

class verPantentes(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny] 
    queryset = vehiculos.objects.all()
    serializer_class = vehiculoSerializer

class verCategorias(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = clientes.objects.all()
    serializer_class = clienteSerializer

class añadirProducto(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        serializer = clienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated] 
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
class ListarUsuarios(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response(serializer.data)
