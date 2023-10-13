from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    def __init__(self, name) -> None: 
        self._name = name
        
    def add(self, component: Component) -> None:
        pass
    
    def remove(self, component: Component) -> None:
        pass
    
    def is_folder(self) -> bool:
        return False
    
    @abstractmethod
    def mostrar(self) -> str:
        pass
    @abstractmethod
    def crear(self) ->bool:
        pass

class File(Component):
    def mostrar(self) -> str:
        return self._name
    
    def crear(self)-> bool:
        open(self._name, "x") #

class Folder(Component):
    def __init__(self,name) -> None:
        super().__init__(name)
        self._children: List[Component] = []
        
    def add(self,component):
        self._children.append(component)
    
    def is_folder(self) -> bool:
        return True
    
    def remove(self,component):
        self._children.remove(component)
    
    def print(self):
        result=self._name
        for child in self._children:
            result+="\t"+child.print()
            result+="\n"
        return result
    
def client_file(component: Component):
    print(component.mostrar())

def client_file_archive(component1: Component, component2: Component):
    if component1.is_folder():
        component1.add(component2)
    print(component1.mostrar())
    
file1 = File("file_1.txt")
client_file(file1)

carpeta1=Folder(File("file_2.txt"))
