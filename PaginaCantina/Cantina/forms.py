from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import Select, DateInput, NumberInput, TextInput, PasswordInput, DecimalField, ImageField, BooleanField, ModelMultipleChoiceField

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nombre', 'ubicacion']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ubicacion' : TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombreYApellido', 'usuario', 'contrasenia', 'dni', 'legajo', 'cuentaCorriente', 'fechaNacimiento', 'area']
        widgets = {
            'nombreYApellido': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'usuario' : TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'contrasenia' : PasswordInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'dni' :NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'legajo' : NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cuentaCorriente' : DecimalField(
                attrs={
                    'class': 'form-control',
                }
            ),
            'fechaNacimiento' : DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'area' : Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precioUnitario', 'stock', 'imagen', 'estado']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descripcion' : TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'precioUnitario' : DecimalField(
                attrs={
                    'class': 'form-control',
                }
            ),
            'stock' :NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen' : ImageField(
                attrs={
                    'class': 'form-control',
                }
            ),
            'estado' : BooleanField(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['produto', 'cantidad']
        widgets = {
            'producto': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'cantidad': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'detalles', 'fechaPedido']
        widgets = {
            'cliente': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'detalles': ModelMultipleChoiceField(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fechaPedido' : DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['user']
        widgets = {
            'user': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        
class UserCreationFormExtended(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)  # Agrega el campo de correo electrónico

class CuentaCorrienteForm(forms.ModelForm):
    class Meta:
        model = CuentaCorriente
        fields = ['cliente', 'saldo']
        widgets = {
            'cliente': Select(   # Esta puesto como OneToOneField creo que funcionara con Select
                attrs={
                    'class': 'form-control'
                }
            ),
            'saldo': DecimalField( 
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class InformeCuentasCorrientesForm(forms.ModelForm):
    class Meta:
        model = InformeCuentasCorrientes
        fields = ['emisor', 'fecha_emision']
        widgets = {
            'emisor': Select(   # Raro
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha_emision' : DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }
