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

    ax.set_xticklabels(['10', '20', '30'])

    # Agregar leyenda
    plt.legend()

    # Mostrar el grafico
    plt.grid(True)
    plt.show()