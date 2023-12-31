# ProyectoPorygon

Programas creados para la solucion de problemas dados en investigación de operaciones.

Versión 0.8
## Cambios de la versión:
- Empaquetado más ligero para Simplex solver.
- NUEVO PROGRAMA: CPM Solver, solucion de problemas de ruta crítica.

## Futuros cambios:
- Almacenamiento e intercambio de las variables.
- Poder exportar CSV.
- Poder ignorar saltos de pagina, espacios, etc.
- Rehabilitar matematicas simbolicas.


# INSTRUCCIONES:
* Descargar de la seccion RELEASES.
* Para usar solo jordan.py como un módulo, vea las instrucciones de la version 0.6.

## Instrucciones de CPM solver.
* Crear un archivo CSV según el formato de ejemplo, es importante que para colocar varios predescesores se separen con espacios.
* La duración debe mantener el mismo tipo de unidades, ya sea horas, días, semanas, meses, etc. los resultados también se mostrarán con esta unidad, la cual no se especifica.
* Es importante que la duración sea un valor entero.
* Posteriormente, debe colocarse en el cuadro de texto principal la dirección del archivo CSV.
* En los otros cuadros, colocar la fecha inicial, el cual debe ser un entero.
* Finalmente, presionar el botón de iniciar.
* Se presentará un diagrama de Grantt, además, el cuadro con los resultados se copiarán al portapapeles.

## Instrucciones de Simplex solver.
### Iniciar desde una linea de texto
* En el cuadro de texto escriba sus datos, sin espacios, separados por comas y punto y coma para cada salto entre filas.
* Ejemplo:

> -2,1,2;-3,4,12;0,1,6;3,-1,21;1,-1,5;3,-6,0

* Finalmente, presione el botón 'Iniciar desde texto'.

### Iniciar desde archivo .csv.
* IMPORTANTE: El archivo debe seguir el formato del ejemplo, de la siguiente manera, donde ## son los coeficientes numericos.
>     ST , VAR1 , VAR2 , ... , VARN , ANS

>        ,  X1  ,  X2  , ... , VARN ,

>     Y1 ,  ##  ,  ##  , ... ,  ##  ,  ##

>     Y2 ,  ##  ,  ##  , ... ,  ##  ,  ##

>    ... ,  ..  ,  ..  , ... ,  ..  ,  ..

>     YN ,  ##  ,  ##  , ... ,  ##  ,  ##

* En caso de usar matematicas simbolicas: pueden colocarse enteros o fracciones (con una barra diagonal "/"), pero no puntos decimales ni símbolos.
* En caso de trabajar con decimales: solo pueden colocarse numeros enteros o decimales, no simbolos ni fracciones.
* En el cuadro de texto debe colocar la ubicacion completa del archivo.
* Ejemplo:

> C:\Users\Me\Documents\csvejemplo.csv

* Finalmente, presione el boton "Iniciar desde CSV".

### Parametros adicionales.

* Se pueden seleccionar los recuadros que especifican diferentes:
* * Mostrar desarrollo completo: Mostrará cada una de las iteraciones que se realizaron en el proceso de solución, los pivotes elegidos y más.
* * Indicar número de decimales: Agregue un espacio y un número entero para indicar la cantidad de números decimales que quiere mostrar (ejemplo: 2,1;1,0 *5*)
* * Exportar txt: El texto mostrado en el cuadro de resultados será exportado como un archivo txt, cópielo en otro lugar para evitar que este se sobreescriba.
* * Exportar CSV: En desarrollo...