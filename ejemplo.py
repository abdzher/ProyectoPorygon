import numpy as np
import sympy as sp
import jordan
from sympy import Matrix


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


mi_matriz = Matrix([y1,y2,y3,y4,y5,z])

# EJECUTAR PROGRAMA
jordan.iniciar(mi_matriz)

# Recuperar resultado en una variable
resultado = np.array(jordan.resultado)

