from django.shortcuts import render
from rest_framework import viewsets, status, generics
from django.contrib.auth import authenticate, login, logout 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
import mercadopago
import json
from .serializer import *
from .models import *
# Create your views here.


class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)
    
class LogoutView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)  
    
class agregarCliente(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        serializer = dueñosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class verProductos(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny] 
    queryset = Vehiculos.objects.all()
    serializer_class = dueñosSerializer    
    
class CarritoComprasVista(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CarritoCompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"estado": "correcto", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"estado": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ProcessPaymentAPIView(APIView):
    def post(self, request):
        try:
            request_values = json.loads(request.body)
            payment_data = {
                "transaction_amount": float(request_values["transaction_amount"]),
                "token": request_values["token"],
                "installments": int(request_values["installments"]),
                "payment_method_id": request_values["payment_method_id"],
                "issuer_id": request_values["issuer_id"],
                "payer": {
                    "email": request_values["payer"]["email"],
                    "identification": {
                        "type": request_values["payer"]["identification"]["type"],
                        "number": request_values["payer"]["identification"]["number"],
                    },
                },
            }

            sdk = mercadopago.SDK("")

            payment_response = sdk.payment().create(payment_data)

            payment = payment_response["response"]
            status = {
                "id": payment["id"],
                "status": payment["status"],
                "status_detail": payment["status_detail"],
            }

            return Response(data={"body": status, "statusCode": payment_response["status"]}, status=201)
        except Exception as e:
            return Response(data={"body": payment_response}, status=400)

class retornarPagado(APIView):   
    def get(self, request):
        return Response({"respuesta": "aprobado"})    

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer      

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculos.objects.all()
    serializer_class = VehiculoSerializer 

class ParcelaViewSet(viewsets.ModelViewSet):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer  

class SectorViewSet(viewsets.ModelViewSet):
    queryset = sector_estacionamiento.objects.all()
    serializer_class = SectorSerializer 