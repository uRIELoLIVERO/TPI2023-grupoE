from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import Select, DateInput, NumberInput, TextInput, PasswordInput, DecimalField, ImageField, BooleanField, ModelMultipleChoiceField, FileInput, CheckboxInput

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
        fields = ['nombreYApellido', 'dni', 'legajo', 'cuentaCorriente', 'fechaNacimiento', 'area']
        widgets = {
            'nombreYApellido': TextInput(attrs={'class': 'form-control'}),
            'dni': NumberInput(attrs={'class': 'form-control'}),
            'legajo': NumberInput(attrs={'class': 'form-control'}),
            'cuentaCorriente': NumberInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': DateInput(attrs={'class': 'form-control'}),
            'area': Select(attrs={'class': 'form-control'}),
        }

        # Nuevos campos para el usuario
        user_username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
        user_password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
 

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precioUnitario', 'stock', 'imagen', 'estado']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'precioUnitario': NumberInput(attrs={'class': 'form-control'}),
            'stock': NumberInput(attrs={'class': 'form-control'}),
            'imagen': FileInput(attrs={'class': 'form-control'}),  
            'estado': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad']
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
        fields = ['cliente', 'detalles']

    detalles = forms.MultipleChoiceField(
        choices=[(detalle.id, str(detalle)) for detalle in DetallePedido.objects.all()],
        widget=forms.CheckboxSelectMultiple,
    )

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
            'saldo': NumberInput( 
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class InformeCuentasCorrientesForm(forms.ModelForm):
    class Meta:
        model = InformeCuentasCorrientes
        exclude = ['fecha_emision']
        fields = ['emisor']
        widgets = {
            'emisor': Select(   # Raro
                attrs={
                    'class': 'form-control'
                }
            )
        }
class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico', max_length=254)