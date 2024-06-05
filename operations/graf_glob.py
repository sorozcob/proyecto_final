"""

graf_glob.py: Modulo para generar una grafica circular de la frecuencia global 
de cada nucleotido en terminos de porcentaje. 

Este modulo provee funcionalidades para graficar la frecuencia global de 
nucleotidos. 

Funciones:
    graficar_frecuencia_global(frecuencia_global):Genera una grafica circular 
        (grafica de pastel) de la frecuencia global de nucleotidos calculada en 
        terminos de porcentaje.
    
    generar_graf_glob(): Genera una grafica de pastel que muestra la frecuencia 
        global de nucleotidos a partir de un archivo FASTA.
    
Ejemplos de uso:
    generar_graf_glob():

Autores: 
    Karla Ximena Gonzalez Platas
    Santiago Orozco Barrera

Versión: 1.0

"""


# ===========================================================================
# =                            Imports
# ===========================================================================

# Importacion de librerias, funciones y modulos
import matplotlib.pyplot as plt # Modulo de matplotlib para graficar
from frec_nt_global import frec_nt_global # Funcion frec_nt_global del modulo frec_nt_global
from proyecto_final.utils.file_io import leer_fasta # Funcion del modulo file_io 

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

def generar_graf_glob():
    """
    Genera una grafica de pastel que muestra la frecuencia global de nucleotidos a partir de un archivo FASTA.
    
        Esta funcion realiza los siguientes pasos:
            1. Lee el archivo FASTA para obtener las secuencias de ADN.
            2. Calcula las frecuencias globales de nucleotidos a partir de las secuencias obtenidas.
            3. Genera la grafica de pastel que muestra la frecuencia global de cada nucleotido.
        
        Parametros:
            No recibe ningun parametro directamente. El archivo FASTA y la funcion para leerlo estan predefinidos dentro 
            de la funcion.
        
        Return:
            Grafica circular
    """
    # Leer el archivo FASTA para obtener las secuencias de ADN
    archivo_fasta = "ruta/al/archivo.fasta"  # Ruta al archivo FASTA
    secuencias_fasta = leer_fasta(archivo_fasta)

    # Obtener las frecuencias globales de nucleótidos
    frecuencias_por_secuencia, frecuencia_global = frec_nt_global(secuencias_fasta)

    # Generar la grafica de pastel utilizando la funcion graficar_frecuencia_global
    graficar_frecuencia_global(frecuencia_global)

# Bloques de prueba para demostrar la funcionalidad del modulo.
if __name__ == "__main__":
    generar_graf_glob()  # Generar la grafica de pastel

