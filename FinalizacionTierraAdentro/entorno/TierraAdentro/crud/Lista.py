class Listado:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        lista = self.session.get("lista")
        if not lista:
            self.session["lista"] = {}
            self.lista = self.session["lista"]
        else:
            self.lista = lista
            
    def agregar(self, productos, venta_id, detalle_venta):
        
        #id = str(venta_id)
        #pro = productos.object.get(id = detalle.producto_id)
        
        detalle = detalle_venta.objects.filter(venta_id = venta_id)
        for dv in detalle:
            
            id = str(dv.id)
              
            if id not in self.lista.keys():
                pro = productos.objects.get(id = dv.producto_id)
                self.lista[id]={
                    "id_venta" : venta_id, 
                    "pro_id" : dv.producto_id,
                    "nombre_producto": pro.nombre,
                    "cantidad": dv.cantidad,
                    "precio": dv.precio,
                    #"opcion": "historial",
                }
                self.guardar()
            
            
            
    
        
        
    def guardar(self):
        self.session["lista"] = self.lista
        self.session.modified = True  
        
    def limpiar(self, detalle, venta_id):
        detalle_venta = detalle.objects.filter(venta_id = venta_id)
        for dv in detalle_venta:
            id = str(dv.id)
            if id in self.lista.keys():
                del self.session["lista"][id]
                self.session.modified = True 
        #self.session["lista"] = {}
        #self.session.modified = True  