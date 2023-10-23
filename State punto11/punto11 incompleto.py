#from __future__ import annotationssu
from abc import ABC, abstractmethod

class Caja_banco:
    def __init__(self,cajero):
        self._estado = None
        self._nombre = cajero

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
    
class Estado(ABC):
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
    def __init__(self):
        super().__init__()
    
    def abierto(self):
        print("La caja ya esta abierta")
        