from django.shortcuts import render

def mysite(request):
    # Lógica de negocio aquí
    return render(request, 'mysite.html')