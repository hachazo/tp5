from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC): # Clase abstracta para construir el producto en este caso las tartas de vainilla y coco
# Define la interfaz que todos los constructores concretos deben seguir

    @property
    @abstractmethod
    def tarta(self) -> None: # Propiedad abstracta que debe devolver el producto construido.
        pass

    @abstractmethod
    def ingredientes(self) -> None:
        pass
    
    @abstractmethod
    def masa(self) -> None: # Método abstracto que construye la masa de la tarta. 
        pass

    @abstractmethod
    def relleno(self) -> None: # Método abstracto que construye el relleno de la tarta.
        pass

class IngredientesMassa(): # Clase que define los ingredientes para la masa de la tarta.
    @staticmethod
    def ingredientes():
        return ("""
        \nIngredientes para la masa:
                250 g de harina
                125 g de mantequilla
                50 g de azúcar
                1 huevo
                1 pizca de sal""")

class Crear_masa():
    @staticmethod
    def pasos():
        return ("""
            \nPara la masa:
                1. Mezclar la harina, la mantequilla, el azúcar y la sal.
                2. Añadir el huevo y amasar.
                3. Dejar reposar la masa en la nevera durante 30 minutos.
                4. Estirar la masa y forrar el molde.
                5. Pinchar la masa con un tenedor y hornear durante 15 minutos a 180ºC.
                6. Dejar enfriar.""")
        
class CrearTartaVainilla(Builder,Crear_masa,IngredientesMassa): # Clase concreta que construye la tarta de vainilla.
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._tarta = TartaVainilla()

    @property
    def tarta(self) -> TartaVainilla:
        tarta = self._tarta
        self.reset()
        return tarta

    def ingredientes(self) -> None:
        self._tarta.add(IngredientesMassa.ingredientes()+"""
            \nIngredientes para el relleno:
                4 huevos
                200 g de azúcar
                500 ml de leche
                1 cucharada de vainilla
                1 cucharada de harina
                1 cucharada de mantequilla
                1 cucharada de azúcar glass""")
    
    def masa(self) -> None:
         self._tarta.add(self.pasos())

    def relleno(self) -> None:
        self._tarta.add("""
              \nPara el relleno:
                1. Batir los huevos con el azúcar.
                2. Añadir la leche y la nata.
                3. Añadir la vainilla.
                4. Verter el relleno sobre la masa.
                5. Hornear durante 40 minutos a 180ºC.
                6. Dejar enfriar.
                        """)

class CrearTartaCoco(Builder,Crear_masa,IngredientesMassa): # Clase concreta que construye la tarta de coco.
    
        def __init__(self) -> None:
            self.reset()
    
        def reset(self) -> None:
            self._tarta = TartaCoco()
    
        @property
        def tarta(self) -> TartaCoco:
            tarta = self._tarta
            self.reset()
            return tarta
    
        def ingredientes(self) -> None:
            self._tarta.add(IngredientesMassa.ingredientes()+"""
              \nIngredientes para el relleno:
                4 huevos
                200 g de azúcar
                500 ml de leche
                1 cucharada de vainilla
                1 cucharada de harina
                1 cucharada de mantequilla
                1 cucharada de azúcar glass""")
        
        def masa(self) -> None:
            self._tarta.add(self.pasos())
    
        def relleno(self) -> None:
            self._tarta.add("""
              \nPara el relleno:
                1. Batir los huevos con el azúcar.
                2. Añadir la leche y la nata.
                3. Añadir el coco.
                4. Verter el relleno sobre la masa.
                5. Hornear durante 40 minutos a 180ºC.
                6. Dejar enfriar.
                            """)
            
class TartaVainilla():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"""Tarta de vainilla:{''.join(self.parts)}""")

class TartaCoco():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"""Tarta de coco: {''.join(self.parts)}""")

builder = CrearTartaVainilla()
builder.ingredientes()
builder.masa()
builder.relleno()
builder.tarta.list_parts()
print("\n")
builder = CrearTartaCoco()
builder.ingredientes()
builder.masa()
builder.relleno()
builder.tarta.list_parts()     
