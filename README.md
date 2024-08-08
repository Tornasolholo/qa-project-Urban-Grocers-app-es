PROYECTO APLICACIÓN “URBAN GROCERS” PARA COMPROBAR COMO LA APLICACIÓN CREA KITS DE PRODUCTOS.
El siguiente proyecto busca automatizar las pruebas desde la lista de comprobación, cargar el código en GitHub para el campo “name” en la solicitud de creación de kit de productos de la aplicación “URBAN GROCERS”.

ARCHIVOS GENERADOS EN PYCHARM
Configuration.py: Contiene las rutas del servidor y paths para el desarrollo del proyecto.
Data.py: Se encuentra el encabezado y cuerpo.
Create_kit_name_kit_test.py: En este archivo se almacena las funciones necesarias para enviar las solicitudes.
Sender_stand_reques.py: Por último, se tiene los parámetros para la creación de un kit según el campo “name”.

Pruebas que se deben comprobar
1.	Prueba 1: El número permitido de caracteres (1).
2.	Prueba 2: El número permitido de caracteres (511).
3.	Prueba 3: El número permitido de caracteres es menor que la cantidad permitida (0).
4.	Prueba 4: El número de caracteres es mayor que la cantidad permitida (512).
5.	Prueba 5: Se permites caracteres especiales (*/-@ñ).
6.	Prueba 6: Se permiten espacios “A aaa”.
7.	Prueba 7: Se permiten números “123”
8.	Prueba 8: El parámetro no se pasa en la solicitud.
9.	Prueba 9: Se ha pasado un tipo de parámetro diferente (número): 123.

Para desarrollar el proyecto se usará la Pycharm y Github mediante un commit.
