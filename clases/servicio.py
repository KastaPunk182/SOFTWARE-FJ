
# Importamos herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# CLASE ABSTRACTA SERVICIO
# Representa los servicios generales de la empresa

class Servicio(ABC):

    def __init__(self, codigo, nombre, tarifa):

        # Validamos que el codigo sea un texto
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El codigo del servicio es obligatorio")

        # Validamos que la tarifa sea numerica y positiva
        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)):
            raise ValueError("La tarifa debe ser numerica")

        if tarifa <= 0:
            raise ValueError("La tarifa debe ser mayor que cero")

        # Atributos encapsulados
        self._codigo = codigo.strip()
        self._nombre = nombre
        self._tarifa = tarifa

    # Propiedad para consultar el codigo
    @property
    def codigo(self):
        return self._codigo

    # Metodo abstracto para calcular el costo
    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    # Metodo abstracto para describir el servicio
    @abstractmethod
    def describir_servicio(self):
        pass

    # Metodo abstracto para validar parametros
    @abstractmethod
    def validar_parametros(self, cantidad):
        pass

# SERVICIO 1: RESERVA DE SALAS

class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, tarifa, capacidad):

        super().__init__(codigo, nombre, tarifa)

        # Capacidad maxima de personas de la sala
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo")

        self._capacidad = capacidad

    # Validamos la duracion de la reserva
    def validar_parametros(self, cantidad):

        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValueError("Las horas deben ser mayores que cero")

        return True

    # Calculamos el costo por horas de reserva
    def calcular_costo(self, cantidad):

        self.validar_parametros(cantidad)

        return cantidad * self._tarifa

    # Descripcion del servicio
    def describir_servicio(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Capacidad: {self._capacidad} personas\n"
            f"Tarifa por hora: ${self._tarifa}"
        )

# SERVICIO 2: ALQUILER DE EQUIPOS

class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, tarifa, equipo):

        super().__init__(codigo, nombre, tarifa)

        # Nombre del equipo que se va a alquilar
        if not isinstance(equipo, str) or not equipo.strip():
            raise ValueError("Debe indicar el equipo")

        self._equipo = equipo.strip()

    # Validamos las horas de alquiler
    def validar_parametros(self, cantidad):

        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValueError("Las horas de alquiler deben ser positivas")

        return True

    # Calculamos el costo del alquiler
    def calcular_costo(self, cantidad):

        self.validar_parametros(cantidad)

        return cantidad * self._tarifa

    # Descripcion del servicio
    def describir_servicio(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Equipo: {self._equipo}\n"
            f"Tarifa por hora: ${self._tarifa}"
        )


# SERVICIO 3: ASESORIAS ESPECIALIZADAS

class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, tarifa, especialidad):

        super().__init__(codigo, nombre, tarifa)

        # Especialidad de la asesoria
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("Debe indicar una especialidad")

        self._especialidad = especialidad.strip()

    # Validamos la duracion de la asesoria
    def validar_parametros(self, cantidad):

        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValueError("Las horas de asesoria deben ser positivas")

        return True

    # Calculamos el costo de la asesoria
    def calcular_costo(self, cantidad):

        self.validar_parametros(cantidad)

        return cantidad * self._tarifa

    # Descripcion del servicio
    def describir_servicio(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Especialidad: {self._especialidad}\n"
            f"Tarifa por hora: ${self._tarifa}"
        )
