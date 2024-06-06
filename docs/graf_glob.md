# Módulo graf_glob

Fecha: 05/06/2024

**Participantes / Autores**:

- [Santiago Orozco Barrera] < [santiago@lcg.unam.mx] >
- [Karla Ximena González Platas] <[ximenagp@lcg.unam.mx]>

## Descripción del Problema

graf_glob es un módulo en Python que genera una gráfica circular (gráfica de pastel) 
de la frecuencia global de cada nucleótido en términos de porcentaje. La funcionalidad 
principal del módulo es graficar las frecuencias globales de nucleótidos calculadas por 
otros módulos o funciones.


## Especificación de Requisitos

#### Requisitos funcionales:

    1. El script debe importar el módulo matplotlib para graficar.
    2. El módulo debe recibir un diccionario con la frecuencia global de nucleótidos.
    3. Debe generar una gráfica circular que muestre las frecuencias globales de los 
    nucleótidos 'A', 'C', 'T', 'G' en términos de porcentaje.
    4. La gráfica debe ser visualmente clara y destacar el nucleótido 'A' utilizando 
    un efecto de resalte.
    5. El módulo debe ser ejecutable desde la línea de comandos con un ejemplo de uso.

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
def graficar_frecuencia_global(frecuencia_global):
    obtener etiquetas y tamaños de las frecuencias globales
    definir colores para cada segmento de la gráfica
    definir la explosión para resaltar el segmento del nucleótido 'A'
    
    crear una figura de tamaño adecuado
    generar la gráfica de pastel con las frecuencias globales
    asegurar que la gráfica sea circular
    mostrar la gráfica en pantalla

```
#### Formato de los datos de entrada:

El diccionario de frecuencias globales de nucleótidos debe tener las claves 
'A', 'C', 'T', 'G' y los valores deben ser los porcentajes correspondientes.

#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona diccionario de frecuencias
                 v
         +-----------------+
         |                 |
         | Lo que se hace: |
         |   Generar la    |
         |     gráfica     |
         +-----------------+

```

- **Actor**: Usuario

- **Descripción**: El usuario proporciona un diccionario con las frecuencias 
globales de nucleótidos. El programa genera y muestra una gráfica circular que 
visualiza estos datos.

- **Flujo principal**:

    1. Proporcionar el diccionario de frecuencias globales de nucleótidos.
    2. Obtener las etiquetas y tamaños de las frecuencias.
    3. Definir colores y resaltar el segmento del nucleótido 'A'.
    4. Crear la figura y generar la gráfica de pastel.
    5. Asegurar que la gráfica sea circular.
    6. Mostrar la gráfica en pantalla.
	
- **Flujos alternativos**: 
1. Argumentos inválidos desde la línea de comandos: El programa manda un mensaje de error.
2. En las pruebas unitarias se genera un mensaje de error cuando:
   
	-La gráfica de pastel no es generada con los datos proporcionados.
	-La salida no contiene las etiquetas y tamaños esperados.

