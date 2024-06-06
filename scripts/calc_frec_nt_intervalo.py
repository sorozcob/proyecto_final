"""
calc_frec_nt_intervalo.py: Script que genera una gráfica de la frecuencia a lo largo de una o varias secuencias

Este script lee las secuencia de DNA en un archivo Fasta y grafica la frecuencia de los 4 nucleótidos en intervalos
de 8 nucleótidos por toda la secuencia. El archivo debe ser en formato Fasta, y la secuencia solo debe contener los
nucleótidos 'A', 'C', 'G' o 'T'. Se puede seleccionar la secuencia a la que se quiere graficar indicando el número 
de esta.

Uso:
    python calc_frec_nt_intervalo.py <path_to_dna_file> [-i <índice(s)>]
    python calc_frec_nt_intervalo.py <path_to_dna_file> [--indices <índice(s)>]

Argumentos:
    <file>: Ruta al archivo de texto que contiene la secuencia de ADN.
    --indices: Opción para especificar las secuencia que se quieren graficar, debe de indicarse qué secuencias separadas por un espacio.
"""

import argparse

from proyecto_final.utils.file_io import leer_fasta
from proyecto_final.operations.frec_nt_intervalo import frecuencia_nt_intervalo
from proyecto_final.utils.validators import validate_fasta_format

def main():

    parser = argparse.ArgumentParser(description="Genera una gráfica de la frecuencia a lo largo de una o varias secuencias ")
    parser.add_argument("file", 
                        type=str, 
                        help="Archivo de ADN del cual leer la secuencia.")

    parser.add_argument("-i", "--indices",
                        type=int,
                        nargs='+',
                        default=None,
                        help='Un número (ej. <2>), un intervalo (ej. 4-7), o varios índices (ej. 3,5,6)')

    args = parser.parse_args()
    file_path = args.file
    indices = args.indices  
    
    try:
        # Leer la secuencia del archivo especificado utilizando la función proporcionada por file_io.py
        validate_fasta_format(file_path)
        sequences = leer_fasta(file_path)

        # Calcular la frecuencia utilizando la función proporcionada por acodon_frequency.py
        i = 1
        for id, seq in sequences.items():
            if args.indices is None or i in indices:
                frecuencia_nt_intervalo(id, seq)
                input("Next?")
            i += 1
    
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()