# Generated by Django 4.2.4 on 2023-12-17 02:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
                ('fechaC', models.DateTimeField(max_length=20, verbose_name='Fecha de contratacion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productoName', models.CharField(max_length=200)),
                ('productoDescription', models.CharField(blank=True, max_length=200)),
                ('productoPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productoImage', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.TextField(blank=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.client', verbose_name='Cliente ok')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.empleado', verbose_name='Empleado ok')),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('preciounit', models.FloatField()),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.BooleanField(default=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.producto', verbose_name='Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.venta', verbose_name='Nro Venta')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pago', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('transferencia', 'Transferencia')], max_length=20)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.venta')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('preciounit', models.FloatField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea.venta', verbose_name='Venta relacionada')),
            ],
            options={
                'indexes': [models.Index(fields=['venta', 'producto'], name='tarea_inven_venta_i_228e46_idx')],
            },
        ),
    ]
