from rest_framework import viewsets, permissions
from tarea.models import Producto, Client, Venta, VentaProducto,Person,Proveedor,Pago,CategoriaProducto,Compra,ItemCompra,Inventario,Factura,Empleado
from tarea.serializers import ProductoSerializer, ClientSerializer, VentaSerializer, VentaProductoSerializer,PersonSerializer,ProveedorSerializer,PagoSerializer,CategoriaProductoSerializer,CompraSerializer,ItemCompraSerializer,InventarioSerializer,FacturaSerializer,EmpleadoSerializer, UserSerializer
from rest_framework import status,views, response
from rest_framework import authentication
from django.contrib.auth.models import User
from django.contrib.auth import logout ,authenticate, login 
from rest_framework.authtoken.models import Token

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.BasicAuthentication]
    

class ClientViewSet(viewsets.ModelViewSet):
  queryset = Client.objects.all()  
  permission_classes = [permissions.AllowAny]
  serializer_class = ClientSerializer

class VentaViewSet(viewsets.ModelViewSet):
  queryset = Venta.objects.all()
  permission_classes = [permissions.IsAuthenticated]
  authentication_classes = [authentication.TokenAuthentication,]
  serializer_class = VentaSerializer

class VentaProductoViewSet(viewsets.ModelViewSet):
  queryset = VentaProducto.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = VentaProductoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagoSerializer
    
class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaProductoSerializer
    
class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CompraSerializer
    
class ItemCompraViewSet(viewsets.ModelViewSet):
    queryset = ItemCompra.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemCompraSerializer
    
class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InventarioSerializer
    
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacturaSerializer
    
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerializer
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
    authentication_classes = [authentication.BasicAuthentication,]

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        username2= request.data.get('username', None)
        password2 = request.data.get('password', None)
        if username2 is None or password2 is None:
            return response.Response({'message': 'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
        user2 = authenticate(username=username2, password=password2)
        if not user2:
            return response.Response({'message': 'Usuario o Contraseña incorrecto !!!! '},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user2)
        # Si es correcto añadimos a la request la información de sesión
        if user2:
            # para loguearse una sola vez
            # login(request, user)
            return response.Response({'message':'usuario y contraseña correctos!!!!'},status=status.HTTP_200_OK)
            #return response.Response({'token': token.key}, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return response.Response(status=status.HTTP_404_NOT_FOUND)        

class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):        
        request.user.auth_token.delete()
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return response.Response({'message':'Sessión Cerrada y Token Eliminado !!!!'},status=status.HTTP_200_OK)