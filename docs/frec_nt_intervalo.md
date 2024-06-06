
# Módulo frec_nt_intervalo

Fecha: 05/06/2024

**Participantes / Autores**:

- [Santiago Orozco Barrera] < [santiago@lcg.unam.mx] >
- [Karla Ximena González Platas] <[ximenagp@lcg.unam.mx]>

## Descripción del Problema

frec_nt_intervalo es un módulo en Python que genera una gráfica de la frecuencia de 
cada nucleótido a lo largo de una secuencia de ADN en intervalos de 8 nucleótidos. 
La funcionalidad principal del módulo es calcular y graficar las frecuencias de 
nucleótidos en intervalos para visualizar cómo varían a lo largo de la secuencia.

## Especificación de Requisitos

#### Requisitos funcionales:

    1. El script debe importar el módulo sys y agregar la ruta al directorio de operaciones.
    2. Debe importar la función graficar_int del módulo graf_int.
    3. El módulo debe recibir una secuencia de ADN y su identificador.
    4. Debe calcular las frecuencias de los nucleótidos 'A', 'C', 'T', 'G' en intervalos 
    de 8 nucleótidos a lo largo de la secuencia.
    5. Debe generar una gráfica que visualice las frecuencias calculadas y mostrarla.
    6. El módulo debe ser ejecutable desde la línea de comandos con un ejemplo de uso.

#### Requisitos no funcionales: 

    - El script deberá estar escrito en Python.
    - El tiempo de cálculo y generación de la gráfica debe ser rápido, incluso con 
      secuencias largas.
    - La gráfica debe ser precisa y representar correctamente las frecuencias calculadas.
    - El módulo debe ser fácil de usar e integrar con otros módulos o scripts.
    - Debe seguir las mejores prácticas de codificación y estructura de proyectos en 
      Python. 

## Análisis y Diseño

La resolución del problema sigue una metodología sencilla basada en la recolección de 
frecuencias de nucleótidos en intervalos de la secuencia, el uso de la biblioteca matplotlib 
para generar la gráfica y la presentación de los resultados de manera visual.

#### Pseudocódigo

Pseudocógido simple que ilustra la lógica básica del modulo:

```
def frecuencia_nt_intervalo(id, seq):
    agregar nucleótidos adicionales al final de la secuencia
    convertir la secuencia a mayúsculas
    
    inicializar lista para almacenar frecuencias de A, T, G, C en cada intervalo
    
    iterar a través de la secuencia para calcular las frecuencias en cada intervalo:
        extraer segmento de 8 nucleótidos
        calcular y agregar frecuencias de A, T, G, C en el segmento a la lista
    
    crear lista de índices para cada intervalo
    
    llamar a la función graficar_int para generar y mostrar la gráfica
    
    devolver lista de frecuencias

```
#### Formato de los datos de entrada:

La secuencia de ADN se proporciona como una cadena de texto y el identificador de la 
secuencia como una cadena.

#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona secuencia e identificador
                 v
         +-----------------+
         |                 |
         | Lo que se hace: |
         |  Calcular las   |
         |   frecuencias   |
         |   en intervalos |
         +-----------------+
                 |
                 v
         +-----------------+
         |                 |
         | Lo que se hace: |
         |   Generar la    |
         |     gráfica     |
         +-----------------+

```

- **Actor**: Usuario

- **Descripción**: El usuario proporciona una secuencia de ADN y su identificador. 
El programa calcula y muestra las frecuencias de nucleótidos en intervalos de 8 
nucleótidos a lo largo de la secuencia.

- **Flujo principal**:

    1. Proporcionar la secuencia de ADN y su identificador.
    2. Agregar nucleótidos adicionales al final de la secuencia.
    3. Convertir la secuencia a mayúsculas.
    4. Calcular las frecuencias de nucleótidos en intervalos de 8 nucleótidos.
    5. Crear una lista de índices para cada intervalo.
    6. Llamar a la función graficar_int para generar y mostrar la gráfica.
    7. Devolver la lista de frecuencias calculadas. 
	
- **Flujos alternativos**: 
[Casos que salen del uso común del programa]
    - Si la secuencia está vacía o no contiene nucleótidos válidos:
        1. El programa manda un mensaje de error.
    - Si el identificador no es válido o está vacío:
        1. El programa manda un mensaje de error.
    - Argumentos inválidos desde la línea de comandos:
        1. El programa manda un mensaje de error.
    - En las pruebas unitarias se genera un mensaje de 
        error cuando:
                    1. Las frecuencias calculadas no son correctas