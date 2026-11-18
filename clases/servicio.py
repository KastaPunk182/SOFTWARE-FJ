
# Importamos herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# Importamos math para validar valores numericos
import math

# CLASE ABSTRACTA SERVICIO
# Representa los servicios generales de la empresa


class Servicio(ABC):

    # Constructor de la clase
    def __init__(self, codigo, nombre, tarifa):

        # Validamos el codigo del servicio
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El codigo es obligatorio")

        # Validamos el nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio")

        # Validamos que la tarifa sea numerica y positiva
        if (
            isinstance(tarifa, bool)
            or not isinstance(tarifa, (int, float))
            or not math.isfinite(tarifa)
            or tarifa <= 0
        ):
            raise ValueError("La tarifa debe ser positiva")

        # Atributos encapsulados
        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._tarifa = tarifa

    # Propiedad para consultar el codigo
    @property
    def codigo(self):
        return self._codigo

    # METODO PARA CALCULAR COSTOS CON OPCIONES
    # Permite aplicar impuestos y descuentos
   

    def _aplicar_impuestos_descuentos(
        self, costo_base, impuesto=0, descuento=0
    ):

        # Validamos el porcentaje de impuesto
        if (
            isinstance(impuesto, bool)
            or not isinstance(impuesto, (int, float))
            or not math.isfinite(impuesto)
            or not 0 <= impuesto <= 100
        ):
            raise ValueError("El impuesto debe estar entre 0 y 100")

        # Validamos el porcentaje de descuento
        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
            or not math.isfinite(descuento)
            or not 0 <= descuento <= 100
        ):
            raise ValueError("El descuento debe estar entre 0 y 100")

        # Aplicamos primero el descuento
        valor_descuento = costo_base * (descuento / 100)

        subtotal = costo_base - valor_descuento

        # Aplicamos el impuesto al subtotal
        valor_impuesto = subtotal * (impuesto / 100)

        # Calculamos el costo final
        costo_total = subtotal + valor_impuesto

        return round(costo_total, 2)

    # Metodo abstracto para calcular el costo
    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
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

        # Inicializamos los atributos de la clase padre
        super().__init__(codigo, nombre, tarifa)

        # Validamos la capacidad de la sala
        if (
            isinstance(capacidad, bool)
            or not isinstance(capacidad, int)
            or capacidad <= 0
        ):
            raise ValueError("La capacidad debe ser positiva")

        self._capacidad = capacidad

    # Validamos la duracion de la reserva
    def validar_parametros(self, cantidad):

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, (int, float))
            or not math.isfinite(cantidad)
            or cantidad <= 0
        ):
            raise ValueError("Las horas deben ser mayores que cero")

        return True

    # Calculamos el costo con impuestos y descuentos opcionales
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):

        self.validar_parametros(cantidad)

        # Calculamos el costo inicial por horas
        costo_base = cantidad * self._tarifa

        # Aplicamos impuestos y descuentos
        return self._aplicar_impuestos_descuentos(
            costo_base, impuesto, descuento
        )

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

        # Validamos el nombre del equipo
        if not isinstance(equipo, str) or not equipo.strip():
            raise ValueError("Debe indicar el equipo")

        self._equipo = equipo.strip()

    # Validamos las horas de alquiler
    def validar_parametros(self, cantidad):

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, (int, float))
            or not math.isfinite(cantidad)
            or cantidad <= 0
        ):
            raise ValueError("Las horas deben ser positivas")

        return True

    # Calculamos el costo del alquiler
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):

        self.validar_parametros(cantidad)

        # Calculamos el costo inicial
        costo_base = cantidad * self._tarifa

        # Aplicamos impuestos y descuentos
        return self._aplicar_impuestos_descuentos(
            costo_base, impuesto, descuento
        )

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

        # Validamos la especialidad
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("Debe indicar una especialidad")

        self._especialidad = especialidad.strip()

    # Validamos las horas de asesoria
    def validar_parametros(self, cantidad):

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, (int, float))
            or not math.isfinite(cantidad)
            or cantidad <= 0
        ):
            raise ValueError("Las horas deben ser positivas")

        return True

    # Calculamos el costo de la asesoria
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):

        self.validar_parametros(cantidad)

        # Calculamos el costo inicial
        costo_base = cantidad * self._tarifa

        # Aplicamos impuestos y descuentos
        return self._aplicar_impuestos_descuentos(
            costo_base, impuesto, descuento
        )

    # Descripcion del servicio
    def describir_servicio(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Especialidad: {self._especialidad}\n"
            f"Tarifa por hora: ${self._tarifa}"
        )
