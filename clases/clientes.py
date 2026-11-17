
# ==========================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: cliente.py
# DESCRIPCIÓN: Clase encargada de gestionar los clientes.

# Importamos re para realizar validaciones de texto
import re

# Creamos una clase Cliente
class Cliente:

    # Constructor: se ejecuta cuando creamos un nuevo cliente
    def __init__(self, nombre, documento, correo):

        # Atributos privados (encapsulación)
        # El guion bajo indica que estos datos son internos
        self._nombre = self._validar_nombre(nombre)
        self._documento = self._validar_documento(documento)
        self._correo = self._validar_correo(correo)

   
    # MÉTODO PARA VALIDAR EL NOMBRE
    # Comprueba que el nombre no esté vacío
   
    def _validar_nombre(self, nombre):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        return nombre.strip()

    # MÉTODO PARA VALIDAR EL DOCUMENTO
    # Comprueba que el documento contenga solamente números
    
    def _validar_documento(self, documento):

        documento = str(documento).strip()

        if not documento.isdigit():
            raise ValueError("El documento debe contener solo números")

        if len(documento) < 5:
            raise ValueError("El documento debe tener mínimo 5 dígitos")

        return documento

    # MÉTODO PARA VALIDAR EL CORREO
    # Comprueba que tenga un formato básico de correo
    
    def _validar_correo(self, correo):

        if not isinstance(correo, str):
            raise ValueError("El correo debe ser texto")

        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.match(patron, correo.strip()):
            raise ValueError("El correo electrónico no es válido")

        return correo.strip()

    # PROPIEDADES (GETTERS)
    # Permiten consultar los atributos privados

    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    @property
    def correo(self):
        return self._correo

   
    # MÉTODO PARA MOSTRAR LA INFORMACIÓN DEL CLIENTE
    # Devuelve los datos registrados
   
    def mostrar_informacion(self):

        return (
            f"Nombre: {self._nombre}\n"
            f"Documento: {self._documento}\n"
            f"Correo: {self._correo}"
        )

    # Método especial para representar el objeto como texto
    def __str__(self):
        return f"Cliente: {self._nombre} - Documento: {self._documento}"
