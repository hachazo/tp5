# Aplique el patrón State para simular el funcionamiento de atención de una caja en un
# banco. La clase Banco tiene una caja y este puede atender una persona, suspender,
# cerrar y abrir la caja. La caja tiene el nombre del cajero y el estado actual, los estados
# posibles son:
# a. Abierta: imprime por pantalla al cliente próximo en la fila.
# b. Suspendida: en este estado solo atiende a personas mayores a 60 años de
# edad, en otro caso imprime un mensaje de espera.
# c. Cerrada: no atiende personas y muestra mensajes indicando su estado.
# Pruebe el correcto funcionamiento del sistema creando personas con diferentes edades
# y cambiando los estados de la caja.

from __future__ import annotations
from abc import ABC, abstractmethod

class Contexto():
    _estado = None
    def __init__(self, estado: Estado) -> None:
        self.transicion(estado)
    def transicion(self, estado: Estado):
        print(f'Contexto: transición a {type(estado).__name__}')
        self._estado = estado
        self._estado.contexto = self
    def solicitar(self):
        self._estado.solicitar()

class Estado(ABC):
    _contexto = None
    @property
    def contexto(self) -> Contexto:
        return self._contexto
    @contexto.setter
    def contexto(self, contexto: Contexto) -> None:
        self._contexto = contexto
    @abstractmethod
    def solicitar(self) -> None:
        pass

class Abierta(Estado):
    def solicitar(self) -> None:
        print('Abierta: imprime por pantalla al cliente próximo en la fila.')

class Suspendida(Estado):
    def solicitar(self) -> None:
        print('Suspendida: en este estado solo atiende a personas mayores a 60 años de edad, en otro caso imprime un mensaje de espera.')

class Cerrada(Estado):
    def solicitar(self) -> None:
        print('Cerrada: no atiende personas y muestra mensajes indicando su estado.')

class Banco():
    def __init__(self) -> None:
        self._estado = None
    def transicion(self, estado: Estado) -> None:
        self._estado = estado
        self._estado.contexto = self
    def solicitar(self) -> None:
        self._estado.solicitar()
