'''
'''
from graf_int import graficar_int

def frecuencia_nt_intervalo(id, seq):
    '''
    Devuelve la gráfica de las frecuencia de una base nitrogenada en intervalos de una secuencia 
    ''' 
    seqn = seq + "NNNNNNN"
    puntos = []
    puntosA = []
    puntosT = []
    puntosG = []
    puntosC = []
    seqn = seqn.upper
    for i in range(len(seqn) - 7):
            segmento = seqn[i:i+7]
            puntosA.append(segmento.count("A"))
            puntosT.append(segmento.count("T"))
            puntosG.append(segmento.count("G"))
            puntosT.append(segmento.count("C"))
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
    frecuencia_nt_intervalo(identificador, secuencia, nucleotido)