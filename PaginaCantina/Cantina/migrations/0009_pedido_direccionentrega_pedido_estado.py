# Generated by Django 4.2.4 on 2023-11-14 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cantina', '0008_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='direccionEntrega',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('cancelado', 'Cancelado'), ('entregado', 'Entregado')], default='Pendiente', max_length=20),
        ),
    ]