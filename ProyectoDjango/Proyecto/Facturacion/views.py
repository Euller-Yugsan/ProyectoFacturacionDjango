from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProductoForm,ClienteForm,FacturaForm
from .models import Producto,Cliente,Factura

def menu(request):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Productos', 'Cliente': 'Clientes','Venta':'Ventas'}
    return render(request,'principal.html',opciones)


def producto(request):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Productos', 'Cliente': 'Clientes','Venta':'Ventas','accion':'Ingresar'}
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')
    else:
        form = ProductoForm()
        opciones['form'] = form
    return render(request, 'producto.html', opciones)


def cliente(request):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Productos', 'Cliente': 'Clientes','Venta':'Ventas','accion':'Ingresar'}
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, 'cliente.html', opciones)



def listarProducto(request):
    producto = Producto.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Productos', 'Cliente': 'Clientes','Venta':'Ventas','productos':producto}
    return render(request, 'listar_producto.html', opciones)

def listarCliente(request):
    cliente = Cliente.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Productos', 'Cliente': 'Clientes','Venta':'Ventas','clientes':cliente}
    return render(request, 'listar_cliente.html', opciones)



def editarProducto(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Productos', 'Cliente': 'Clientes','Venta':'Ventas','accion':'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')

    return render(request, 'producto.html', opciones)

def editarCliente(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Productos', 'Cliente': 'Clientes','Venta':'Ventas','accion':'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')

    return render(request, 'cliente.html', opciones)

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarproducto')
    return render(request, 'eliminar_producto.html', {'Producto': producto})

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarcliente')
    return render(request, 'eliminar_cliente.html', {'Cliente': cliente})    


def listarFactura(request):
    factura = Factura.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Productos', 'Cliente': 'Clientes','Venta':'Ventas','facturas':factura}
                
    return render(request, 'listar_factura.html', opciones)







