from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClienteForm
from .forms import UserCreationFormExtended
from .models import *
from django.views import View
from .forms import DetallePedidoForm

def lista_productos(request):
    # Filtrar los productos con estado=True
    productos_disponibles = Producto.objects.filter(estado=True)

    # Manejar el formulario de DetallePedido
    if request.method == 'POST':
        detalle_form = DetallePedidoForm(request.POST)
        if detalle_form.is_valid():
            detalle_pedido = detalle_form.save(commit=False)
            # Guardar el detalle_pedido en la sesión del usuario
            carrito = request.session.get('carrito', [])
            carrito.append({
                'producto_id': detalle_pedido.producto.id,
                'cantidad': detalle_pedido.cantidad,
            })
            request.session['carrito'] = carrito

    # Pasar la información al template
    context = {
        'productos_disponibles': productos_disponibles,
        'detalle_form': DetallePedidoForm(),
    }

    # Renderizar el template con la información
    return render(request, 'consultarProductos.html', context)

def mysite(request):
    # Lógica de negocio aquí
    return render(request, 'mysite.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect(reverse('lista_productos'))
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def miCarrito(request):
    carrito = request.session.get('carrito', [])
    total_items = sum(item['cantidad'] for item in carrito)
    
    total_precio = sum(
        item['cantidad'] * Producto.objects.filter(id=item['producto_id']).first().precioUnitario
        for item in carrito
    )

    productos_en_carrito = [
        {
            'producto': Producto.objects.filter(id=item['producto_id']).first(),
            'cantidad': item['cantidad'],
        }
        for item in carrito
    ]

    context = {
        'productos_en_carrito': productos_en_carrito,
        'total_items': total_items,
        'total_precio': total_precio,
    }

    return render(request, 'miCarrito.html', context)


def detallePago(request):
    return render(request, 'detallePago.html')

def lista_productos(request):
    # Filtrar los productos con estado=True
    productos_disponibles = Producto.objects.filter(estado=True)

    # Pasar la información al template
    context = {
        'productos_disponibles': productos_disponibles,
    }

    # Renderizar el template con la información
    return render(request, 'consultarProductos.html', context)
