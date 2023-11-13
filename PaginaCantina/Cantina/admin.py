from django.contrib import admin

from django.contrib import admin
from .models import Producto, Area
    
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    
class AreaAdmin(admin.ModelAdmin):
    ordering = ['nombre']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Area, AreaAdmin)