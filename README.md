# repo\_proyecto

Behavior tracker
Justo Barbosa Moreira, Sol Collins, Uma Poggi, Victoria Azpeitia

Este programa esta hecho para procesar y analizar el comportamiento en distintas aplicaciones móviles. El sistema lee y estructura datos, calcula las métricas y representa el comportamiento en esta aplicaciones.



Manejo de errores:

Para evitar posibles errores en nuestro proyecto analizamos puntos de quiebre donde los datos podrían ser erróneos en su tipo, rango o directamente inexistentes. Para poder hacer un buen manejo de los mismos se aplicaron códigos de try-except que no solo ayudan a que fluya el programa sino que notifican el tipo de error que se llevó a cabo. En la función de "métricas" se buscaron evitar los errores de división por cero y cantidades negativas, en la función "procesamiento" se analizó la posibilidad que el id ingresado sea inexistente, y en las funciones de "cargar\_datos" y "validación" se analizaron posibles errores a la hora de encontrar el archivo, listas vacías y tipos de datos inválidos.

En el main la posibilidad de un error se encuentra al no encontrar el archivo o al errar en la operación que se aplica a esos datos ingresados.



Objetos:

En nuestro trabajo se podrían aplicar objetos en diferentes partes, como lo son:

* Las funciones de parsear\_datos y cargar\_datos: ambas funciones utilizadas en el mismo archivo de phyton utilizan mismas variables que se repiten en cada uno de los try para poder evaluar esos datos y formar la base de lo que se analizan en las posterior funciones. En este caso se podría crear una clase que involucre ambas funciones y un init que defina estos datos que se repiten a lo largo de ambas funciones. Es decir, en el archivo "cargar\_datos.py" se va a incluir una clase que sea datos, donde se definen los datos repetidos y se los llama con la ayuda del self. Los métodos utilizados son los ya creados y definidos como parsear\_datos y cargar\_datos.
* En validación\_datos.py: se definen los datos obtenidos del archivo pero la repetición se da a lo largo de todo el manejo de errores, podría verse facilitado con la aplicación de objetos. La clase podría definir las variables y luego aplicar como método a la función de "validar\_registro" que involucra condicionales y ciclos definidos para el manejo de errores.



Pandas:

El uso de pandas podría darse al incorporar archivos de tipo DataFrame que incluyan los datos posibles para poder llevar a cabo este proyecto. 

* Primero que nada se aplicaría en el main una entrada donde no se acceda a archivos separados sino mas bien a uno que obtenga todos los datos necesarios y luego a partir del llamado de las diferentes funciones se modifique el DataFrame para manipular las series y acceder a los datos.  
* En el caso del archivo de cargar\_datos.py que incluye las funciones de cargar\_datos y parsear\_datos en vez de separar los datos del archivo se podría llamar a las series donde se incluyan los datos y se podría acceder mediante los métodos loc e iloc para su llamado o manipulación. 
* Luego en el caso en los que se calculan promedios y tiempos totales hay datos a los que se puede acceder más fácilmente con el uso de series o en el caso de necesitar datos específicos se puede usar el método de filtrado donde el llamado a una serie de datos se le aplica un condicional que excluye esos datos que no cumplen (se pueden usar métodos como .isin(), .count(), .mean(), y muchos más). 

