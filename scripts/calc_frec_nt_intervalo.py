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
# Se importa la librería argparse
import argparse
# Se importa leer_fasta del archivo file_io 
from proyecto_final.utils.file_io import leer_fasta
# Se importa frecuencia_nt_intervalo del archivo frec_nt_intervalo
from proyecto_final.operations.frec_nt_intervalo import frecuencia_nt_intervalo
# Se importa alidate_fasta_format del archivo validators
from proyecto_final.utils.validators import validate_fasta_format

# Definir la función principal del programa
def main():
    # Crear un objeto ArgumentParser con una descripción para el programa
    parser = argparse.ArgumentParser(description="Genera una gráfica de la frecuencia a lo largo de una o varias secuencias ")
    # Agregar un argumento posicional que represente el archivo de ADN del cual leer la secuencia
    parser.add_argument("file", 
                        type=str, 
                        help="Archivo de ADN del cual leer la secuencia.")
    # Agregar un argumento opcional que represente los índices a considerar
    parser.add_argument("-i", "--indices",
                        type=int,
                        nargs='+',
                        default=None,
                        help='Un número (ej. <2>), un intervalo (ej. 4-7), o varios índices (ej. 3,5,6)')

    # Parsear los argumentos de la línea de comandos
    args = parser.parse_args()
    # Obtener la ruta del archivo de ADN del argumento "file"
    file_path = args.file
    # Obtener los índices del argumento "indices"
    indices = args.indices  

    try:
        # Validar el formato archivo de ADN para que se FASTA utilizando validate_fasta_format de validators
        validate_fasta_format(file_path)
        # Leer las secuencias del archivo FASTA utilizando una función externa
        sequences = leer_fasta(file_path)

        # Inicializar un contador para los identificadores de secuencia
        i = 1
        # Iterar sobre los identificadores y secuencias en el diccionario "sequences"
        for id, seq in sequences.items():
            # Verificar si no se especificaron índices o si el índice actual está en los índices especificados
            if args.indices is None or i in indices:
                # Calcular la frecuencia de los nucleótidos en el intervalo de la secuencia actual
                frecuencia_nt_intervalo(id, seq)
                # Esperar la entrada del usuario para continuar
                input("Next?")
            # Incrementar el contador de identificadores de secuencia
            i += 1
    
    # Capturar cualquier excepción que ocurra durante la ejecución del programa
    except Exception as e:
        # Imprimir un mensaje de error en caso de excepción
        print(f"Error: {str(e)}")

# Verificar si este script está siendo ejecutado directamente como el programa principal
if __name__ == "__main__":
    # Llamar a la función main() definida anteriormente
    main()