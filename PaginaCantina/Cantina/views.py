from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClienteForm, UserCreationFormExtended, TuFormularioDeFiltro, DetallePedidoForm
from .models import *
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def mysite(request):
    # Lógica de negocio aquí
    return render(request, 'mysite.html')

def detalledePago(request):
    return render(request, 'detalledePago.html')

def detalledeEntrega(request):
    return render(request, 'detalledeEntrega.html')

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


def detalleDeEntregaYPago(request):
    return render(request, 'detalleDeEntregaYPago.html')

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
    
    cliente_id = request.user.id  # Obtener el ID del usuario autenticado

    nuevo_pedido = Pedido.objects.create(cliente_id=cliente_id)  # Usar el ID del cliente obtenido

    total_pedido = 0
    
    for producto in productos_disponibles:
            detalle_pedido = DetallePedido.objects.create(
                producto=producto,
                cantidad=producto.cantidad,
                subtotal=producto.subtotal
            )
            nuevo_pedido.detalles.add(detalle_pedido)
            total_pedido += producto.subtotal

    nuevo_pedido.total = total_pedido
    nuevo_pedido.save()

    productos_disponibles.update(carrito=0, cantidad=1)
        
    
    return render(request, 'consultarProductos.html', context)


def productos_en_carrito(request):
    productos_en_carrito = Producto.objects.filter(carrito=1)
    return render(request, 'agregar_al_carrito.html', {'productos_en_carrito': productos_en_carrito})

def actualizar_carrito(request, product_id):
    producto = get_object_or_404(Producto, id=product_id)
    producto.carrito = 1
    producto.save()  # Actualiza el valor de 'carrito' a 1
    return JsonResponse({'success': True})

def quitarProducto(request, product_id):
    # Utiliza el decorador @require_POST para permitir solo solicitudes POST
    producto = get_object_or_404(Producto, id=product_id)
    producto.carrito = 0
    producto.save()
    return JsonResponse({'success': True})

def actualizar_subtotal(request):
    if request.method == 'POST':
        producto_id = request.POST.get('productoId')
        nuevo_subtotal = request.POST.get('nuevoSubtotal')

        try:
            carrito_item = Carrito.objects.get(id=producto_id)
            carrito_item.cantidad = nuevo_subtotal
            carrito_item.save()

            return JsonResponse({'nuevo_subtotal': nuevo_subtotal})
        except Carrito.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado en el carrito'})
    else:
        return JsonResponse({'error': 'Método no permitido'})

def guardar_datos(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('productos'))

        for item in data:
            try:
                producto = Producto.objects.get(id=item['id'])

                # Actualiza los campos del objeto existente
                producto.cantidad = item['cantidad']
                producto.subtotal = item['subtotal']

                producto.save()

            except Producto.DoesNotExist:
                # Manejar el caso donde el producto no existe en la base de datos
                pass

        return JsonResponse({'mensaje': 'Datos actualizados con éxito'})
    else:
        # Manejar el caso donde la solicitud no es POST
        pass


def obtener_areas(request):
    areas = Area.objects.all()
    areas_nombres = [area.nombre for area in areas]
    return JsonResponse({'areas': areas_nombres})

def calcular_total(request):
    try:
        productos = Producto.objects.filter(carrito=1)
        total = sum(producto.subtotal for producto in productos)
        return JsonResponse({'total': total})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def detalle_pedido(request):
    return render(request, 'detalleDeEntregaYPago.html')

def detalles_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalles_pedido = DetallePedido.objects.filter(pedido=pedido)  # Obtener detalles asociados a este pedido
    return render(request, 'detalles_pedido.html', {'pedido': pedido, 'detalles_pedido': detalles_pedido})



@login_required
def consultarPedido(request):
    productos_seleccionados = Producto.objects.filter(carrito=1)
    if request.user.is_authenticated:
        cliente_id = request.user.id  # Obtener el ID del usuario autenticado

        nuevo_pedido = Pedido.objects.create(cliente_id=cliente_id)  # Usar el ID del cliente obtenido

        total_pedido = 0  # Inicializamos el total del pedido

        for producto in productos_seleccionados:
            detalle_pedido = DetallePedido.objects.create(
                producto=producto,
                cantidad=producto.cantidad,
                subtotal=producto.subtotal
            )
            nuevo_pedido.detalles.add(detalle_pedido)
            total_pedido += producto.subtotal

        nuevo_pedido.total = total_pedido
        nuevo_pedido.save()


        return render(request, 'consultarPedido.html', {'nuevo_pedido': nuevo_pedido})

@login_required
def lista_pedidos(request):
    # Obtener los pedidos del usuario autenticado
    pedidos_usuario = Pedido.objects.filter(cliente=request.user)
    
    # Pasar los pedidos al contexto
    context = {
        'pedidos_usuario': pedidos_usuario
    }

    return render(request, 'lista_pedidos.html', context)

def obtener_pedidos(request):
    # Lógica para obtener los pedidos
    return render(request, 'obtener_pedidos.html', context)


def verCtaCte(request):
    return render(request, 'verCtaCte.html')

def resetPassword2(request):
    return render(request, 'resetPassword2.html')


def revisionPedido(request):
    return render(request, 'revisionPedido.html')

def detallePagoFinal(request):
    return render(request, 'detallePagoFinal.html')

