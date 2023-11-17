from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
class Area(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    nombreYApellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    legajo = models.IntegerField()
    cuentaCorriente = models.DecimalField(max_digits=10, decimal_places=2)
    fechaNacimiento = models.DateField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)

    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField()
    estado = models.BooleanField()
    carrito = models.IntegerField(default=0)
    cantidad = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(stock)])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url

    @property
    def total_carrito(self):
        carrito = self.detallepedido_set.filter(pedido__estado='pendiente')
        total = sum(item.subtotal for item in carrito)
        return total

class DetallePedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Pedido(models.Model):
    estado_choices = [
        ('pendiente', 'Pendiente'),
        ('cancelado', 'Cancelado'),
        ('entregado', 'Entregado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalles = models.ManyToManyField(DetallePedido)
    fechaPedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=estado_choices, default='pendiente')
    direccionEntrega = models.CharField(max_length=255, blank=True, null=True)


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
