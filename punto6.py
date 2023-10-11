from __future__ import annotations
from abc import ABC, abstractmethod
# Patron Factory Method

#Aplique el patrón Factory Method para la creación de juegos físicos y digitales. Los
# juegos comparten un id y un importe. También el método abstracto getPrecio, que se
# encarga de calcular el precio de uno u otro. Para ello los juegos físicos tienen un
# atributo que es el precio de traslado (a caso de ejemplo elija usted). Y los juegos
# digitales el precio depende de la plataforma en la cual se compra teniendo como
# atributo el precio de la plataforma. Estos valores deben ser float y multiplicarlos al
# importe.
class JuegoFisico(ABC): # clase product
    def __init__(self,id,importe,precio_traslado):
        self._id = id
        self._importe = importe
        self._precio_traslado = precio_traslado
    
    @abstractmethod
    def getPrecio(self):
        pass
    
class JuegoDigital(ABC): # Clase product
    def __init__(self,id,importe,plataforma):
        self._id = id
        self._importe = importe
        self._plataforma = plataforma
        
    @abstractmethod
    def getPrecio(self):
        pass

class JuegoFisicoFactory(ABC): # Clase Creator
    @abstractmethod
    def factory_method(self):
        pass
    
    def notificar(self) -> str:
        notificador = self.factory_method()
        result = f"Creator: notifico al usuario con: {notificador.getPrecio()}"
        return result

class JuegoDigitalFactory(ABC): # Clase Creator
    @abstractmethod
    def factory_method(self):
        pass
    
    def notificar(self) -> str:
        notificador = self.factory_method()
        result = f"Creator: notifico al usuario con: {notificador.getPrecio()}"
        return result

class ConcreteCreatorJuegoFisicoPS4(JuegoFisicoFactory): # Clase ConcreteCreator
    def factory_method(self) -> JuegoFisico:
        return JuegoFisicoPS4(1,100,1.5)


class   JuegoFisicoPS4(JuegoFisico): # Clase ConcreteProduct
    def getPrecio(self):
        return self._importe * self._precio_traslado
    
class   JuegoFisicoXBOX(JuegoFisico): # Clase ConcreteProduct
    def getPrecio(self):
        return self._importe * self._precio_traslado

class   JuegoDigitalPS4(JuegoDigital): # Clase ConcreteProduct
    def getPrecio(self):
        return self._importe * self._plataforma

class  JuegoDigitalXBOX(JuegoDigital): # Clase ConcreteProduct
    def getPrecio(self):
        return self._importe * self._plataforma

def notificar_precio(creator: JuegoFisicoFactory) -> None: # Clase Client
    print(f"Cliente: No se sabe de que forma se envia la notificación, pero se que se lo puedo pedir.\n"
        f"{creator.notificar()}", end="")

notificar_precio(ConcreteCreatorJuegoFisicoPS4())
# print("Juego Fisico PS4")
# enviar_notificacion(JuegoFisicoPS4(1,100,1.5))
# print("\n")
# juego = JuegoFisicoPS4(1,100,1.5)