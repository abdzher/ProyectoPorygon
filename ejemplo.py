import jordan
import numpy as np
import sympy as sp



'NUEVO ---- Iniciar desde tabla CSV'
# IMPORTANTE: El archivo debe seguir el formato del ejemplo, de la siguiente manera
#        ST , VAR1 , VAR2 , ... , VARN , ANS
#           ,  X1  ,  X2  , ... , VARN ,
#        Y1 ,  ##  ,  ##  , ... ,  ##  ,  ##
#        Y2 ,  ##  ,  ##  , ... ,  ##  ,  ##
#       ... ,  ..  ,  ..  , ... ,  ..  ,  ..
#        YN ,  ##  ,  ##  , ... ,  ##  ,  ##
# Donde ## son los coeficientes numericos.
# En caso de usar matematicas simbolicas: pueden colocarse enteros o fracciones, pero no puntos decimales ni simbolos
# En caso de trabajar con decimales: solo pueden colocarse numeros enteros o decimales, no simbolos ni fracciones

# Para iniciar simplemente se debe colocar el comando siguiente con los parametros indicados.
# Parametro 1: Indicar la ubicacion del archivo como un string.
#      Si el archivo csv se encuentra en la misma carpeta que jordan.py, es tan facil como solo poner su nombre y extension (recuerda no usar espacios).
# Parametro 2: True si quiere que se muestren todas las iteraciones, False para evitar eso.
# Parametro 3: True si quiere usar matematicas simbolicas, False para trabajar con decimales.
# Parametro 4: El numero de decimales que se mostraran en caso de trabajar con ellos.

jordan.iniciar_desde_csv(ubicacion = 'csvejemplo.csv' , mostrar_desarrollo = True, simbolico = False, numero_de_decimales = 3)




'NUEVO ---- Iniciar desde listas'
# Puedes crear una lista de listas e iniciar desde ahi el programa
mi_lista = [[-2,1,2],[-3,4,12],[0,1,6],[3,-1,6],[3,-1,21],[1,-1,5],[3,-6,0]]
jordan.iniciar_desde_listas(lista = mi_lista , mostrar_desarrollo = False, simbolico = True)




'- Iniciar desde un objeto array o matrix creado'
# RESULTADO DECIMAL
# Importante poner el .0, sino los resultados decimales se darán como enteros.

y1 = [-2.0, 1.0, 2.0]
y2 = [-3.0, 4.0, 12.0]
y3 = [0.0, 1.0, 6.0]
y4 = [3.0, -1.0, 21.0]
y5 = [1.0, -1.0, 5.0]
z = [3.0, -6.0, 0.0]

mi_matriz = np.array([y1,y2,y3,y4,y5,z])

# EJECUTAR PROGRAMA
jordan.iniciar(mi_matriz)

# Recuperar resultado en una variable
resultado = jordan.resultado




# RESULTADO CON FRACCIONES
# Indispensable tener instalado sympy

y1 = [-2, 1, 2]
y2 = [-3, 4, 12]
y3 = [0, 1, 6]
y4 = [3, -1, 21]
y5 = [1, -1, 5]
z = [3, -6, 0]


mi_matriz = sp.Matrix([y1,y2,y3,y4,y5,z])

# EJECUTAR PROGRAMA
jordan.iniciar(mi_matriz)

# Recuperar resultado en una variable
resultado = jordan.resultado

