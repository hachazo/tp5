from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List # importa una lista de tipo Component


class Component(ABC):
    def __init__(self, name) -> None: 
        self._name = name # Definimos el artibuto name (atributo del componente) que es el nombre del archivo o carpeta

    @property
    def parent(self, name) -> Component: # Premite aceeder al componente padre
        return self._parent

    @parent.setter
    def parent(self, parent: Component): # Permite definir el componente padre
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:

        return False

    @abstractmethod
    def mostrar(self) -> str: # Metodo abstracto que permite mostrar el nombre del archivo o carpeta
        pass # (tienen que se implementados en las clases hijas (subclases))

    # @abstractmethod
    # def crear(self) ->bool: # Metodo abstracto que permite crear el archivo o carpeta
    #     pass # (tienen que se implementados en las clases hijas (subclases))


class File(Component): #  subclase de Component

    def mostrar(self) -> str: # Implementa el metodo mostrar de la clase padre
        return self._name # Devuelve el nombre del archivo
    
    def crear(self)-> bool: # Implementa el metodo crear de la clase padre
        open(self._name, "x") # Crea un archivo //NO SE USA
    


class Folder(Component):

    def __init__(self, name) -> None: # Inicializa el atributo self._children como una lista vacia
        super().__init__(name)
        self._children: List[Component] = []

    def add(self, component: Component) -> None: # Agrega un componente a la lista _children
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None: # Elimina un componente de la lista _children
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool: # Devuelve True si es un composite (una carpeta)
        return True

    def mostrar(self) -> str: # Implementa el metodo mostrar de la clase padre
        result = self._name # Devuelve el nombre de la carpeta
        for child in self._children: # y el nombre de los archivos que contiene de manera recursiva
            result+="\t"+child.mostrar()
        result+="\n"
        return result
    
    # def crear(self) ->bool: # Implementa el metodo crear de la clase padre
    #     open(self._name, "x") # Crea una carpeta // NO SE USA
    #     for child in self._children: # y los archivos que contiene de manera recursiva
    #         child.crear()
    #     return True
    
def client_code(component: Component) -> None: # funcion que toma un objeto de tipo Component
    print(component.mostrar()) # e imprime el nombre del archivo o carpeta con el metodo mostrar


def client_code2(component1: Component, component2: Component) -> None: # Se le pasa un objeto de Folder y otro de File
                                                                        # lo que permite tratar de manera uniforme los objetos pese a ser diferentes.
    if component1.is_composite():
        component1.add(component2) # Se le agrega un archivo al final de la lista (en este caso la variable archivo)
    print(component1.mostrar())


archivo = File("archivo_x.txt")
client_code(archivo)
print("\n")

root_folder = Folder("root")

folder1 = Folder("carpeta_1") # Es una lista de componentes
folder1.add(File("archivo1-1.txt"))
folder1.add(File("archivo1-2.txt"))

folder2 = Folder("carpeta_2") # Es una lista de componentes
folder2.add(File("archivo2-1.txt"))

root_folder.add(folder1)
root_folder.add(folder2)

print("Imprimimos el sistema de archivos:")
client_code(root_folder)
print("\n")

print("No es necesario saber :") # Se le agrega la variable arhivo al final de la lista.
client_code2(root_folder, archivo)