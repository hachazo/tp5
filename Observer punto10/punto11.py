# Permite definir un mecanismo de suscripcion para notificar a multiples objetos
# de un evento que ocurra sobre el objeto que estan observando.

# Ejemplo: subscribirse a un canal de youtube que 
# este se encarge de noficarte cuando suba un video nuevo.

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Observable(ABC): # Metodos que tendra el objeto observable
    @abstractmethod
    def agregar(self, observador: Observador) -> None:
        pass
    
    @abstractmethod
    def quitar(self, observador: Observador) -> None:
        pass
    
    @abstractmethod
    def notificar(self) -> None:
        pass
    
# El bojeto observable tiene que tener un listado de objetos a los cuales
# poder notificar.
# Ademas tiene quev poder agregar y quitar objetos de ese listado.

class SistemaMeteorologico(Observable): # Objeto observable concreto
    _estado: str = None
    _observadores: List[Observador] = []
    
    def agregar(self, observador: Observador) -> None:
        self._observadores.append(observador)
        
    def quitar(self, observador: Observador) -> None:
        self._observadores.remove(observador)
        
    def notificar(self) -> None: # Metodo que notifica a los observadores (en este caso reportero)
        print("Sistema meteorologico: Notificando a los observadores...")
        for observador in self._observadores:
            observador.actualizar(self)
            
    def cambiar_estado(self) -> None: # Metodo que contiene lo que se va a notificar a los observadores 
                                      #(en este caso el estado del clima que tiene el reportero)
        print("\nSistema meteorologico: Cambiando estado...")
        self._estado = randrange(0, 10)
        print(f"Sistema meteorologico: Mi estado ha cambiado a: {self._estado}")
        self.notificar()

class Observador(ABC): # Metodos que tendra el objeto observador ( en este caso el reportero)
    @abstractmethod
    def actualizar(self, observable: Observable) -> None:
        pass
    
# El objeto observador tiene que poder actualizar su estado cuando el objeto
# observable cambie su estado.
class Reportero(Observador): # Objeto observador concreto
    def actualizar(self, observable: Observable) -> None:
        if observable._estado < 3:
            print("Reportero: El clima es soleado")
        elif observable._estado == 3:
            print("Reportero: El clima es nublado")
        else:
            print("Reportero: El clima es lluvioso")

sistema_meteorologico = SistemaMeteorologico()

reportero1 = Reportero()
reportero2 = Reportero()
sistema_meteorologico.agregar(reportero1)
#sistema_meteorologico.agregar(reportero2)
sistema_meteorologico.cambiar_estado()
sistema_meteorologico.notificar()