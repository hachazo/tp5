# Cree una clase Helper con un método que permita traducir una palabra de español a
# inglés. Establezca traducciones para al menos 5 palabras.
# Cree una clase Helper dos métodos: uno que convierta una cadena a mayúsculas y
# otro que convierta a minúsculas.
# Luego, implemente un patrón Facade para permitir el acceso a estos tres métodos
# desde una nueva clase

class Helper():
    def __init__(self):
        self.traducciones = {"hola":"hello","adios":"goodbye","casa":"house","perro":"dog","gato":"cat"}
    
    def traducir(self,palabra):
        return self.traducciones.get(palabra)
    
    def mayusculas(self,palabra):
        return palabra.upper()
    
    def minusculas(self,palabra):
        return palabra.lower()

class Facade():
    def __init__(self):
        self.helper = Helper()
    
    def traducir(self,palabra):
        return self.helper.traducir(palabra)
    
    def mayusculas(self,palabra):
        return self.helper.mayusculas(palabra)
    
    def minusculas(self,palabra):
        return self.helper.minusculas(palabra)

facade = Facade()
print(facade.traducir("hola"))
print(facade.mayusculas("hola"))
print(facade.minusculas("HOLA"))