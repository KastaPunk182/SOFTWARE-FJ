#Proyecto: Software FJ
#Sistema Integral de Gestión de Clientes,
#Servicios y Reservas.
#Curso: Programación 213023_518
#Carlos Arturo Castañeda Perez 1030534737
#UNAD - Fase 4


# Importamos las herramientas necesarias
import logging
from pathlib import Path

# Importamos las clases del proyecto
from clases.clientes import Cliente
from clases.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from clases.reserva import Reserva
from clases.gestion import GestionSistema


# CONFIGURACION DEL ARCHIVO DE REGISTRO


# Creamos la carpeta logs en la raiz del proyecto
RUTA_LOGS = Path(__file__).resolve().parent / "logs"
RUTA_LOGS.mkdir(exist_ok=True)

# Configuramos el archivo general de eventos y errores
logging.basicConfig(
    filename=RUTA_LOGS / "software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)

# Creamos el registrador principal
logger = logging.getLogger("SoftwareFJ.Main")


# FUNCION PARA EJECUTAR OPERACIONES
# Utiliza try, except, else y finally

def ejecutar_operacion(numero, descripcion, funcion):

    print("\n" + "=" * 60)
    print(f"OPERACION {numero}: {descripcion}")
    print("=" * 60)

    try:

        # Ejecutamos la operacion solicitada
        resultado = funcion()

    except Exception as error:

        # Capturamos cualquier error sin detener el programa
        print(f"ERROR CONTROLADO: {error}")

        # Registramos el error en el archivo de logs
        logger.exception(
            f"Error en la operacion {numero}: {descripcion}"
        )

    else:

        # Se ejecuta cuando no ocurre ninguna excepcion
        print("OPERACION REALIZADA CORRECTAMENTE")

        if resultado is not None:
            print(resultado)

        logger.info(
            f"Operacion {numero} realizada: {descripcion}"
        )

    finally:

        # Se ejecuta siempre, haya error o no
        print(f"Finalizacion de operacion {numero}")


# FUNCION PRINCIPAL DEL SISTEMA

def iniciar_sistema():

    print("\n")
    print("*" * 60)
    print("          SISTEMA INTEGRAL SOFTWARE FJ")
    print("     GESTION DE CLIENTES, SERVICIOS Y RESERVAS")
    print("*" * 60)

    # Creamos el administrador general del sistema
    sistema = GestionSistema()

    # Listas auxiliares para las pruebas
    clientes = []
    servicios = []
    reservas = []

    
    # OPERACION 1: REGISTRAR CLIENTE VALIDO
    

    def prueba_cliente_valido():

        cliente = Cliente(
            "C001",
            "Carlos Ramirez",
            "12345678",
            "carlos@email.com"
        )

        sistema.registrar_cliente(cliente)
        clientes.append(cliente)

        return cliente.mostrar_informacion()

    ejecutar_operacion(
        1,
        "Registro de cliente valido",
        prueba_cliente_valido
    )

    
    # OPERACION 2: INTENTAR REGISTRAR CLIENTE INVALIDO
   

    def prueba_cliente_invalido():

        cliente = Cliente(
            "C002",
            "Juan Perez",
            "87654321",
            "correo_incorrecto"
        )

        sistema.registrar_cliente(cliente)

    ejecutar_operacion(
        2,
        "Registro de cliente con correo invalido",
        prueba_cliente_invalido
    )

    
    # OPERACION 3: INTENTAR REGISTRAR CLIENTE DUPLICADO
   

    def prueba_cliente_duplicado():

        sistema.registrar_cliente(clientes[0])

    ejecutar_operacion(
        3,
        "Intento de registro de cliente duplicado",
        prueba_cliente_duplicado
    )

    
    # OPERACION 4: CREAR Y REGISTRAR SERVICIOS VALIDOS
    

    def prueba_servicios_validos():

        sala = ReservaSala(
            "S001",
            "Sala de reuniones",
            100000,
            20
        )

        equipo = AlquilerEquipo(
            "S002",
            "Alquiler de proyector",
            50000,
            "Proyector"
        )

        asesoria = AsesoriaEspecializada(
            "S003",
            "Asesoria de redes",
            80000,
            "Telecomunicaciones"
        )

        # Registramos los tres servicios
        for servicio in [sala, equipo, asesoria]:

            sistema.registrar_servicio(servicio)
            servicios.append(servicio)

        return "Se registraron los tres servicios especializados"

    ejecutar_operacion(
        4,
        "Creacion de tres servicios validos",
        prueba_servicios_validos
    )

    
    # OPERACION 5: CREAR SERVICIO INCORRECTO
    

    def prueba_servicio_invalido():

        servicio = ReservaSala(
            "S004",
            "Sala incorrecta",
            -50000,
            15
        )

        sistema.registrar_servicio(servicio)

    ejecutar_operacion(
        5,
        "Intento de creacion de servicio con tarifa negativa",
        prueba_servicio_invalido
    )

    
    # OPERACION 6: CREAR Y REGISTRAR RESERVA
    

    def prueba_crear_reserva():

        reserva = Reserva(
            "R001",
            clientes[0],
            servicios[0],
            2
        )

        sistema.registrar_reserva(reserva)
        reservas.append(reserva)

        return reserva.mostrar_informacion()

    ejecutar_operacion(
        6,
        "Creacion de reserva valida",
        prueba_crear_reserva
    )

    
    # OPERACION 7: INTENTAR PROCESAR RESERVA PENDIENTE
    

    def prueba_reserva_sin_confirmar():

        # La reserva todavia esta pendiente
        # Por eso no debe permitir su procesamiento
        return reservas[0].procesar()

    ejecutar_operacion(
        7,
        "Intento de procesar reserva sin confirmar",
        prueba_reserva_sin_confirmar
    )

    
    # OPERACION 8: CONFIRMAR Y PROCESAR RESERVA
    

    def prueba_confirmar_reserva():

        reservas[0].confirmar()

        costo = reservas[0].procesar()

        return f"Costo final de la reserva: ${costo:,.2f}"

    ejecutar_operacion(
        8,
        "Confirmacion y procesamiento de reserva",
        prueba_confirmar_reserva
    )

    
    # OPERACION 9: CREAR Y CANCELAR OTRA RESERVA
    

    def prueba_cancelar_reserva():

        reserva = Reserva(
            "R002",
            clientes[0],
            servicios[1],
            3
        )

        sistema.registrar_reserva(reserva)
        reservas.append(reserva)

        reserva.cancelar()

        return f"Estado de la reserva: {reserva.estado}"

    ejecutar_operacion(
        9,
        "Creacion y cancelacion de reserva",
        prueba_cancelar_reserva
    )

    
    # OPERACION 10: CALCULAR COSTOS CON DIFERENTES OPCIONES
    

    def prueba_calculos():

        servicio = servicios[0]

        # Calculo normal
        costo_normal = servicio.calcular_costo(2)

        # Calculo con impuesto del 19%
        costo_impuesto = servicio.calcular_costo(
            2,
            impuesto=19
        )

        # Calculo con descuento del 10%
        costo_descuento = servicio.calcular_costo(
            2,
            descuento=10
        )

        # Calculo con impuesto y descuento
        costo_completo = servicio.calcular_costo(
            2,
            impuesto=19,
            descuento=10
        )

        return (
            f"Costo normal: ${costo_normal:,.2f}\n"
            f"Costo con impuesto: ${costo_impuesto:,.2f}\n"
            f"Costo con descuento: ${costo_descuento:,.2f}\n"
            f"Costo con impuesto y descuento: "
            f"${costo_completo:,.2f}"
        )

    ejecutar_operacion(
        10,
        "Calculos con impuestos y descuentos",
        prueba_calculos
    )

    
    # RESUMEN GENERAL DEL SISTEMA
    

    print("\n")
    print("*" * 60)
    print("              RESUMEN FINAL SOFTWARE FJ")
    print("*" * 60)

    print(sistema.mostrar_resumen())

    print("\nDETALLE DE LAS RESERVAS:")

    for reserva in sistema.consultar_reservas():

        print("\n" + reserva.mostrar_informacion())

    print("\n")
    print("El sistema finalizo sus pruebas correctamente.")
    print("Los errores detectados fueron controlados.")
    print("Los registros se encuentran en la carpeta logs.")
    print("*" * 60)


# PUNTO DE ENTRADA DEL PROGRAMA
# Ejecuta el sistema cuando se inicia main.py

if __name__ == "__main__":

    try:

        iniciar_sistema()

    except Exception as error:

        # Capturamos errores generales no previstos
        logger.exception("Error general del sistema")

        print(f"Error general controlado: {error}")

    finally:

        print("\nEjecucion del programa finalizada.")
