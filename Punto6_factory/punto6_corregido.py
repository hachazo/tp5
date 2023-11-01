# Aplique el patrón Factory Method para la creación de juegos físicos y digitales. Los
# juegos comparten un id y un importe. También el método abstracto getPrecio, que se
# encarga de calcular el precio de uno u otro. Para ello los juegos físicos tienen un
# atributo que es el precio de traslado (a caso de ejemplo elija usted). Y los juegos
# digitales el precio depende de la plataforma en la cual se compra teniendo como
# atributo el precio de la plataforma. Estos valores deben ser float y multiplicarlos al
# importe.

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Creator(ABC): 
              
    @abstractmethod
    def factory_method(self):
        pass
    
    def getPrecio(self) -> str:
        notificador = self.factory_method()
        result = f"Creator: Se notifico al usuario con el precio de {notificador.calcular_precio()}"
        return result
    
class ConcreteCreatorJuegoFisico(Creator):
    def __init__(self,id,importe,precio_traslado):
        self._id = id
        self._importe = importe
        self._precio_traslado = precio_traslado
    
    def factory_method(self) -> JuegoFisico:    
        return JuegoFisico(self._importe,self._precio_traslado)
    
class ConcreteCreatorJuegoDigital(Creator):
    def __init__(self,id,importe,plataforma):
        self._id = id
        self._importe = importe
        self._plataforma = plataforma
    def factory_method(self) -> JuegoDigital:    
        return JuegoDigital(self._importe,self._plataforma)

class Notificacion(ABC):
    @abstractmethod
    def calcular_precio(self) -> int:
        pass

class JuegoFisico(Notificacion):
    def __init__(self,importe,precio_traslado):
        self._importe = importe
        self._precio_traslado = precio_traslado
        
    def calcular_precio(self) -> int:
        return self._importe * self._precio_traslado

class JuegoDigital(Notificacion):
    def __init__(self,importe,plataforma):
        self._importe = importe
        self._plataforma = plataforma
        
    def calcular_precio(self) -> int:
        return self._importe * self._plataforma

def enviar_notificacion(creator: Creator) -> None:
    print(creator.getPrecio())
    
enviar_notificacion(ConcreteCreatorJuegoFisico(1,600,1.5))
enviar_notificacion(ConcreteCreatorJuegoDigital(1,1000,1.2))