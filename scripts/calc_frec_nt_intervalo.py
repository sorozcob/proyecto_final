"""
calc_frec_nt_intervalo.py: Script para calcular la frecuencia de los codones en una secuencia de ADN.

Este script lee una secuencia de ADN desde un archivo dado y calcula la frecuencia de los codones presentes.
La secuencia de ADN debe estar en un archivo de texto y solo contener los caracteres 'A', 'C', 'G' o 'T'.
Adicionalmete, se puede seleccionar el marco de lectura, que puede ser -3, -2, -1, 1, 2, o 3. 

Uso:
    python calculate_codon_frequency.py <path_to_dna_file> [--normalize]

Argumentos:
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de ADN.
    --normalize        : Opción para normalizar el contenido de AT excluyendo 'N's del c
"""

import argparse
import sys
#sys.path.append("")
#sys.path.append("")
from  file_io import leer_fasta
from  frec_nt_intervalo import frecuencia_nt_intervalo

class ParseIndices(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        indices = []
        for value in values:
            if '-' in value:
                start, end = value.split('-')
                indices.extend(range(int(start), int(end) + 1))
            elif ',' in value:
                indices.extend(int(x) for x in value.split(','))
            else:
                indices.append(int(value))
        setattr(namespace, self.dest, indices)

def main():

    parser = argparse.ArgumentParser(description="Calcula la  ")
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument(
        "-i", "--indices",
        action=ParseIndices,
        nargs='+',
        help='Un número (ej. 2), un intervalo (ej. 4-7), o varios índices (ej. 3,5,6)'
    )

    args = parser.parse_args()
    file_path = args.file
    nucleotides = args.nucleotides.upper

    try:
        # Leer la secuencia del archivo especificado utilizando la función proporcionada por file_io.py
        sequences = leer_fasta(file_path)

        # Calcular la frecuencia utilizando la función proporcionada por acodon_frequency.py
        i = 1
        for id, seq in sequences.items:
            if i in args.indices:
                frecuencia_nt_intervalo(id, seq, nucleotides)
                input("Next?")
            i += 1
        
        # Mostrar el resultado al usuario
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()