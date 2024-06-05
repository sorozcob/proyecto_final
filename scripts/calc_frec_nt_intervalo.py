"""
calc_frec_nt_intervalo.py: Script que genera una gráfica de la frecuencia a lo largo de una o varias secuencias

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
from  utils.file_io import leer_fasta
from  operations.frec_nt_intervalo import frecuencia_nt_intervalo

class beta_ParseIndices(argparse.Action): #argparse.Action es una clase de argparse que define cómo se manejan los argumentos de línea de comandos.
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

class ParseIndices(argparse.Action): #argparse.Action es una clase de argparse que define cómo se manejan los argumentos de línea de comandos.
    def __call__(self, parser, namespace, values, option_string=None): # __call__ método que permite que una instancia de la clase se pueda llamar como si fuera una función.
        # self: Primer parámetro de cualquier método de instancia en una clase. self se refiere a la instancia de la clase que llama al método.
        # parser: Un objeto ArgumentParser. Es el parser que está llamando a esta acción.
        # namespace: Un objeto que contiene los atributos que representan los argumentos de línea de comandos parseados.
        # values: Los valores del argumento que se están procesando.
        # option_string=None: El nombre de la opción como fue especificada en la línea de comandos. Es None si el argumento no fue especificado como una opción.
        indices = []
        for value in values:
            if '-' in value:
                try:
                    start, end = value.split('-')
                    indices.extend(range(int(start), int(end) + 1))
                except ValueError:
                    raise argparse.ArgumentTypeError(f"Invalid range value: {value}")
            elif ',' in value:
                try:
                    indices.extend(int(x) for x in value.split(','))
                except ValueError:
                    raise argparse.ArgumentTypeError(f"Invalid list value: {value}")
            else:
                try:
                    indices.append(int(value))
                except ValueError:
                    raise argparse.ArgumentTypeError(f"Invalid single value: {value}")
        setattr(namespace, self.dest, indices) #Utiliza la función setattr para establecer el atributo self.dest del objeto namespace con el valor de indices. self.dest es el nombre del argumento como fue especificado en el parser


def main():

    parser = argparse.ArgumentParser(description="Calcula la  ")
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument(
        "-i", "--indices",
        action=ParseIndices,
        nargs='+',
        default=None,
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
            if args.indices is None or i in args.indices:
                frecuencia_nt_intervalo(id, seq, nucleotides)
                input("Next?")
            i += 1
        
        # Mostrar el resultado al usuario
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()