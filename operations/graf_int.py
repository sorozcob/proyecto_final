'''
'''
import matplotlib as plt
def graficar_int(id, puntos, index):
    plt.plot(puntos[0][:], index, label="Frecuencia de A")
    plt.plot(puntos[1][:], index, label="Frecuencia de T")
    plt.plot(puntos[2][:], index, label="Frecuencia de G")
    plt.plot(puntos[3][:], index, label="Frecuencia de C")

    # Agregar etiquetas y titulo
    plt.xlabel("Posición")
    plt.ylabel("Frecuencia")
    plt.title(f"Grafico de la frecuencia de nucleótidos de la secuencia {id}")

    # Agregar leyenda
    plt.legend()

    # Configurar las marcas de los ejes
    plt.xticks(range(0, max(index) + 1, 10))  # Marcas en el eje x cada 10 unidades
    plt.yticks([0.25, 0.5, 0.75, 1.0]) 
    
    # Mostrar el grafico
    plt.grid(True)
    plt.show()