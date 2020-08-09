
from django import forms
from .models import Producto,Cliente,Factura


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock','iva')
        label = {'descripcion': 'Descripcion', 'precio': 'precio', 'stock': 'Stock','iva':'Iva'}

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion')
        label = {'ruc': 'Ruc', 'nombre': 'Nombre', 'direccion': 'Direccion'}
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('cliente', 'fecha', 'total')
        label = {'cliente': 'Cliente', 'fecha': 'Fecha', 'total': 'Total'}      
