"""

frec_nt_global.py: Modulo para calcular la frecuencia de nucleotidos en cada 
secuencia y la frecuencia en terminos de porcentaje de manera global.

Este modulo provee funcionalidades para calcular la frecuencia de nucleotidos. 

Funciones:
   frec_nt_global(secuencias): Calcula la frecuencia de nucleotidos en cada 
   secuencia y globalmente en terminos de porcentaje. 
    
Ejemplos de uso estan disponibles en el bloque principal del modulo.

Autores: 
    Karla Ximena Gonzalez Platas
    Santiago Orozco Barrera

Versión: 1.0

"""

# ===========================================================================
# =                            Imports
# ===========================================================================

# Importacion de librerias, funciones y modulos
import argparse # Libreria para manejar argumentos desde la linea de comandos
from Bio import SeqIO # Funcion SeqIO del modulo Bio para  leer archivos
from collections import Counter # Modulo de collections para contar elementos
from proyecto_final.utils.file_io import leer_fasta # Funcion del modulo file_io 

# ===========================================================================
# =                            Functions
# ===========================================================================

def frec_nt_global(secuencias):
    """
    Calcula la frecuencia de nucleotidos en cada secuencia y globalmente en 
    terminos de porcentaje. 
    
    Parametros:
        secuencias (dict): Diccionario de secuencias de ADN.
        
    Return:
        frecuencias_por_secuencia, frecuencia_global (tuple): Dos diccionarios, 
        uno con las frecuencias por secuencia y otro con la frecuencia global.
    """
    # Inicializar el diccionario, Counter y contador 
    frecuencias_por_secuencia = {} 
    frecuencia_global = Counter()
    total_nucleotidos = 0
    
    for id, secuencia in secuencias.items(): # Iterar sobre cada secuencia
        conteo_local = Counter(secuencia) # Contar nucleotidos en cada secuencia
        frecuencias_por_secuencia[id] = {nuc: conteo_local[nuc] for nuc in 'ACTG'} # Almacenar el conteo 
        frecuencia_global.update(conteo_local) # Actualizar el Counter global
        # Actualizar el contador total de nucleotidos sumando el conteo local
        total_nucleotidos += sum(conteo_local[nuc] for nuc in 'ACTG') 
    # Calcular la frecuencia global de cada nucleotido en terminos de porcentaje
    frecuencia_global = {nuc: (frecuencia_global[nuc] / total_nucleotidos) * 100 for nuc in 'ACTG'}
    # Devolver un tuple
    return frecuencias_por_secuencia, frecuencia_global

# Bloque de prueba para demostrar la funcionalidad del modulo.
if __name__ == "__main__":
    # Ejemplo de secuencias de ADN para probar la funcion
    secuencias_prueba = {
        "secuencia1": "ATCGATCGATCG",
        "secuencia2": "GCTAGCTAGCTA",
        "secuencia3": "ATAGCTAGCTAG",
    }
    
    try:
        # Calcular las frecuencias de nucleotidos
        frecuencias_por_secuencia, frecuencia_global = frec_nt_global(secuencias_prueba)
        
        # Imprimir los resultados obtenidos 
        print("Frecuencias por secuencia:")
        for id, frecuencias in frecuencias_por_secuencia.items():
            print(f"ID: {id}, Frecuencias: {frecuencias}")
        
        print("\nFrecuencia global de nucleotidos:")
        for nuc, frecuencia in frecuencia_global.items():
            print(f"{nuc}: {frecuencia:.2f}%")
    
    except Exception as e:
        print(f"Error: {str(e)}")

