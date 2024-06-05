"""

graf_glob.py: Modulo para generar una grafica circular de la frecuencia global 
de cada nucleotido en terminos de porcentaje. 

Este modulo provee funcionalidades para graficar la frecuencia global de 
nucleotidos. 

Funciones:
    graficar_frecuencia_global(frecuencia_global):Genera una grafica circular 
        (grafica de pastel) de la frecuencia global de nucleotidos calculada en 
        terminos de porcentaje.
    
Ejemplos de uso:
    graficar_frecuencia_global(frecuencia_global)

Autores: 
    Karla Ximena Gonzalez Platas
    Santiago Orozco Barrera

Versión: 1.0

"""


# ===========================================================================
# =                            Imports
# ===========================================================================

import matplotlib.pyplot as plt # Importar modulo de matplotlib para graficar

# ===========================================================================
# =                            Functions
# ===========================================================================

def graficar_frecuencia_global(frecuencia_global):
    """
    Genera una grafica circular (grafica de pastel) de la frecuencia global de nucleotidos
    calculada en terminos de porcentaje.
    
        Parametros:
            frecuencia_global (dict): Diccionario con la frecuencia global de cada nucleotido.
            Las claves son 'A', 'C', 'T', 'G' y los valores son los porcentajes.

    """
    labels = frecuencia_global.keys() # Asignar las claves del diccionario
    sizes = frecuencia_global.values() # Asignar los valores de los porcentajes
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] # Colores para segmentos de la grafica
    explode = (0.1, 0, 0, 0)  # Resaltar el primer segmento ('A')

    plt.figure(figsize=(8, 8)) # Crear figura con un tamano de 8x8 para la grafica
    # Generar la grafica de pastel 
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    plt.axis('equal')  # Asegurar que la grafica sea circular
    plt.title("Frecuencia Global de Nucleotidos")
    plt.show() # Mostrar la grafica en pantalla

# Bloque de prueba para demostrar la funcionalidad del modulo
if __name__ == "__main__":
    # Supongamos que ya hemos obtenido las frecuencias globales de nucleotidos
    frecuencia_global = {'A': 30.0, 'C': 20.0, 'T': 25.0, 'G': 25.0}
    # Llamar a la funcion para generar la grafica de pastel
    graficar_frecuencia_global(frecuencia_global)  # Generar la grafica de pastel

