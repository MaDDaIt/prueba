from django.contrib import admin
from tarea.models import Producto,Client,Venta,VentaProducto,Empleado,Compra,CategoriaProducto,ItemCompra,Proveedor,Pago,Factura,Inventario
# Register your models here.

admin.site.register(Producto)
admin.site.register(Client)
admin.site.register(Venta)
admin.site.register(VentaProducto)
admin.site.register(Empleado)
admin.site.register(Compra)
admin.site.register(CategoriaProducto)
admin.site.register(ItemCompra)
admin.site.register(Proveedor)
admin.site.register(Pago)
admin.site.register(Factura)
admin.site.register(Inventario)