class Producto():
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def getPrecio(self):
        return self._precio

class ProductoDecorator(Producto):
    def __init__(self,producto):
        self._producto = producto
    
    def getPrecio(self):
        return self._producto.getPrecio()
    
class Producto_usd_Decorator(ProductoDecorator):
    def __init__(self,producto):
        self._producto = producto
        
    def getPrecio(self):
        return f"$USD: {self._producto.getPrecio()}"
    
class Producto_ars_Decorator(ProductoDecorator):
    def __init__(self,producto):
        self._producto = producto
        
    def getPrecio(self):
        return f"$ARS: {self._producto.getPrecio()}"
    
def getPrecio(producto: Producto):
    print(producto.getPrecio())
    
producto1 = Producto("Coca-Cola", 100)
producto2 = Producto_ars_Decorator(producto1)
getPrecio(producto2)