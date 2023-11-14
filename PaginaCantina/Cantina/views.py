from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClienteForm
from .forms import UserCreationFormExtended
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
            return redirect('base.html')  # Cambia 'nombre_de_tu_vista_principal' por el nombre de tu vista principal
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



def lista_productos(request):
    # Filtrar los productos con estado=True
    productos_disponibles = Producto.objects.filter(estado=True)

    # Pasar la información al template
    context = {
        'productos_disponibles': productos_disponibles,
    }

    # Renderizar el template con la información
    return render(request, 'consultarProductos.html', context)