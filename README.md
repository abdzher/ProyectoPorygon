# ProyectoPorygon

 Un intento de un algoritmo para resolver problemas por el método simplex.

Versión 0.5
## Cambios de la versión:
- Se agregan las dimensiones de la matriz como entidades de las funciones, por lo tanto se puede llamar como un modulo.
- Se agregan mas comentarios para mejor entendimiento.
- Se agrega la opcion de mostrar cada iteracion.

## Futuros cambios:
- Integracion de sympy para el manejo de resultados fraccionarios.
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
