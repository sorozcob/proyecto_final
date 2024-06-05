'''
frec_nt_intervalo.py: Módulo para calcular el contenido de adenina y timina en secuencias de ADN.

Este módulo proporciona funciones para determinar el porcentaje de las bases de adenina (A)
y timina (T) en una secuencia de ADN dada. Esto es útil para estudios genéticos donde
las proporciones de AT pueden ser indicativas de ciertas características genómicas.

Funciones:
- calculate_at_content(sequence, normalize=True): Devuelve el porcentaje de AT en la secuencia.
'''
import sys
sys.path.append("C:/Users/soroz/Desktop/proyecto_final/operations")
from graf_int import graficar_int

def frecuencia_nt_intervalo(id, seq):
    '''
    Devuelve la gráfica de las frecuencia de una base nitrogenada en intervalos de una secuencia 
    ''' 
    seqn = seq + "NNNNNNN"
    seqn = seqn.upper()
    puntos = []
    puntosA = []
    puntosT = []
    puntosG = []
    puntosC = []
    num_nt = len(seqn)
    for i in range(num_nt - 7):
            segmento = seqn[i:i+7]
            puntosA.append(segmento.count("A")/8)
            puntosT.append(segmento.count("T")/8)
            puntosG.append(segmento.count("G")/8)
            puntosT.append(segmento.count("C")/8)
    puntos.append(puntosA)
    puntos.append(puntosT)
    puntos.append(puntosG)
    puntos.append(puntosC)

    index = list(range(1,len(seq)))

    graficar_int(id, puntos, index)


if __name__  == "__main__":
    identificador = "> Seq1"
    secuencia = "atgctagctagctagctagca"
    nucleotido = "a"+"t"
    frecuencia_nt_intervalo(identificador, secuencia)