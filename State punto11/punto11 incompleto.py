# Permite que un objeto modifique su comportamiento cada vez que cambie su estado interno. Parecería como si cambiara su clase.
#permite que un objeto ejecute distintas lineas de codigo dependiendo de su estado interno.

#from __future__ import annotationssu
from abc import ABC, abstractmethod

class Banco: # clase context (solo visible para el cliente), todo lo demas esta oculto para el cliente
    def __init__(self):
        self._estado = Cerrado(lista)
        
    def set_estado(self, estado):
        self._estado = estado
        
    def get_estado(self):
        return self._estado
    
    def abierto(self):
        self._estado.abierto()
     
    def suspendido(self):
        self._estado.suspendido()
           
    def cerrado(self):
        self._estado.cerrado()
    
class Estado(ABC): # la clase context delega el trabajo a la clase estado, la clase context save que se va a ejecutar algo pero no sabe que
    @abstractmethod
    def abierto(self):
        pass
    
    @abstractmethod
    def suspendido(self):
        pass
    
    @abstractmethod
    def cerrado(self):
        pass
    
class Abierto(Estado):
    def __init__(self,lista):
        super().__init__()
        self._lista = lista
    def abierto(self):
        print(f"El proximo cliente es: {self._lista[0]._nombre}")
    
    def suspendido(self):
        print("La caja esta abierta")
    
    def cerrado(self):
        print("La caja esta abierta")

class Suspendido(Estado):
    def __init__(self,lista):
        super().__init__()
        self._lista = lista
    
    def suspendido(self): 
        if self._lista[0]._edad > 60:
            print(f"El proximo cliente es: {self._lista[0]._nombre}")
        print("No te podemos atender, la caja solo atiende a personas mayores de 60 años")
    
    def cerrado(self):
        print("Por favor espere")
    
    def abierto(self):
        print("Por favor espere")
        

class Cerrado(Estado):
    def __init__(self,lista):
        super().__init__()
        self._lista = lista
    def cerrado(self):
        print("La caja ya esta cerrada")
    
    def abierto(self):
        print("La caja ya esta cerrada")
    
    def suspendido(self):
        print("La caja ya esta cerrada")
#### Termina el patron state ####        
        
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
lista = []
lista.append(Persona("juan", 21))
lista.append(Persona("pedro", 30))
lista.append(Persona("maria", 63))
lista.append(Persona("jose", 55))
lista.append(Persona("luis", 70))

banco = Banco()
banco.set_estado(Abierto(lista))
banco.get_estado().abierto()

lista.remove(lista[0])
#banco.get_estado().abierto()
banco.get_estado().suspendido()

