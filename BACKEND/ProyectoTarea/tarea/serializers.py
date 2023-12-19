from rest_framework import serializers
from tarea.models import Producto, Client, Venta, VentaProducto, Person,Proveedor,Pago,CategoriaProducto,Compra,ItemCompra,Inventario,Factura,Empleado
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        read_only_fields = ('created_at',)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'
        extra_kwargs = {
            'fecha': {'read_only': True, 'required': False},
            # 'fecha': {'read_only': True},
        }        
class VentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaProducto
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proveedor
        fields = '__all__'
        
class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'
        
class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= CategoriaProducto
        fields= '__all__'
        
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model= Compra
        fields='__all__'
        
class ItemCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model= ItemCompra
        fields= '__all__'
        
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields= '__all__'
        
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
        
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Empleado
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email']
         #esconder password
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user