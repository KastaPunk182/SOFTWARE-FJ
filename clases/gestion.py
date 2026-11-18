
# Importamos las clases necesarias
from .clientes import Cliente
from .servicio import Servicio
from .reserva import Reserva

# Importamos el sistema de registro de eventos
import logging


# Configuramos el registro de eventos
logger = logging.getLogger("SoftwareFJ.Gestion")

# EXCEPCION PERSONALIZADA
# Se utiliza cuando existen registros duplicados

class RegistroDuplicadoError(Exception):
    pass

# CLASE GESTION DEL SISTEMA
# Administra clientes, servicios y reservas

class GestionSistema:

    # Constructor de la clase
    def __init__(self):

        # Listas internas para almacenar los registros
        self._clientes = []
        self._servicios = []
        self._reservas = []

        logger.info("Sistema de gestion inicializado")

    
    # REGISTRAR CLIENTE
    # Agrega un cliente a la lista interna
    

    def registrar_cliente(self, cliente):

        # Comprobamos que sea un objeto de tipo Cliente
        if not isinstance(cliente, Cliente):
            raise TypeError("El registro debe ser un objeto Cliente")

        # Comprobamos que el documento no este repetido
        for registrado in self._clientes:

            if registrado.documento == cliente.documento:
                raise RegistroDuplicadoError(
                    "Ya existe un cliente con ese documento"
                )

        # Agregamos el cliente a la lista
        self._clientes.append(cliente)

        logger.info(
            f"Cliente registrado: {cliente.documento}"
        )

        return True

    
    # REGISTRAR SERVICIO
    # Agrega un servicio a la lista interna
    

    def registrar_servicio(self, servicio):

        # Verificamos que sea un servicio valido
        if not isinstance(servicio, Servicio):
            raise TypeError("El objeto debe ser un Servicio valido")

        # Evitamos codigos de servicio duplicados
        for registrado in self._servicios:

            if registrado.codigo == servicio.codigo:
                raise RegistroDuplicadoError(
                    "Ya existe un servicio con ese codigo"
                )

        # Guardamos el servicio
        self._servicios.append(servicio)

        logger.info(
            f"Servicio registrado: {servicio.codigo}"
        )

        return True

    
    # REGISTRAR RESERVA
    # Agrega una reserva a la lista interna
    
    def registrar_reserva(self, reserva):

        # Verificamos que sea una reserva valida
        if not isinstance(reserva, Reserva):
            raise TypeError("El objeto debe ser una Reserva valida")

        # Evitamos codigos de reserva repetidos
        for registrada in self._reservas:

            if registrada.codigo == reserva.codigo:
                raise RegistroDuplicadoError(
                    "Ya existe una reserva con ese codigo"
                )

        # Guardamos la reserva
        self._reservas.append(reserva)

        logger.info(
            f"Reserva registrada: {reserva.codigo}"
        )

        return True

    
    # CONSULTAR CLIENTES
    # Devuelve una copia de la lista de clientes
    
    def consultar_clientes(self):

        return self._clientes.copy()

    
    # CONSULTAR SERVICIOS
    # Devuelve una copia de la lista de servicios
    

    def consultar_servicios(self):

        return self._servicios.copy()

   
    # CONSULTAR RESERVAS
    # Devuelve una copia de la lista de reservas
    
    def consultar_reservas(self):

        return self._reservas.copy()

    
    # MOSTRAR RESUMEN DEL SISTEMA
    # Indica la cantidad de registros almacenados
    

    def mostrar_resumen(self):

        return (
            "\n========== RESUMEN SOFTWARE FJ ==========\n"
            f"Total de clientes: {len(self._clientes)}\n"
            f"Total de servicios: {len(self._servicios)}\n"
            f"Total de reservas: {len(self._reservas)}\n"
            "========================================="
        )
