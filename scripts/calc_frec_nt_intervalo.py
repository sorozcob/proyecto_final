'''

calc_frec_nt_intervalo.py: Script que genera una gráfica de la frecuencia 
a lo largo de una o varias secuencias

Este script lee las secuencia de DNA en un archivo Fasta y grafica la 
frecuencia de los 4 nucleótidos en intervalos de 8 nucleótidos por toda la 
secuencia. El archivo debe ser en formato Fasta, y la secuencia solo debe 
contener los nucleótidos 'A', 'C', 'G' o 'T'. Se puede seleccionar la 
secuencia a la que se quiere graficar indicando el número de esta.

Uso:
   python calc_frec_nt_intervalo.py <path_to_dna_file> [-i <índice(s)>]
   python calc_frec_nt_intervalo.py <path_to_dna_file> [--indices <índice(s)>]
   python -m proyecto_final.scripts.calc_frec_nt_intervalo proyecto_final/utils/archivo.fasta

Argumentos:
    <file>: Ruta al archivo de texto que contiene la secuencia de ADN.
    --indices: Opción para especificar las secuencia que se quieren graficar, 
    debe de indicarse qué secuencias separadas por un espacio.
'''
# ===========================================================================
# =                            Imports
# ===========================================================================
# Se importa la librería argparse
import argparse
# Se importa leer_fasta del archivo file_io 
from proyecto_final.utils.file_io import leer_fasta
# Se importa frecuencia_nt_intervalo del archivo frec_nt_intervalo
from proyecto_final.operations.frec_nt_intervalo import frecuencia_nt_intervalo
# Se importa alidate_fasta_format del archivo validators
from proyecto_final.utils.validators import validate_fasta_format

# ===========================================================================
# =                            Main
# ===========================================================================
# Definir la función principal
def main():
    # Crear un objeto ArgumentParser
    parser = argparse.ArgumentParser(description="Genera una gráfica de la frecuencia a lo largo de una o varias secuencias ")
    # Argumentos posicionales
    parser.add_argument("file", 
                        type=str, 
                        help="Archivo de ADN del cual leer la secuencia.")
    # Argumento opcional
    parser.add_argument("-i", "--indices",
                        type=int,
                        nargs='+',
                        default=None,
                        help='Un número (ej. <2>), un intervalo (ej. 4-7), o varios índices (ej. 3,5,6)')

    # Parsear los argumentos
    args = parser.parse_args()
    file_path = args.file
    indices = args.indices  

    try:
        # Validar el formato archivo de ADN para que se FASTA
        validate_fasta_format(file_path)
        # Leer las secuencias del archivo FASTA
        sequences = leer_fasta(file_path)

        i = 1
        # Iterar sobre los identificadores y secuencias
        for id, seq in sequences.items():
            # Verificar los índices 
            if args.indices is None or i in indices:
                # Calcular la frecuencia de los nucleótidos en la secuencia
                puntos = frecuencia_nt_intervalo(id, seq)
                print(f"Las frecuencias para la secuencia {id} son, en el orden A, T, G, C:\n {puntos}")
                input("Next?")
            i += 1
    
    # Capturar cualquier excepción
    except Exception as e:
        print(f"Error: {str(e)}")

# Si este script está siendo ejecutado como el programa principal
if __name__ == "__main__":
    main()