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
1. Descargar los archivos, puedes descargar todo el código dando click en Code y luego en Download ZIP.
2. Guardar el archivo jordan.py en alguna carpeta, de preferencia en la misma carpeta donde se colocará el archivo que contenga la matriz a resolver.
3. Crear un archivo nuevo, importar los módulos numpy, sympy y jordan:
        import numpy
        import sympy
        import jordan
    3.1. En caso de no tener numpy o sympy instalados, instalarlos con pip, en Windows simplemente debe correrse el siguiente comando en CMD:
        py -m pip install numpy
        py -m pip install sympy
    3.2. En caso de estar trabajando con Anaconda, estos módulos deberían funcionar sin problema
4. Crear la matriz, esta puede ser con el metodo array de numpy o con matrix de sympy para el uso de matemáticas simbólicas. Se recomienda el siguiente procedimiento:
    4.1. Crear las hileras de la matriz una por una, estas deben contener los coeficientes de cada variable en orden, tanto para las restricciones como para la función objetivo.
    4.2. Si se elaboró un tableu, seguir ese formato. Recordar que se debe partir de un punto factible (última columna positiva).
    4.3. Si se desean los resultados en decimales:
        4.3.1. Es importante agregar .0 al final de cada número, o su decimal correspondiente.
        4.3.2. Usar el array de numpy de la siguiente forma: mi_matriz = numpy.array([y1,y2,...,z])
               donde y1, y2, ... corresponden a cada una de las hileras que contienen las restriciones, y z la función objetivo.
    4.4. Si se desean los resultados en fracciones:
        4.4.1. Es importante que los datos estén contenidos como enteros, sin ningún decimal.  /// Considerando corregir esto.
        4.4.2. Usar matrix de sympy de la siguiente forma: mi_matriz = sympy.matrix([y1,y2,...,z])
5. Finalmente se inicia el programa con el comando jordan.iniciar(mi_matriz, False)
6. Adicionalmente, si se quiere obtener cada iteración del programa, se coloca como segundo parámetro True (por defecto False).
7. Una vez ejecutado el programa, se puede recuperar el resultado de la siguiente forma: resultado = jordan.resultado
