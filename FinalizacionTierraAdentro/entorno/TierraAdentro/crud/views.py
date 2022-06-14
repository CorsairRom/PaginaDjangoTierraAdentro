from ast import For, arg
from calendar import c
from cgitb import text
from email import message
from platform import processor
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from crud.Rut import validarRut
from crud.Carrito import Carrito
from crud.Lista import Listado
from crud.context_processor import total_carrito
from .models import Categoria, Cliente, DetalleVenta, Producto, Lista, Venta
from .forms import ClienteForm, Custom, ContactoForm, ProductoForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def renderProductos():
    productos = Producto.objects.all()
    
    data ={
        'productos':productos,
        
    }
    return data

def opciones (opcion):
    op ={
        0: "perfil",
        1: "historial",
        2: "lista_productos",
        3: "agregar_productos",   
    }
    return op.get(opcion, "Desconocido")

def index(request):
    
    return render(request, "crud/index.html")


def productos(request):
    
    return render(request, "crud/productos.html")

def arbustos(request):
    data = renderProductos()
    return render(request, "crud/arbustos.html", data)


    
def flores(request):
    data = renderProductos()
    
    return render(request, "crud/flores.html", data)


def maceteros(request):
    data = renderProductos()
    return render(request, "crud/maceteros.html", data)


def tierrahojas(request):
    data = renderProductos()
    return render(request, "crud/tierrahojas.html", data)


def about(request):
    return render(request,"crud/about.html")

def contacto(request):
    data = {
        "form": ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario    
    
    return render(request,"crud/contacto.html", data)

def registrar(request):
    data = {
        "form": Custom
    }
    if request.method == 'POST':
        formulario = Custom(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #redirigir al inicio
            user = authenticate(username= formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="cliente")
        data["form"]= formulario   
        
    return render(request, "registration/registrar.html", data)

@login_required()
def cliente(request):
    form = ClienteForm(request.POST or None)
    ctx = {
        "form" : form
    }
    if request.method == "POST":
        form2 = ClienteForm(data=request.POST)
        if form2.is_valid():
            datos = form2.cleaned_data
            cliente = Cliente()
            cliente.usuario = request.user
            cliente.nombre = datos.get("nombre")
            cliente.apellido = datos.get("apellido")
            cliente.rut = datos.get("rut")
            cliente.direccion = datos.get("direccion")
            cliente.n_celular = datos.get("n_celular")
            cliente.fecha_nacimiento = datos.get("fecha_nacimiento")
            cliente.save()
            return redirect(perfil, 0)
        else:
            return render(request, "registration/cliente.html", {"form": form2})
   
    
    return render(request, "registration/cliente.html", ctx)

@login_required()
def cambiarpass(request):
    form=PasswordChangeForm(request.POST or None)
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(perfil, 0)
    
    return render(request,"registration/cambiarpass.html",contexto)  
  

#@permission_required('is_vendedores')
@login_required()
def perfil(request, opcion):
    listado = Listado(request)
    usuario = request.user
    venta = Venta.objects.all()
    productos = Producto.objects.all()
    detalle_ventas = DetalleVenta.objects.filter(venta_id = 7)
    precios = []
    
    cliente = Cliente.objects.get(usuario_id = usuario.id)
    rut = validarRut(str(cliente.rut))
    ventas = Venta.objects.filter(cliente_id = cliente.id)
    prueba = "esta es la prueba"
    data={
        "form" : ProductoForm(),
        "productos" : productos,
        "ventas" : ventas,
        "opcion" : opcion,
        "prueba" : request.session["lista"].keys,
        "prueba2" : request.session["lista"].values,
        "venta" : venta,
        "cliente" : cliente,
        "rut" : rut
        #"prueba3" : request.session["lista"]['21'],
        
        
    }
    # for d in detalle_ventas:
    #     data["prueba"] = d.precio
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            pro = Producto.objects.latest('id')#nuevo
            pro.usuario_id = request.user.id#nuevo
            pro.save()#nuevo
        else:
            data["form"] = formulario 
    
    return render(request,"crud/perfil.html", data)

#Funciones modificar eliminar
@login_required()
@permission_required("is_vendedores")
def modificar(request, id):
    producto = get_object_or_404(Producto, id=id)
    data ={
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm (data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect(perfil, 2)
        data["form"] = formulario
    return render(request, "crud/modificar.html" , data)

@login_required()
@permission_required("is_vendedores")
def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(perfil, 2)
# Fin funciones modificar eliminar


#Funciones carrito
@login_required()
def carro(request):
    cliente = Cliente.objects.get(usuario_id = request.user.id)
    ctx = {
        "sub" : cliente.subscriptor
    }
    return render(request, "crud/carro.html", ctx)

@login_required()
def agregar(request, producto_id, pagina):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect(pagina)


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carro")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carro")

def sumar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.sumar(producto)
    return redirect("carro")
@login_required()    
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carro")

@login_required()
def guardar(request):
    usuario = request.user
    tot_carrito = total_carrito(request)
    carrito = Carrito(request)
    total = tot_carrito["total_carrito"]
    cliente = Cliente.objects.get(usuario_id = usuario.id)
    if cliente.subscriptor == True:
        total = tot_carrito["descuento"]
    ventas = Venta(cliente_id = cliente.id, total = total)
    ventas.save()
    venta_actual = Venta.objects.get(id = ventas.id)
    #guardar detalle
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            detalle = DetalleVenta(venta_id = venta_actual.id, producto_id = int(value["producto_id"]), cantidad = int(value["cantidad"]), precio = int(value["precio"]) )
            
            detalle.save()
            if cliente.subscriptor == False and int(value["producto_id"]) == 45:
                cliente.subscriptor = True
                cliente.save()
    carrito.limpiar()
    return redirect(perfil, 1)  
# Fin carrito


#borrar venta
def borrar_registro(request, venta_id):
    venta = Venta.objects.get(id = venta_id) 
    venta.delete()
    return redirect(perfil, 1)

@login_required()
def ver_detalle(request, venta_id):
    
    #detalle_venta = DetalleVenta.objects.filter(venta_id = venta_id)
    detalle_venta = DetalleVenta
    productos = Producto
    listado = Listado(request)
   
    listado.agregar(productos, venta_id, detalle_venta)
    
    return  redirect(perfil, 1)

@login_required()
def limpiar_lista(request, venta_id):
    detalle_venta = DetalleVenta
    
    lista = Listado(request)
    lista.limpiar(detalle_venta, venta_id)
    return redirect(perfil, 1)


@login_required()
@permission_required("is_superuser")
def estadoPedido(request, venta_id, opcion):
    venta = Venta.objects.get(id = venta_id)
    op = {
        0 : 'En proceso',
        1 : 'Despachado',
        2 : 'Entregado',
    }
    
        
    venta.estado = str(op.get(opcion))
    venta.save()
    return redirect(perfil, 4)

@login_required()
def permiso(request):
    usuario = request.user
    grupo = Group.objects.get(name = "vendedores")
    grupo.user_set.add(usuario)
    cliente = Cliente.objects.get(usuario_id= usuario.id)
    cliente.vendedor= True
    cliente.save()
    return redirect(perfil, 0)

