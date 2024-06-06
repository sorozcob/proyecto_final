'''
'''
import matplotlib.pyplot as plt
def graficar_int(id, puntos, index):
    '''
    Grafica los puntos que representan las frecuencias 

    Args:
        puntos (array): Los valores para x que representan las frecuencias 
        de los nucleótidos.
        index (array): Valores de y que va de 1 al la longitud de la secuencia
        id (str): El identificador de la secuencia

    Returns:
        puntos (matriz): Con las frecuencias de todos los puntos 
    '''
    # Graficar los puntos
    plt.plot(index, puntos[0][:], label="Frecuencia de A")
    plt.plot(index, puntos[1][:], label="Frecuencia de T")
    plt.plot(index, puntos[2][:], label="Frecuencia de G")
    plt.plot(index, puntos[3][:], label="Frecuencia de C")

    # Agregar etiquetas y titulo
    plt.xlabel("Posición")
    plt.ylabel("Frecuencia")
    plt.title(f"Grafico de la frecuencia de nucleótidos de la secuencia {id}")

    # Agregar leyenda
    plt.legend()

    # Configurar las marcas de los ejes
    plt.xticks(range(0, max(index) + 1, 10))  
    plt.yticks([0.25, 0.5, 0.75, 1.0]) 

    # Mostrar el grafico
    plt.grid(True)
    plt.show()
    if __name__ == "__main__":
        return puntos

# Si se está siendo ejecutado como el programa principal
if __name__ == "__main__":
    id = "> Seq1"
    puntos = [
        [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4],
        [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],
        [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
        [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]]
    index = list(range(1, 17))
    graficar_int(id, puntos, index)