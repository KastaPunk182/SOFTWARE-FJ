# Este archivo identifica la carpeta clases como un paquete.
# Permite organizar e importar los diferentes modulos del sistema Software FJ.
# Paquete clases - Software FJ
# Sistema Integral de Gestión de Clientes, Servicios y Reservas

from .entidad import Entidad
from .clientes import Cliente
from .servicio import (
    Servicio,
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada,
)
from .reserva import (
    Reserva,
    ReservaInvalidaError,
    EstadoReservaError,
    ErrorProcesamientoReserva,
)
from .gestion import (
    GestionSistema,
    RegistroDuplicadoError,
)

__all__ = [
    "Entidad",
    "Cliente",
    "Servicio",
    "ReservaSala",
    "AlquilerEquipo",
    "AsesoriaEspecializada",
    "Reserva",
    "ReservaInvalidaError",
    "EstadoReservaError",
    "ErrorProcesamientoReserva",
    "GestionSistema",
    "RegistroDuplicadoError",
]
