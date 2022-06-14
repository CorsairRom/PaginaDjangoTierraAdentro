from django.contrib import admin
from .models import Categoria, Producto, Contacto, Cliente, DetalleVenta, Venta
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria", "stock"]
    list_editable = ["precio", "stock"]
    search_fields = ["nombre"]
    list_filter = ["categoria", "stock"]
    list_per_page = 10
    
class VentasAdmin (admin.ModelAdmin):
    list_display = ["cliente", "total", "estado", "fecha", "hora"]
    list_filter = ["estado", "cliente"]
    list_per_page: 10
    
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Venta, VentasAdmin)
admin.site.register(DetalleVenta)

admin.site.register(Contacto)