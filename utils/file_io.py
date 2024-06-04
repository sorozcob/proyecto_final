"""

file_io.py: Funcion para leer las secuencias de un archivo en formato FASTA.

Este modulo provee funcionalidades para leer secuencias de ADN desde un archivo
en formato FASTA, asegurando que las secuencias sean validas y esten bien formateadas.

Funciones:
   leer_fasta(archivo): Lee un archivo en formato FASTA y devuelve un diccionario 
   con las secuencias.
    
Ejemplos de uso estan disponibles en el bloque principal del modulo.

Autores: 
    Karla Ximena Gonzalez Platas
    Santiago Orozco Barrera

Versión: 1.0

"""

# ===========================================================================
# =                            Imports
# ===========================================================================

import argparse # Importacion de la libreria argparse
from Bio import SeqIO # Importacion de la funcion SeqIO del modulo Bio

# ===========================================================================
# =                            Functions
# ===========================================================================
def leer_fasta(archivo):
    """
    Lee un archivo en formato FASTA y devuelve un diccionario con las secuencias.
    
    Parametros:
        filename (str): Nombre del archivo en formato FASTA.
        
    Return:
        dict: Un diccionario donde las claves son los identificadores de las secuencias
              y los valores son las secuencias correspondientes.
    """
    sequences = {} # Inicializar diccionario
    with open(archivo, 'r') as file: # Abrir archivo en modo lectura
        for record in SeqIO.parse(file, 'fasta'): # Iterar sobre las secuencias del archivo
            # Agregar secuencia al diccionario
            sequences[record.id] = str(record.seq)
    return sequences

# Bloques de prueba para demostrar la funcionalidad del modulo.
if __name__ == "__main__":
    # Configurar el argumento de linea de comando para el nombre del archivo FASTA
    parser = argparse.ArgumentParser(description="Script para leer un archivo FASTA.")
    parser.add_argument("filename", help="Nombre del archivo FASTA")
    args = parser.parse_args()
    
    # Leer el archivo FASTA y manejar cualquier error
    try:
        fasta_sequences = leer_fasta(args.filename)
        for identifier, sequence in fasta_sequences.items():
            print(f"ID: {identifier}, Sequence: {sequence}")
    except Exception as e:
        print(f"Error: {str(e)}")
