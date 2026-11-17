import re

# Importamos la clase abstracta Entidad
from .entidad import Entidad

# La clase Cliente hereda de Entidad
class Cliente(Entidad):

    # Constructor de la clase Cliente
    def __init__(self, identificador, nombre, documento, correo):

        # Llamamos al constructor de la clase padre
        super().__init__(identificador)

        # Inicializamos los atributos privados
        self._nombre = self._validar_nombre(nombre)
        self._documento = self._validar_documento(documento)
        self._correo = self._validar_correo(correo)

    # VALIDAR NOMBRE DEL CLIENTE
    
    def _validar_nombre(self, nombre):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        return nombre.strip()
    # VALIDAR DOCUMENTO
   
    def _validar_documento(self, documento):

        documento = str(documento).strip()

        if not documento.isdigit():
            raise ValueError("El documento debe contener números")

        if len(documento) < 5:
            raise ValueError("El documento debe tener mínimo 5 dígitos")

        return documento

    # VALIDAR CORREO ELECTRÓNICO
    
    def _validar_correo(self, correo):

        if not isinstance(correo, str):
            raise ValueError("El correo debe ser texto")

        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.match(patron, correo.strip()):
            raise ValueError("El correo no es válido")

        return correo.strip()

    # PROPIEDADES PARA CONSULTAR LOS ATRIBUTOS PRIVADOS
   
    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    @property
    def correo(self):
        return self._correo

    # IMPLEMENTACIÓN DEL MÉTODO ABSTRACTO DE ENTIDAD
   
    def mostrar_informacion(self):

        return (
            f"Identificador: {self._identificador}\n"
            f"Nombre: {self._nombre}\n"
            f"Documento: {self._documento}\n"
            f"Correo: {self._correo}"
        )

    # Representación del objeto como texto
    def __str__(self):

        return f"Cliente: {self._nombre} - Documento: {self._documento}"
