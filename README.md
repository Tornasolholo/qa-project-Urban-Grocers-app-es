Nombre: Angela Macias Vera
Cohort: 12

PROYECTO APLICACIÓN “URBAN GROCERS” PARA COMPROBAR COMO LA APLICACIÓN CREA KITS DE PRODUCTOS.
El siguiente proyecto busca automatizar las pruebas desde la lista de comprobación, cargar el código en GitHub para el campo “name” en la solicitud de creación de kit de productos de la aplicación “URBAN GROCERS”.

ARCHIVOS GENERADOS EN PYCHARM
Configuration.py: Contiene las rutas del servidor y paths para el desarrollo del proyecto.
Data.py: Se encuentra el encabezado y cuerpo.
Create_kit_name_kit_test.py: En este archivo se almacena las funciones necesarias para enviar las solicitudes.
Sender_stand_reques.py: Por último, se tiene los parámetros para la creación de un kit según el campo “name”.

PRUEBAS QUE SE DEBEN COMPROBAR
1.	Prueba 1: El número permitido de caracteres (1).
2.	Prueba 2: El número permitido de caracteres (511).
3.	Prueba 3: El número permitido de caracteres es menor que la cantidad permitida (0).
4.	Prueba 4: El número de caracteres es mayor que la cantidad permitida (512).
5.	Prueba 5: Se permites caracteres especiales (*/-@ñ).
6.	Prueba 6: Se permiten espacios “A aaa”.
7.	Prueba 7: Se permiten números “123”
8.	Prueba 8: El parámetro no se pasa en la solicitud.
9.	Prueba 9: Se ha pasado un tipo de parámetro diferente (número): 123.

DESCRIPCION DE LAS TECNOLOGÍAS USADAS
Para desarrollar el proyecto se usará la Pycharm y Github mediante un commit.
Python: Lenguaje de programación principal utilizado para el desarrollo del proyecto y la escritura de pruebas automatizadas.
Requests: Biblioteca de Python para realizar solicitudes HTTP. Se utiliza en sender_stand_request.py para enviar solicitudes a la API de la aplicación "Urban Grocers".
PyCharm: Entorno de desarrollo integrado (IDE) utilizado para el desarrollo del proyecto.
GitHub: Plataforma de control de versiones donde se almacena el código fuente del proyecto y se realiza el seguimiento de los cambios.
JSON: Formato de intercambio de datos utilizado para enviar y recibir datos entre la aplicación y la API.

INSTRUCCIONES PARA EJECUTAR LAS PRUBAS DEL SIGUIENTE PROYECTO: 
Para ejecutar las pruebas del proyecto, sigue estos pasos:
Configuración del Entorno de Desarrollo:
1 - Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org. Instala la biblioteca requests utilizando pip si no lo has hecho ya
2 - Clonar el Repositorio: Clona el repositorio del proyecto desde GitHub a tu máquina local. Utiliza el siguiente comando (reemplaza <URL_DEL_REPOSITORIO> con la URL del repositorio)
3 - Revisar Archivos de Configuración: Asegúrate de que los archivos de configuración (configuration.py, data.py, sender_stand_request.py, Create_kit_name_kit_test.py) estén correctamente configurados. Verifica que URL_SERVICE en configuration.py apunte a la URL correcta del servicio de la API.
4 - Ejecutar las Pruebas: Navega al directorio donde se encuentran los archivos del proyecto. Ejecuta las pruebas utilizando un marco de pruebas como pytest. Asegúrate de tener pytest instalado. Puedes instalarlo con pip si es necesario.
5 - Verificar Resultados: Revisa los resultados de las pruebas en la terminal o consola. pytest mostrará un resumen de las pruebas que pasaron y las que fallaron.
Asegúrate de que todas las pruebas se ejecuten correctamente y verifica cualquier mensaje de error o advertencia.
