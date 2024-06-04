"""
NAME: Lagrange
       

VERSION: 2.0
        

AUTHOR: JOCELYN TRUJILLO GUTIERREZ


DESCRIPTION: 
    
    Aplica el metodo de Lagrange, dado que el usuario introduzca un
    conjunto de puntos (x,y) y dados estos puntos puede ya sea encontrar
    una funcion que los describa o encontrar una y especifica de un punto x.
        
USAGE

    Introducir los datos solicitados.
    
ARGUMENTS:

    n(int): Numeros de puntos que tienes.
    --> Llenar tabla.

    graficar(str): Variable que al ser igualada a si procede a
                   imprimir toda grafica de los valores. Cuando 
                   se introduce cualquier valor distinto de si
                   se imprime el valor de y en el punto x.

    encontrar_y(str): Variable que al ser igualada a si procede a
                      calcular y para una x especifica. Cuando 
                      se introduce cualquier valor distinto de si
                      se calcula el polinomio que describe los puntos.


    x(float): Punto x del cual se quiere encontrar su valor de y.

    -------------------------------------NOTA-------------------------------------

    Todos los datos se trabajaron en funcion de x, al introducir cualquier otra 
    literal el codigo no funcionara.


METHOD

    Metodologia utilizada en el codigo:
        1.- El usuario procede a introducir los datos indicados.  
        2.- Calcular el valor de y o la funcion de y.
        3.- Impresion de resultados.


"""
# ===========================================================================
# =                            imports
# ===========================================================================

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ===========================================================================
# =                            funciones
# ===========================================================================

def tabulacion(n):
  tabla = np.empty((n,2))
  for i in range(n):
    tabla[i,0] = float(input(f"Introduce el valor de x{i}:"))
    tabla[i,1] = float(input(f"Introduce el valor de y{i}:"))
  return tabla

def valor_y(x,n,tabla):
  y = 0
  for i in range(n):
    x_xj = 0
    xi_xj = 0
    yi = tabla[i,1]
    for j in range(n):
      if i != j:
        yi *= (x - tabla[j,0]) / (tabla[i,0] - tabla[j,0])
    y += yi

  return y

def funcion_y(n,tabla):
  x = sp.symbols('x')
  y = 0
  for i in range(n):
    x_xj = 0
    xi_xj = 0
    yi = tabla[i,1]
    for j in range(n):
      if i != j:
        yi *= (x - tabla[j,0]) / (tabla[i,0] - tabla[j,0])
    y += yi

  return sp.simplify(y)

def grafica(tabla):
    plt.plot(tabla[:, 0], tabla[:, 1], marker='o')
    plt.axhline(0)
    plt.axvline(0)
    plt.grid(True)
    plt.show()

# ===========================================================================
# =                            main
# ===========================================================================

# Paso 1: Introducir datos
n = int(input(f"Numero de datos que quieres incluir: ")) # Num de datos
tabla = tabulacion(n)

graficar = str(input(f"Quieres imprimir la grafica de los puntos introducidos?(Introducir cualquier valor distinto de si se tomara como no). "))

encontrar_y = str(input(f"Quieres encontrar el valor de una y para cierta x dados puntos introducidos?(Introducir cualquier valor distinto de si se tomara como no). "))

# Paso 2: Dados los puntos se aplica la formula

if encontrar_y.upper() == "SI":
  x = float(input(f"Introduce el valor de x al que quieras llegar: "))
  print("\nA partir de los siguientes puntos:\n\tx  \ty")
  for i in range(n):
    print(f"\t{tabla[i,0]}\t{tabla[i,1]}")
  if graficar.upper() == "SI":
    grafica(tabla)
  print(f"\nSe obtuvo el siguiente valor de y = {valor_y(x,n,tabla)} para x = {x}")
else:
  print("\nA partir de los siguientes puntos:\n\tx  \ty")
  for i in range(n):
    print(f"\t{tabla[i,0]}\t{tabla[i,1]}")
  if graficar.upper() == "SI":
    grafica(tabla)
  print(f"\nSe obtuvo la siguiente funcion que los describe: {funcion_y(n,tabla)}")
