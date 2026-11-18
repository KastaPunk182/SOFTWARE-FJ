# SOFTWARE-FJ

## Sistema Integral de Gestión de Clientes, Servicios y Reservas

### 1. Descripción del proyecto

Software FJ es una aplicación desarrollada en Python que permite gestionar clientes, servicios especializados y reservas de una empresa.

El proyecto utiliza programación orientada a objetos para organizar la información, validar los datos y controlar las operaciones del sistema.

### 2. Objetivo

Desarrollar un sistema que permita administrar clientes, servicios y reservas mediante clases, herencia, encapsulamiento, abstracción, polimorfismo y manejo de excepciones.

### 3. Funcionalidades principales

- Registro y validación de clientes.
- Validación de documentos y correos electrónicos.
- Control de clientes duplicados.
- Registro de servicios especializados.
- Validación de tarifas y parámetros.
- Creación, confirmación y cancelación de reservas.
- Procesamiento de reservas y cálculo de costos.
- Aplicación de impuestos y descuentos.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores mediante archivos LOG.

### 4. Estructura del proyecto

```text
SOFTWARE-FJ/
│
├── clases/
│   ├── __init__.py
│   ├── entidad.py
│   ├── clientes.py
│   ├── servicio.py
│   ├── reserva.py
│   └── gestion.py
│
├── logs/
│   ├── software_fj.log
│   └── reservas.log
│
├── main.py
└── README.md
```

### 5. Tecnologías utilizadas

- Python 3.11.9
- Visual Studio Code
- GitHub

Se utilizan bibliotecas estándar de Python como:
- abc
- re
- math
- logging
- pathlib
- datetime

### 6. Ejecución del programa

Para ejecutar el proyecto se deben seguir estos pasos:

1. Abrir la carpeta SOFTWARE-FJ en Visual Studio Code.
2. Abrir una terminal.
3. Verificar que Python esté instalado.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

### 7. Pruebas realizadas

Se implementaron diez operaciones de prueba para verificar el funcionamiento del sistema:

1. Registro de cliente válido.
2. Registro de cliente con correo inválido.
3. Intento de registro de cliente duplicado.
4. Creación de tres servicios válidos.
5. Intento de creación de servicio con tarifa negativa.
6. Creación de reserva válida.
7. Intento de procesar una reserva sin confirmar.
8. Confirmación y procesamiento de reserva.
9. Creación y cancelación de otra reserva.
10. Cálculos con impuestos y descuentos.

### 8. Registro de eventos y errores

El sistema utiliza el módulo logging de Python para almacenar información sobre las operaciones realizadas y los errores detectados.

Los registros se almacenan en la carpeta logs mediante los archivos:

- software_fj.log
- reservas.log

### 9. Autor

Proyecto académico desarrollado para la asignatura de Programación.

UNAD - Fase 4.
