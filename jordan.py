''' ======================= SOLUCION POR METODO DE JORDAN ======================= '''
''' =======================       - VERSION 0.5 -         ======================= '''


import numpy as np
import sympy

# Variables que se usan solo si se eligio obtener cada iteracion.
desarrollo = False
iteracion = 0
resultado = np.array([0,0])

# INICIAR EL PROGRAMA: Obtiene el numero de hileras y de columnas.
def iniciar(mtrx,mostrar_desarrollo=False):
    
    global desarrollo
    desarrollo = mostrar_desarrollo
    
    m = mtrx.shape[0] - 1 # Num de hileras
    n = mtrx.shape[1] - 1 # Num de columnas
    
    print('====== EL PROCESO SERA INICIADO =======')
    print(f'La matriz inicial es \n{mtrx}')
    print(f'La matriz es de {m+1}X{n+1}')
    
    if desarrollo == True: print('Se mostrara cada iteracion del programa')
    
    comprobar_resultado(mtrx,m,n)
    
    
# Funcion de transicion.
def comprobar_resultado(mtrx,m,n):
    obtener_indice(mtrx,m,n)
    
# Funcion para obtener la columna con valor negativo en Z.
def obtener_indice(mtrx,m,n):
    
    resultados = []
    indice = -1
    
    for i in range(0,n): resultados.append(mtrx[m,i])
    
    for i in resultados: 
        if i < 0:
            indice = resultados.index(i)
            break
        
    if indice == -1: final(mtrx)
    else: obtener_pivote(indice,mtrx,m,n)


# Funcion que obtiene el pivote bajo el principio de obtener el minimo cociente.
def obtener_pivote(indice,mtrx,m,n):
    
    global desarrollo
    global iteracion
    
    iteracion += 1
    lista = []
    
    
    for i in range(0,m):
        if mtrx[i,indice] <= 0:
            lista.append(999999999999999999999999999999999999)
            continue
        lista.append(mtrx[i,n]/mtrx[i,indice])
        
    r = lista.index(min(lista))
    
    if desarrollo == True: print(f'\n==== Iteracion numero: {iteracion}\nEl pivote elegido es: \n({r},{indice}) con valor {mtrx[r,indice]}')
    
    resolver(r,indice,mtrx,m,n)


# Esta funcion realiza las operaciones del procedimiento dado el pivote seleccionado
def resolver(r,s,mtrx,m,n):
    
    global desarrollo
    matrix = mtrx
    clon = np.copy(mtrx)
    pivote = mtrx[r,s]
    
    matrix[r,s] = 1/pivote
    
    for i in range(0,m+1):
        if i == r: continue
        matrix[i,s] = - clon[i,s]/pivote
    
    for j in range(0,n+1):
        if j == s: continue
        matrix[r,j] = clon[r,j]/pivote
    
    for i in range(0,m+1):
        if i == r: continue
        else:
            for j in range(0,n+1):
                if j == s: continue
                else: matrix[i,j] = clon[i,j] - ((clon[i,s]*clon[r,j])/pivote)
                
    if desarrollo == True: print(f'El resultado de la iteracion es: \n{matrix}')
    comprobar_resultado(matrix,m,n)    
    

def final(mtrx):
    global iteracion
    global resultado
    resultado = mtrx
    print(f'''
=====================================================
El proceso se ha finalizado, solucion en 
{iteracion} iteraciones. La matriz resultante es:
{mtrx}'''
    )
