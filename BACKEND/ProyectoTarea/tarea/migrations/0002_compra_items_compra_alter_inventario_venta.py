# Generated by Django 4.2.4 on 2023-12-17 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='items_compra',
            field=models.ManyToManyField(to='tarea.itemcompra'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='venta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tarea.venta'),
        ),
    ]
