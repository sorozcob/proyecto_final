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
    --indices: Opción para especificar las secuencia que se quieren graficar.
"""

import argparse
import sys
#sys.path.append("C:/Users/soroz/Desktop/proyecto_final/utils")
#sys.path.append("C:/Users/soroz/Desktop/proyecto_final/operations")
from file_io import leer_fasta
from frec_nt_intervalo import frecuencia_nt_intervalo

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

    parser = argparse.ArgumentParser(description="Genera una gráfica de la frecuencia a lo largo de una o varias secuencias ")
    parser.add_argument("file", 
                        type=str, 
                        help="Archivo de ADN del cual leer la secuencia.")
    '''
    parser.add_argument("-i", "--indices",
                        action=ParseIndices,
                        nargs='+',
                        default=None,
                        help='Un número (ej. 2), un intervalo (ej. 4-7), o varios índices (ej. 3,5,6)')
    '''
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
        sequences = leer_fasta(file_path)

        # Calcular la frecuencia utilizando la función proporcionada por acodon_frequency.py
        i = 1
        for id, seq in sequences.items:
            if args.indices is None or i in args.indices:
                frecuencia_nt_intervalo(id, seq, indices)
                input("Next?")
            i += 1
        
        # Mostrar el resultado al usuario
    except Exception as e:
        print(f"Error: {str(e)}")

#if __name__ == "__main__":
    #main()