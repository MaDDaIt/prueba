from django.db import models
import datetime
# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    direccion=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
 
class Producto(models.Model):
    productoName = models.CharField(max_length=200)
    productoDescription = models.CharField(blank=True, max_length=200)
    productoPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productoImage = models.ImageField(null=True, blank=True, upload_to='images/')
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    def __str__ (self):
        return self.productoName
 
class ItemCompra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    preciounit = models.FloatField()

    def __str__(self):
        return f'{self.cantidad} x {self.producto.productoName}'
    
class Compra(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    items_compra = models.ManyToManyField(ItemCompra)
    
    def __str__(self):
        return f'Compra {self.id} - Proveedor: {self.proveedor}'   
    
    def procesar_compra(self):
        # Lógica de procesamiento de la compra
        nueva_compra = Compra.objects.create()

        # Asociar productos a la nueva compra
        for item_compra in self.items_compra.all():
            nuevo_item = ItemCompra.objects.create(
                compra=nueva_compra,
                producto=item_compra.producto,
                cantidad=item_compra.cantidad,
                preciounit=item_compra.preciounit,
            )

            # Actualizar el inventario
            nuevo_item.actualizar_inventario()
            
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre
    

class Person(models.Model):
    nombre = models.CharField('Nombre', max_length = 100)
    apellido = models.CharField('Apellido', max_length = 200)
    telefono= models.CharField('Telefono',max_length=9)
    foto = models.ImageField(null=True, blank=True, upload_to='fotos/')
    class Meta:
        abstract = True

class Client(Person):
    email = models.EmailField(blank=True)

    def __str__(self):
        return '{0},{1}'.format(self.apellido,self.nombre)
    
class  Empleado(Person):
    cargo= models.CharField('Cargo',max_length=100)
    fechaC = models.DateField('Fecha de contratacion',max_length=20)
    
    def __str__(self):
        return '{0},{1}'.format(self.apellido,self.nombre)

class Venta(models.Model) :
    client = models.ForeignKey(Client,on_delete=models.CASCADE, verbose_name='Cliente ok', null=False)
    empleado= models.ForeignKey(Empleado,on_delete=models.CASCADE, verbose_name='Empleado ok',null=False)
    fecha = models.DateTimeField(default=datetime.datetime.now)
    description = models.TextField(blank = True)
    def __str__ (self):
         return '{0}'.format(self.id)


class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name='Nro Venta', null=False)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE, verbose_name='Producto', null=False)
    cantidad = models.PositiveIntegerField(default=0)
    preciounit = models.FloatField()
    modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default = True)
    def __str__(self):
        return f'{self.venta} to {self.producto}'

class Pago(models.Model):
    METODO_EFECTIVO = 'efectivo'
    METODO_TARJETA = 'tarjeta'
    METODO_TRANSFERENCIA = 'transferencia'

    METODO_PAGO_CHOICES = [
        (METODO_EFECTIVO, 'Efectivo'),
        (METODO_TARJETA, 'Tarjeta'),
        (METODO_TRANSFERENCIA, 'Transferencia'),
    ]

    fecha = models.DateTimeField(default=datetime.datetime.now)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES)

    def __str__(self):
        return f'Pago {self.id} - Venta: {self.venta}, Monto: {self.monto}, Método: {self.metodo_pago}'
    
class Factura(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

    def __str__(self):
        return f'Factura {self.id} - Venta: {self.venta}'
      
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Inventario - Producto: {self.producto}, Stock: {self.stock}'
    
    class Meta:
        indexes = [
                models.Index(fields=['venta', 'producto',])]