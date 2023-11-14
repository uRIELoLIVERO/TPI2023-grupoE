from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClienteForm, UserCreationFormExtended, TuFormularioDeFiltro, DetallePedidoForm
from .models import *
from django.views import View

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
            return redirect(reverse('consultarProductos'))
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

def consultarProductos(request):
    productos_disponibles = Producto.objects.filter(estado=True)

    if request.method == 'GET':
        form = TuFormularioDeFiltro(request.GET)

        if form.is_valid():
            rango_precio = form.cleaned_data.get('rango_precio')
            tipo_orden = form.cleaned_data.get('tipo_orden')

            if rango_precio:
                min_precio, max_precio = map(int, rango_precio.split('-'))
                productos_disponibles = productos_disponibles.filter(precioUnitario__range=(min_precio, max_precio))

            if tipo_orden == 'A-Z':
                productos_disponibles = productos_disponibles.order_by('nombre')
            elif tipo_orden == 'Z-A':
                productos_disponibles = productos_disponibles.order_by('-nombre')
            elif tipo_orden == 'menor-mayor':
                productos_disponibles = productos_disponibles.order_by('precioUnitario')
            elif tipo_orden == 'mayor-menor':
                productos_disponibles = productos_disponibles.order_by('-precioUnitario')

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
 
    context = {
        'productos_disponibles': productos_disponibles,
        'form': TuFormularioDeFiltro(),
        'detalle_form': DetallePedidoForm(),
    }

    return render(request, 'consultarProductos.html', context)

