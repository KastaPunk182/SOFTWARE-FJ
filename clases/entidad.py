
# ABC permite crear clases abstractas
# abstractmethod permite definir métodos obligatorios
from abc import ABC, abstractmethod

# Clase abstracta que representa una entidad general
class Entidad(ABC):

    # Constructor de la clase
    def __init__(self, identificador):

        # Atributo protegido que identifica cada entidad
        self._identificador = identificador

    # Propiedad para consultar el identificador
    @property
    def identificador(self):
        return self._identificador

    # Método abstracto que deberán implementar
    # las clases que hereden de Entidad
    @abstractmethod
    def mostrar_informacion(self):
        pass
