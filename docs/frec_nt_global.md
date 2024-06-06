# Módulo frec_nt_global

Fecha: 05/06/2024

**Participantes / Autores**:

- [Santiago Orozco Barrera] < [santiago@lcg.unam.mx] >
- [Karla Ximena González Platas] <[ximenagp@lcg.unam.mx]>

## Descripción del Problema

frec_nt_global es un módulo en Python que calcula la frecuencia de nucleótidos en 
cada secuencia de ADN proporcionada por un archivo en formato fasta y calcula la 
frecuencia global de cada nucleótido en términos de porcentaje. Adicionalmente, se 
desea implementar una clase de pruebas unitarias para verificar la correcta 
funcionalidad del módulo.


## Especificación de Requisitos

#### Requisitos funcionales:

        1. El script debe importar un modulo para contar elementos.

        2. El módulo debe leer secuencias de ADN proporcionadas en un diccionario.

        3. Debe calcular la frecuencia de nucleótidos ('A', 'C', 'T', 'G') para cada 
        secuencia.

        4. Debe calcular la frecuencia global de nucleótidos en términos de porcentaje.

        5. Debe proporcionar resultados en formato de diccionarios, uno para frecuencias 
        por secuencia y otro para la frecuencia global.

        6. El módulo debe incluir pruebas unitarias que verifiquen la correcta 
        funcionalidad de la función principal.

#### Requisitos no funcionales: 

        - El script deberá estar escrito en Python.
        - El tiempo de respuesta debe ser rápido, incluso con archivos de gran tamaño.
        - El módulo debe ser eficiente y manejar grandes cantidades de datos sin problemas.
        - Debe ser fácil de usar y mantener.
        - Debe seguir las mejores prácticas de codificación y estructura de proyectos en Python.
- 

## Análisis y Diseño

La resolución del problema sigue una metodología sencilla basada en la recolección de datos, el 
procesamiento de esos datos para calcular las frecuencias de nucleótidos, y la presentación de los 
resultados. Se utilizará la biblioteca collections de Python para contar los nucleótidos.

#### Pseudocódigo

Pseudocógido simple que ilustra la lógica básica del modulo:

```
def frec_nt_global(secuencias):
    inicializar diccionarios para frecuencias por secuencia y frecuencia global
    inicializar contador de nucleótidos totales
    
    para cada secuencia en secuencias:
        contar nucleótidos en la secuencia actual
        actualizar frecuencias por secuencia y frecuencia global
        actualizar contador total de nucleótidos
    
    calcular porcentaje de frecuencias globales
    devolver frecuencias por secuencia y frecuencia global

```
#### Formato de los datos de entrada:

Las secuencias de ADN se proporcionarán en un diccionario donde las claves son identificadores de 
secuencias y los valores son las secuencias de ADN en formato de cadena de texto.

#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-----------------+
         |                 |
         | Lo que se hace: |
         |  Calcular las   |
         |   frecuencias   |
         +-----------------+

```

- **Actor**: Usuario

- **Descripción**: El usuario proporciona un archivo de entrada con secuencias de ADN en formato fasta. 
El programa calcula y muestra las frecuencias de nucleótidos por secuencia y la frecuencia global de 
cada nucleótido.

- **Flujo principal**:

        1. Proporcionar el archivo de entrada con secuencias de ADN.
        2. Leer las secuencias del archivo.
        3. Calcular las frecuencias de nucleótidos por secuencia.
        4. Calcular la frecuencia global de nucleótidos en términos de porcentaje.
        5. Imprimir los resultados. 
	
- **Flujos alternativos**: 

	- Si el archivo está vacío
		El programa manda un mensaje de error

        - Si el archivo contiene caracteres inválidos
                El programa manda un mensaje de error

        - Argumentos inválidos de -n (distintos a ATGC)
                El programa manda un mensaje de error 

        - En las pruebas unitarias se genera un mensaje de 
        error cuando:
                Las frecuencias globales no sumen aproximadamente 100%.
                Las frecuencias por secuencia no sean calculadas correctamente.
