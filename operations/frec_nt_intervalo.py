'''
frec_nt_intervalo.py: Módulo que genera una gráfica de la frecuencia a lo largo de una o varias secuencias

Este módulo proporciona una función para graficar la frecuencia de cada nucleótico a lo largo de la secuencia 
en intervalos de 
el porcentaje de las bases de adenina (A)
y timina (T) en una secuencia de ADN dada. Esto es útil para estudios genéticos donde
las proporciones de AT pueden ser indicativas de ciertas características genómicas.

Funciones:
- calculate_at_content(sequence, normalize=True): Devuelve el porcentaje de AT en la secuencia.
'''
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
import sys
sys.path.append("C:/Users/soroz/Desktop/proyecto_final/operations")
from graf_int import graficar_int

def frecuencia_nt_intervalo(id, seq):
    '''
    Devuelve la gráfica de las frecuencia de una base nitrogenada en intervalos de una secuencia 
    ''' 
    seqn = seq + "NNNNNNN"
    seqn = seqn.upper()
    puntos = [[] for _ in range(4)]  # Inicializa puntos como una lista de listas para almacenar las frecuencias de A, T, G, C
    num_nt = len(seqn)
    for i in range(num_nt - 7):  # Ajustado para un segmento de longitud 8
        segmento = seqn[i:i+8]
        puntos[0].append(segmento.count("A") / 8)  # Frecuencia de A
        puntos[1].append(segmento.count("T") / 8)  # Frecuencia de T
        puntos[2].append(segmento.count("G") / 8)  # Frecuencia de G
        puntos[3].append(segmento.count("C") / 8)  # Frecuencia de C
    
    index = list(range(1, len(seqn) - 6))

    print(puntos)
    print(index)
    graficar_int(id, puntos, index)

if __name__  == "__main__":
    identificador = "> Seq1"
    secuencia = "atgagctagctgcggcgatagcgatcgacgatcgagcgcgctagcgtacggagctatcagcagtcgatcgatgcatgctagtggctagtgtgtgatcgatgtcggctagtagtcgtagctagctagctgatcatcgatca"
    frecuencia_nt_intervalo(identificador, secuencia)
