# Permite definir un mecanismo de suscripcion para notificar a multiples objetos
# de un evento que ocurra sobre el objeto que estan observando.

# Ejemplo: subscribirse a un canal de youtube que 
# este se encarge de noficarte cuando suba un video nuevo.

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC): # Metodos que tendra el objeto observable 
    @abstractmethod
    def attach(self, observer: Observer) -> None: # agregar un subscritor

        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None: # quitar un subscritor

        pass

    @abstractmethod
    def notify(self) -> None: # notificar a los subscritores
        pass

# El bojeto observable tiene que tener un listado de objetos a los cuales
# poder notificar.
# Ademas tiene quev poder agregar y quitar objetos de ese listado.

class ConcreteSubject(Subject): # Objeto observable concreto
    state: int = None


    observers: List[Observer] = [] # listado de subscritores

    def attach(self, observer: Observer) -> None: # agregar un subscritor
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None: # quitar un subscritor
        self._observers.remove(observer)

    def notify(self) -> None: # notificar a los subscritores

        # print("Subject: Notifying observers...")
        # for observer in self._observers:
        #     observer.update(self)

    def some_business_logic(self) -> None: # Metodo que contiene lo que se va a notificar a los observadores

        # print("\nSubject: I'm doing something important.")
        # self._state = randrange(0, 10)

        # print(f"Subject: My state has just changed to: {self._state}")
        # self.notify()


class Observer(ABC): # Metodos que tendra el objeto observador ( en este caso el subscritor)

    @abstractmethod
    def update(self, subject: Subject) -> None: # actualizar su estado cuando el objeto observable cambie su estado.

        pass

# class ConcreteObserverA(Observer): # subscritor concreto
#     def update(self, subject: Subject) -> None:
#         if subject._state < 3:
#             print("ConcreteObserverA: Reacted to the event")


# class ConcreteObserverB(Observer): # subscritor concreto
#     def update(self, subject: Subject) -> None:
#         if subject._state == 0 or subject._state >= 2:
#             print("ConcreteObserverB: Reacted to the event")
