# Módulo graf_int

Fecha: 05/06/2024

**Participantes / Autores**:

- [Santiago Orozco Barrera] < [santiago@lcg.unam.mx] >
- [Karla Ximena González Platas] <[ximenagp@lcg.unam.mx]>

## Descripción del Problema

El módulo graf_int proporciona una función para graficar una matriz que representa la 
frecuencia de cada nucleótido a lo largo de una secuencia de ADN en intervalos de 8 
nucleótidos. Este módulo es útil para visualizar cómo varían las frecuencias de los 
nucleótidos a lo largo de una o varias secuencias


## Especificación de Requisitos

#### Requisitos funcionales:

    1. El script debe importar el módulo matplotlib.pyplot para generar gráficos.
    2. Debe definir una función graficar_int que reciba un identificador de secuencia, 
    una matriz de frecuencias y una lista de índices.
    3. La función debe graficar las frecuencias de los nucleótidos a lo largo de la secuencia.
    4. Debe etiquetar los ejes y agregar un título al gráfico.
    5. Debe agregar una leyenda para diferenciar las frecuencias de cada nucleótido.
    6. Debe mostrar el gráfico generado.
    7. El módulo debe ser ejecutable desde la línea de comandos con un ejemplo de uso.
    
#### Requisitos no funcionales: 

    - El script deberá estar escrito en Python.
    - El tiempo de generación de la gráfica debe ser rápido.
    - La gráfica debe ser precisa y representar correctamente los porcentajes 
      proporcionados.
    - El módulo debe ser fácil de usar e integrar con otros módulos o scripts.
    - Debe seguir las mejores prácticas de codificación y estructura de proyectos 
      en Python.


## Análisis y Diseño

La resolución del problema sigue una metodología sencilla basada en la recolección 
de frecuencias de nucleótidos, el uso de la biblioteca matplotlib para generar la 
gráfica y la presentación de los resultados de manera visual.

#### Pseudocódigo

Pseudocógido simple que ilustra la lógica básica del modulo:

```
def graficar_int(id, puntos, index):
    graficar las frecuencias de los nucleótidos usando matplotlib
    
    etiquetar los ejes y agregar un título
    
    agregar una leyenda para diferenciar las frecuencias de cada nucleótido
    
    mostrar el gráfico generado
    
    devolver la matriz de frecuencias

```
#### Formato de los datos de entrada:

    - id: Identificador de la secuencia (str)
    - puntos: Matriz con las frecuencias de los nucleótidos (array)
    - index: Lista de índices que va de 1 a la longitud de la secuencia (array)

#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona matriz de frecuencias e identificador
                 v
         +-----------------+
         |                 |
         | Lo que se hace: |
         |    Graficar     |
         |    frecuencias  |
         +-----------------+
                 |
                 v
         +-----------------+
         |                 |
         | Lo que se hace: |
         |    Mostrar la   |
         |    gráfica      |
         +-----------------+

```

- **Actor**: Usuario

- **Descripción**: El usuario proporciona una matriz de frecuencias de nucleótidos 
y el identificador de la secuencia. El programa genera y muestra una gráfica con 
las frecuencias a lo largo de la secuencia.

- **Flujo principal**:
    1. Proporcionar la matriz de frecuencias de nucleótidos y el identificador de 
    la secuencia.
    2. Graficar las frecuencias usando matplotlib.
    3. Etiquetar los ejes y agregar un título.
    4. Agregar una leyenda para diferenciar las frecuencias de cada nucleótido.
    5. Mostrar el gráfico generado.
    6. Devolver la matriz de frecuencias.
	
- **Flujos alternativos**: 
    [Casos que salen del uso común del programa]
    - Si la matriz de frecuencias está vacía o no contiene datos válidos:
        1. El programa manda un mensaje de error.
    - Si el identificador no es válido o está vacío:
        1. El programa manda un mensaje de error.
    - Argumentos inválidos desde la línea de comandos:
        1. El programa manda un mensaje de error.


