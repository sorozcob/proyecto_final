'''

frec_nt_intervalo.py: Módulo que genera una gráfica de la frecuencia a lo 
largo de una o varias secuencias.

Este módulo proporciona una función para graficar la frecuencia de cada 
nucleótico a lo largo de la secuencia en intervalos de 8 nucleótidos. 

Funciones:
- frecuencia_nt_intervalo(id, seq): Grafica la frecuencia de la secuencia 
de cada nucleótido.

Ejemplos de uso:
    python frec_nt_intervalo.py

Autores: 
    Karla Ximena Gonzalez Platas
    Santiago Orozco Barrera

Versión: 1.0

'''
# ===========================================================================
# =                            Imports
# ===========================================================================
# Importar el módulo sys
import sys
# Agregar la ruta al directorio de operaciones al módulo sys para poder importar el módulo graf_int
sys.path.append("C:/Users/soroz/Desktop/proyecto_final/operations")
# Importar la función graficar_int del módulo graf_int
from graf_int import graficar_int

# ===========================================================================
# =                            Main
# ===========================================================================
# Definir la función frecuencia_nt_intervalo que calcula y grafica las frecuencias de las bases nitrogenadas en intervalos de una secuencia
def frecuencia_nt_intervalo(id, seq):
    """
    Calcula las frecuencias de los 4 nucleótidos y llama a la función 
    graficar_int para graficarlos

    Args:
        seq (str): La secuencia de ADN a analizar.
        id (str): El identificador de la secuencia

    Returns:
        puntos (matriz): Con las frecuencias de todos los puntos 

    """
    # Agregar una secuencia de 7 nucleótidos adicionales al final de la secuencia original para asegurar que todos los intervalos tengan una longitud de 8
    seqn = seq + "NNNNNNN"
    
    # Convertir la secuencia a mayúsculas para asegurar una comparación insensible a mayúsculas y minúsculas
    seqn = seqn.upper()
    
    # Inicializar una lista de listas llamada "puntos" para almacenar las frecuencias de A, T, G, C en cada intervalo
    puntos = [[] for _ in range(4)]
    
    # Calcular el número total de nucleótidos en la secuencia (incluyendo los nucleótidos añadidos)
    num_nt = len(seqn)
    
    # Iterar a través de la secuencia para calcular las frecuencias en cada intervalo
    for i in range(num_nt - 7):  # Ajustado para un segmento de longitud 8
        # Extraer un segmento de 8 nucleótidos
        segmento = seqn[i:i+8]
        
        # Calcular y agregar las frecuencias normalizadas de A, T, G, C en el segmento actual a la lista "puntos"
        puntos[0].append(segmento.count("A") / 8)  # Frecuencia de A
        puntos[1].append(segmento.count("T") / 8)  # Frecuencia de T
        puntos[2].append(segmento.count("G") / 8)  # Frecuencia de G
        puntos[3].append(segmento.count("C") / 8)  # Frecuencia de C
    
    # Crear una lista de índices para cada intervalo
    index = list(range(1, len(seqn) - 6))
    
    # Llamar a la función graficar_int para generar una gráfica de las frecuencias en intervalos y mostrarla
    puntos = graficar_int(id, puntos, index)
    
    return puntos 

# Verificar si este script está siendo ejecutado directamente como el programa principal
if __name__  == "__main__":
    identificador = "> Seq1"
    secuencia = "atgctacgtgcgcgcgattagcgtatttatatgcgcgatcggatctgattgtctaggcgagcggcagcgatcgtagctagctagctagctagctgactgcgcgcgtagctgcgatcgatcgtagccgtcga"
    frecuencia_nt_intervalo(identificador, secuencia)
