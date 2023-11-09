from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

class Cliente(models.Model):
    nombreYApellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
    dni = models.IntegerField()
    legajo = models.IntegerField()
    cuentaCorriente = models.DecimalField(max_digits=10, decimal_places=2)  # Usar DecimalField para cuentas corrientes
    fechaNacimiento = models.DateField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    estado = models.BooleanField()

class DetallePedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalles = models.ManyToManyField(DetallePedido)
    fechaPedido = models.DateTimeField(auto_now_add=True)

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el modelo User de Django
    # Agrega campos adicionales para el perfil del administrador si es necesario

class CuentaCorriente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros campos relacionados con la cuenta corriente

class InformeCuentasCorrientes(models.Model):
    emisor = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    # Otros campos relacionados con el informe
