
# Importamos herramientas necesarias
import logging
from pathlib import Path
from datetime import datetime
import math

# CONFIGURACION DEL REGISTRO DE EVENTOS Y ERRORES

# Creamos la ruta de la carpeta logs en el proyecto
RUTA_LOGS = Path(__file__).resolve().parent.parent / "logs"

# Si la carpeta no existe, la creamos automaticamente
RUTA_LOGS.mkdir(parents=True, exist_ok=True)

# Configuramos el archivo donde se guardaran los registros
logger = logging.getLogger("SoftwareFJ.Reservas")
logger.setLevel(logging.INFO)

# Evitamos crear varios registros iguales
if not logger.handlers:

    manejador = logging.FileHandler(
        RUTA_LOGS / "reservas.log",
        encoding="utf-8"
    )

    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    manejador.setFormatter(formato)
    logger.addHandler(manejador)

# EXCEPCIONES PERSONALIZADAS
# Permiten identificar errores especificos del sistema

class ReservaInvalidaError(Exception):
    """Error cuando los datos de una reserva son incorrectos."""
    pass

class EstadoReservaError(Exception):
    """Error cuando se intenta realizar una operacion no permitida."""
    pass

class ErrorProcesamientoReserva(Exception):
    """Error cuando ocurre un problema al procesar una reserva."""
    pass

# CLASE RESERVA
# Gestiona la relacion entre cliente y servicio

class Reserva:

    # Constructor de la clase Reserva
    def __init__(self, codigo, cliente, servicio, duracion):

        # Validamos el codigo de la reserva
        if not isinstance(codigo, str) or not codigo.strip():
            raise ReservaInvalidaError(
                "El codigo de la reserva es obligatorio"
            )

        # Validamos que exista un cliente valido
        if not callable(getattr(cliente, "mostrar_informacion", None)):
            raise ReservaInvalidaError(
                "El cliente no es valido"
            )

        # Validamos que el servicio tenga los metodos necesarios
        if not callable(getattr(servicio, "calcular_costo", None)):
            raise ReservaInvalidaError(
                "El servicio no permite calcular costos"
            )

        if not callable(getattr(servicio, "describir_servicio", None)):
            raise ReservaInvalidaError(
                "El servicio no permite mostrar su descripcion"
            )

        # Validamos la duracion
        self._validar_duracion(duracion)

        # Guardamos los datos de la reserva
        self._codigo = codigo.strip()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion

        # Toda reserva comienza en estado pendiente
        self._estado = "PENDIENTE"

        # Inicializamos el costo
        self._costo = None

        # Registramos la creacion de la reserva
        logger.info(
            f"Reserva {self._codigo} creada correctamente"
        )

    # VALIDAR DURACION
    # Comprueba que la duracion sea un numero positivo
    #--------------------------------------------------
    def _validar_duracion(self, duracion):

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ReservaInvalidaError(
                "La duracion debe ser un numero positivo"
            )

    # PROPIEDADES PARA CONSULTAR LOS DATOS
    @property
    def codigo(self):
        return self._codigo

    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    # CONFIRMAR RESERVA
    # Cambia el estado de pendiente a confirmada
    #--------------------------------------------------
    def confirmar(self):

        if self._estado != "PENDIENTE":
            raise EstadoReservaError(
                "Solo se pueden confirmar reservas pendientes"
            )

        self._estado = "CONFIRMADA"

        logger.info(
            f"Reserva {self._codigo} confirmada"
        )

        return True

    # CANCELAR RESERVA
    # Permite cancelar reservas pendientes o confirmadas
    def cancelar(self):

        if self._estado not in ("PENDIENTE", "CONFIRMADA"):
            raise EstadoReservaError(
                "La reserva no se puede cancelar en su estado actual"
            )

        self._estado = "CANCELADA"

        logger.info(
            f"Reserva {self._codigo} cancelada"
        )

        return True

    # PROCESAR RESERVA
    # Calcula el costo utilizando el servicio seleccionado
    # ----------------------------------------------------

    def procesar(self):

        try:

            # Verificamos que la reserva este confirmada
            if self._estado != "CONFIRMADA":
                raise EstadoReservaError(
                    "La reserva debe estar confirmada para procesarse"
                )

            # Calculamos el costo mediante el servicio
            costo_calculado = self._servicio.calcular_costo(
                self._duracion
            )

            # Comprobamos que el resultado sea valido
            if (
                isinstance(costo_calculado, bool)
                or not isinstance(costo_calculado, (int, float))
                or not math.isfinite(costo_calculado)
                or costo_calculado < 0
            ):
                raise ValueError(
                    "El costo calculado no es valido"
                )

            # Guardamos el costo y actualizamos el estado
            self._costo = costo_calculado
            self._estado = "PROCESADA"

            logger.info(
                f"Reserva {self._codigo} procesada. "
                f"Costo: ${self._costo}"
            )

            return self._costo

        except Exception as error:

            # Registramos el error en el archivo de logs
            logger.exception(
                f"Error al procesar reserva {self._codigo}"
            )

            # Encadenamos la excepcion original
            raise ErrorProcesamientoReserva(
                f"No fue posible procesar la reserva {self._codigo}"
            ) from error

   
    # MOSTRAR INFORMACION DE LA RESERVA
    # Devuelve los datos principales de la reserva
    # ------------------------------------------------------

    def mostrar_informacion(self):

        informacion = (
            f"Codigo: {self._codigo}\n"
            f"Estado: {self._estado}\n"
            f"Duracion: {self._duracion} horas\n"
            f"Cliente:\n{self._cliente.mostrar_informacion()}\n"
            f"Servicio:\n{self._servicio.describir_servicio()}"
        )

        if self._costo is not None:
            informacion += f"\nCosto total: ${self._costo}"

        return informacion

    # Representacion de la reserva como texto
    def __str__(self):

        return (
            f"Reserva {self._codigo} - "
            f"Estado: {self._estado}"
        )
