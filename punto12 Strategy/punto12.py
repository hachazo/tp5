# Patrón Strategy.
# En una plataforma de streaming de películas se desea consultar el catálogo. Sin
# embargo hay diferentes situaciones que podrían llevar a qué el sea filtrado de diferentes
# formas, un ejemplo de ello es cuando la cuenta que está usando el sistema pertenece a
# un niño. En este caso el catálogo solo debe mostrar películas que no sean para
# mayores de 13 años.
# Utilizando el patrón strategy defina una estrategia general que retorne el catálogo
# completo y luego una estrategia para niños que filtra las películas por edad.
# Escriba en consola el listado implementando la estrategia para todo el catálogo. Luego
# imprima el listado usando la estrategia para menores de 13.
# Finalmente, implemente una tercera estrategia que retorne el catálogo de películas para
# menores de 18 años. Compruebe el resultado en consola.

from __future__ import annotations
from abc import ABC, abstractmethod

class Catalogo:
    def __init__(self, nombre: str, clasificacion: int) -> None:
        self._nombre = nombre
        self._clasificacion = clasificacion
        
class Streaming():
    def __init__(self,metodo_filtar: Filtrar) -> None:
        self.__filtar = metodo_filtar
    
    @property
    def filtrar(self) -> Filtrar:
        return self.__filtar
    
    @filtrar.setter
    def filtrar(self, metodo_filtar: Filtrar) -> None:
        self.__filtar = metodo_filtar
        
    def filtrar(self, catalogo: Catalogo) -> None:
        self.__filtar.filtrar(catalogo)

class Filtrar(ABC):
    @abstractmethod
    def filtrar(self, catalogo: Catalogo) -> None:
        pass
    
class Menores_13:
    def filtrar(self, catalogo: Catalogo) -> None:
        if catalogo._clasificacion <= 13:
            print(catalogo._nombre)
            
class Mayores_13:
    def filtrar(self, catalogo: Catalogo) -> None:
        if catalogo._clasificacion > 13:
            print(catalogo._nombre)
            
peliculas_series = []

peliculas_series.append(Catalogo("El señor de los anillos", 18))
peliculas_series.append(Catalogo("star wars", 13))
peliculas_series.append(Catalogo("Harry Potter", 13))
peliculas_series.append(Catalogo("Los Simpson", 13))

filtrar = Streaming(Menores_13())

for i in peliculas_series:
    filtrar.filtrar(i)
