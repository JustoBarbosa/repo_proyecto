# repo\_proyecto

Behavior tracker
Justo Barbosa Moreira, Sol Collins, Uma Poggi, Victoria Azpeitia

Este programa esta hecho para procesar y analizar el comportamiento en distintas aplicaciones móviles. El sistema lee y estructura datos, calcula las métricas y representa el comportamiento en esta aplicaciones.



Manejo de errores:

Para evitar posibles errores en nuestro proyecto analizamos puntos de quiebre donde los datos podrían ser erróneos en su tipo, rango o directamente inexistentes. Para poder hacer un buen manejo de los mismos se aplicaron códigos de try-except que no solo ayudan a que fluya el programa sino que notifican el tipo de error que se llevó a cabo. En la función de "métricas" se buscaron evitar los errores de división por cero y cantidades negativas, en la función "procesamiento" se analizó la posibilidad que el id ingresado sea inexistente, y en las funciones de "cargar\_datos" y "validación" se analizaron posibles errores a la hora de encontrar el archivo, listas vacías y tipos de datos inválidos.

En el main la posibilidad de un error se encuentra al no encontrar el archivo o al errar en la operación que se aplica a esos datos ingresados. 

