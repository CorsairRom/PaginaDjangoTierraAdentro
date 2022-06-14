from crud.views import about, agregar, arbustos, borrar_registro, cambiarpass, carro, cliente, contacto, eliminar, eliminar_producto, estadoPedido, flores, guardar,  \
    index, limpiar_carrito, limpiar_lista, maceteros, modificar, perfil, permiso, productos, registrar, restar_producto, sumar_producto, tierrahojas, ver_detalle

from django.urls import  path

urlpatterns = [
    path('', index, name="index"),
    path('productos/', productos, name="productos"),
    path('arbustos/', arbustos, name="arbustos"),
    path('flores/', flores, name="flores"),
    path('maceteros/', maceteros, name="maceteros"),
    path('tierrahojas/', tierrahojas, name="tierrahojas"),
    path('about/', about, name="about"),
    path('contacto/', contacto, name="contacto"),
    path('registrar/', registrar, name="registrar"),
    path('perfil/<opcion>/', perfil, name="perfil"),
    path('carro/', carro, name="carro"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('agregar/<int:producto_id>/<str:pagina>/', agregar, name="agregar"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', restar_producto, name="restar"),
    path('sumar/<int:producto_id>/', sumar_producto, name="sumar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    path('guardar/', guardar, name="guardar"),
    path('borrar_registro/<int:venta_id>/', borrar_registro, name="borrar_registro"),
    path('ver_detalle/<int:venta_id>/', ver_detalle, name="ver_detalle"),
    path('limpiar_lista/<int:venta_id>', limpiar_lista, name="limpiar_lista"),
    path('estadoPedido/<int:venta_id>/<int:opcion>', estadoPedido, name="estadoPedido"),
    path('cliente/', cliente, name="cliente"),
    path('cambiarpass/', cambiarpass, name="cambiarpass"),
    path('permiso/', permiso, name="permiso"),
    
    
    
]