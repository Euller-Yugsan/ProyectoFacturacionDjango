"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Facturacion.views import menu , producto,listarProducto,editarProducto,eliminarProducto,listarCliente,cliente,editarCliente,eliminarCliente,listarFactura
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='index'),
    path('producto/', producto, name='producto'),
    path('cliente/', cliente, name='cliente'),
    path('editarproducto/<int:id>/',editarProducto,name='editarproducto'),
    path('editarcliente/<int:id>/',editarCliente,name='editarcliente'),
    path('listarproducto/', listarProducto, name='listarproducto'),
    path('eliminarproducto/<int:id>', eliminarProducto, name='eliminarproducto'),
    path('eliminarclienre/<int:id>', eliminarCliente, name='eliminarcliente'),
    path('listarcliente/', listarCliente, name='listarcliente'),
    path('listarfactura/', listarFactura, name='listarfactura'),

    
]
