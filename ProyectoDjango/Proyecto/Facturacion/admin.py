
from .models import Producto,Cliente,Factura

from django.contrib import admin

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display = ('descripcion', 'precio', 'stock','iva' ,'creacion')
    ordering = ('descripcion',)
    search_fields = ('descripcion',)
    list_filter = ('descripcion',)

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display = ('ruc', 'nombre', 'direccion','creacion')
    ordering = ('nombre',)
    search_fields = ('nombre','ruc')
    list_filter = ('nombre',)




    
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)

