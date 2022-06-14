from datetime import datetime
from distutils.command.upload import upload
from tkinter import CASCADE
from typing import Tuple
import django
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, IntegerField



# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="producto", null=True)
    usuario = models.ForeignKey(User, blank= True, null= True, on_delete=models.CASCADE) #nuevo
    def __str__(self):
        return self.nombre
   
opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
    
]
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensajes = models.TextField()
    
    def __str__(self):
        return self.nombre
  
    
class Cliente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    rut = models.CharField(unique=True, max_length=10)
    direccion = models.CharField( max_length=50)
    n_celular = models.CharField(max_length=10, verbose_name="Numero celular")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    subscriptor = models.BooleanField(default=False)
    vendedor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido
 
    
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField('fecha creacion', auto_now_add=True, null=True)
    hora = models.DateTimeField(auto_now_add=True, null=True)
    total = models.CharField(max_length=100, default=0)
    estado = models.CharField(max_length=30, default='En espera')
    
    def __str__(self):
        return str (self.cliente )
    
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, db_column='venta_id', on_delete=models.CASCADE, blank=True, null= True)
    producto = models.ForeignKey(Producto, db_column='producto_id', on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(default=1)
    precio = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.precio)+ ' '+str(self.cantidad) 
    
class Lista(models.Model):
    click_nombre= models.CharField(max_length=10)  #guardo el nombre del producto
    cant_click =  models.IntegerField() #guardo la cantidad de click que ise sobre el
    usuario = models.ImageField()#usuario al que le corresponde esta lista