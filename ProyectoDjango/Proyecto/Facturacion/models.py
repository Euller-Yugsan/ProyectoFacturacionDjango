from django.db import models
from django.utils import timezone
# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)
    prueba = models.BooleanField(default=True)
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creacion")
    modificacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Modificacion")

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ["-creacion"]
    
    def __str__(self):
        return self.descripcion


class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)
    prueba = models.BooleanField(default=True)
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creacion")
    modificacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Modificacion")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ["-creacion"]
    
    def __str__(self):
        return self.cliente

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField(default=0)
    prueba = models.BooleanField(default=True)
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creacion")
    modificacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Modificacion")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ["-creacion"]

    def __str__(self):
        return self.factura





    


