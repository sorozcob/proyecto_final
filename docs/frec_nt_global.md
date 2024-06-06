# calculate_at_content

Fecha: 15/05/2024

**Participantes**:

- [Santiago Orozco] < [santiago@lcg.unam.mx] >

## Descripción del Problema

calculate_at_content es un módulo que toma un archivo de texto con una secuencia de nucleótidos desde la lína de comandos 
y calcula la cantidad de adeninas y timinas que hay en la secuencia, y lo regresa relacionandolo con el número de nucleótidos
totales. Tiene la opción de normalizar el contenido de AT en caso de que haya 'N's en la secuencia.



## Especificación de Requisitos

Requisitos funcionales
- Se necesitan las funciones de la librería argparse.
- Aceptará un archivo desde línea de comandos. En calculate_codon_frequency en scripts
- Lee un archivo dado en formato string, solo acepta archivos con los caracteres a, t, g y c en mayúsculas o minúsculas. En calculate_codon_frequency en scripts y función read_dna_sequence en file_io.py en utils
- Cuenta cuantas veces aparece la letra A, T y lo divide entre en número total de nucleótidos. Función codon_frequency en operations
- Puede normalizar el contenido de AT en caso de que haya N's (representa a cuelquier nucleótido) en la secuencia. Función codon_frequency en operations
- Imprime el contenido de AT. En calculate_codon_frequency en scripts

Requisitos no funcionales

- El script deberá estar escrito en Python.
- El script es de tipo CLI
- El tiempo de respuesta debe ser rápido, incluso con archivos de gran tamaño.
- 

## Análisis y Diseño


```
Función principal:
    Pide los argumentos por línea de comandos
    Lee la secuencia de nucleótidos
    Llama a la función read_dna_sequence de utils:
        
        
    Inicializar los contadores para cada letra
    Abrir el archivo en modo lectura 
    Iterar sobre cada línea del archivo
    Convertir la línea a minúsculas para contar sin distinción de mayúsculas/minúsculas
    Iterar sobre cada caracter de la línea
    Incrementar el contador correspondiente si el caracter es una de las letras a contar
    Imprimir los resultados de los contadores

```



#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo
                 v
         +-------+-------+
         |  Calculador   |
         |  del contenido|
         |  de a y t en  |
         |  la secuencia |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El usuario proporciona un archivo de entrada con una secuencia de nucleótidos. El programa cuenta el número de repeticiones de cada nucleótido.
- **Flujo principal**:

	1. Abre y lee el archivo llamado "archivo.txt" 
	2. Se recorre el arcivo caracter por carecter 
	3. Se utiliza la función count para contadar el símbolo que aparece
        4. Imprime el número de repeticines por cada nucleótido
	
- **Flujos alternativos**: [Casos que salen del uso común del programa]
        - Si el archivo es inexistente
                1. El programa manda un mensaje de error

	- Si el archivo está vacío
		1. El programa manda un mensaje de error

        - Si el archivo contiene caracteres inválidos
                1. El programa manda un mensaje de error

        - Argumentos inválidos de -n (distintos a ATGC)
                1. El programa manda un mensaje de error 
