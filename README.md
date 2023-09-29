# ProyectoPorygon

 Un intento de un algoritmo para resolver problemas por el método simplex.

Versión 0.6
## Cambios de la versión:
- Ahora puedes iniciar desde un archivo .csv o desde datos en una lista compuesta.
- Se han agregado excepciones para cuando se encuentre un dato no numerico
- Se ha integrado pretty print de sympy para la visualizacion correcta de las matrices resultantes.
- Se agregan nuevos parametros en las funciones:
- - Simbolico: True o False para usar matematicas simbolicas o usar decimales (respectivamente).
- - Numero de decimales: Indica el numero de decimales que se mostraran en las matrices impresas al no usar matematicas simbolicas.
- Ademas, estos parametros tienen valores por defecto.
- Se agregaron descripciones para cada funcion, de esta forma se ayuda a la legibilidad del programa.

## Futuros cambios:
- Creación de una interfaz.
- Almacenamiento e intercambio de las variables.
- Hacer modular todas las funciones, para así poder llamar una por una.


# INSTRUCCIONES:
* Descargar los archivos, puedes descargar todo el código dando click en Code y luego en Download ZIP.
* Guardar el archivo jordan.py en alguna carpeta, de preferencia en la misma carpeta donde se colocará el archivo que contenga la matriz a resolver.
* Crear un archivo nuevo, importar los módulos numpy, sympy y jordan:

>    import numpy

>    import sympy

>    import jordan

* * En caso de no tener numpy o sympy instalados, instalarlos con pip, en Windows simplemente debe correrse el siguiente comando en CMD:

>    py -m pip install numpy

>    py -m pip install sympy

* * En caso de estar trabajando con Anaconda, estos módulos deberían funcionar sin problema

### Iniciar desde archivo .csv.
* IMPORTANTE: El archivo debe seguir el formato del ejemplo, de la siguiente manera, donde ## son los coeficientes numericos.
>     ST , VAR1 , VAR2 , ... , VARN , ANS

>        ,  X1  ,  X2  , ... , VARN ,

>     Y1 ,  ##  ,  ##  , ... ,  ##  ,  ##

>     Y2 ,  ##  ,  ##  , ... ,  ##  ,  ##

>    ... ,  ..  ,  ..  , ... ,  ..  ,  ..

>     YN ,  ##  ,  ##  , ... ,  ##  ,  ##


* En caso de usar matematicas simbolicas: pueden colocarse enteros o fracciones, pero no puntos decimales ni simbolos
* En caso de trabajar con decimales: solo pueden colocarse numeros enteros o decimales, no simbolos ni fracciones
* Los parametros modificables son los siguientes:
* * Parametro 1: Indicar la ubicacion del archivo como un string.
* * * Si el archivo csv se encuentra en la misma carpeta que jordan.py, es tan facil como solo poner su nombre y extension (recuerda no usar espacios).
* * Parametro 2: True si quiere que se muestren todas las iteraciones, False para evitar eso.
* * Parametro 3: True si quiere usar matematicas simbolicas, False para trabajar con decimales.
* * Parametro 4: El numero de decimales que se mostraran en caso de trabajar con ellos.
* Se inicia como se muestra a continuacion:
>   jordan.iniciar_desde_csv(ubicacion = 'csvejemplo.csv' , mostrar_desarrollo = True, simbolico = False, numero_de_decimales = 3)

* Adicionalmente, si se quiere obtener cada iteración del programa, se coloca como segundo parámetro True (por defecto False).
* Una vez ejecutado el programa, se puede recuperar el resultado de la siguiente forma: 

>    resultado = jordan.resultado

### Iniciar desde datos en una lista compuesta.
* Crear la lista, esta contendra m sublistas, donde se colocaran los valores numericos.
* Recordar que cada sublista debe tener el mismo numero de elementos.
* Para iniciar se toman en cuenta los parametros anteriores y se inicia como se indica a continuacion:
>   mi_lista = [[-2,1,2],[-3,4,12],[0,1,6],[3,-1,6],[3,-1,21],[1,-1,5],[3,-6,0]]

>   jordan.iniciar_desde_listas(lista = mi_lista , mostrar_desarrollo = False, simbolico = True)

* Adicionalmente, si se quiere obtener cada iteración del programa, se coloca como segundo parámetro True (por defecto False).
* Una vez ejecutado el programa, se puede recuperar el resultado de la siguiente forma: 

>    resultado = jordan.resultado

### Crear la matriz por mi cuenta [ANTIGUO Y NO RECOMENDADO].

* Crear la matriz, esta puede ser con el metodo array de numpy o con matrix de sympy para el uso de matemáticas simbólicas. Se recomienda el siguiente procedimiento:
* * Crear las hileras de la matriz una por una, estas deben contener los coeficientes de cada variable en orden, tanto para las restricciones como para la función objetivo.
* * Si se elaboró un tableu, seguir ese formato. Recordar que se debe partir de un punto factible (última columna positiva).
* * Si se desean los resultados en decimales:
* * * Es importante agregar .0 al final de cada número, o su decimal correspondiente.
* * * Usar el array de numpy de la forma siguiente, donde "y1", "y2", ... corresponden a cada una de las hileras que contienen las restriciones, y "z" la función objetivo.

>   mi_matriz = numpy.array([y1,y2,...,z]) 

* * Si se desean los resultados en fracciones:
* * * Es importante que los datos estén contenidos como enteros, sin ningún decimal.  > /// Considerando corregir esto.
* * * Usar matrix de sympy de la siguiente forma: 

>    mi_matriz = sympy.matrix([y1,y2,...,z])

* Finalmente se inicia el programa con el comando 

>    jordan.iniciar(mi_matriz, False)

* Adicionalmente, si se quiere obtener cada iteración del programa, se coloca como segundo parámetro True (por defecto False).
* Una vez ejecutado el programa, se puede recuperar el resultado de la siguiente forma: 

>    resultado = jordan.resultado
