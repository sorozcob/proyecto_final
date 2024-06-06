# Proyecto final
## Descripción
Este paquete está orientado a la graficación de la frecuencia de nucleótidos en una secuencia de DNA en un archivo FASTA. Contiene dos scripts: calc_frec_nt_global.py, calcula la frecuencia de los cuatro nucleótidos de todas las secuencias en un archivo FASTA, y después las grafica en una gráfica de pastel; y calc_frec_nt_intervalo.py que toma una, varias, o todas las secuencias de un archivo FASTA y por secuencia calcula la frecuencia de los cuatro nucleótidos en intervalos de ocho nucleótidos, después grafica estas frecuencias.

## Uso
Usted puede usar el script calc_frec_nt_global.py de la siguiente manera:
    python calc_frec_nt_global.py <filename> 
    python -m proyecto_final.scripts.calc_frec_nt_global proyecto_final/utils/archivo.fasta

Usted puede usar el script calc_frec_nt_intervalo.py de la siguiente manera:
   python calc_frec_nt_intervalo.py <filename> [-i <índice(s)>]
   python calc_frec_nt_intervalo.py <filename> [--indices <índice(s)>]
   python -m proyecto_final.scripts.calc_frec_nt_intervalo proyecto_final/utils/archivo.fasta

Donde 'filename' es el nombre del archivo FASTA que contiene la secuencia de DNA. 

## Salida
El script calc_frec_nt_global.py graficará una gráfica de pastel de la frecuancia de los cuatro nucleótidos
calc_frec_nt_intervalo.py graficará la frecuencia de los cuatro nucleótidos en intervalos de ocho nucleótidos.

## Control de errores
Si el archivo no está en formato FASTA, el script generará un mensaje de error. Si el usuario ingresa un carácter inválido para el argumento nucleótidos, se imprime un mensaje de error.

## Pruebas
El script incluye un conjunto de pruebas unitarias en el directorio tests. Puede ejecutar estas pruebas con:
    python .\tests\test_operations\test_frec_nt_global.py
    python .\tests\test_operations\test_frec_nt_intervalo.py
    python .\tests\test_operations\test_graf_glob.py
    python .\tests\test_operations\test_graf_int.py

## Datos
El script está diseñado para operar en un archivo FASTA, con un identificador por secuencia de nucleótidos. No hay restricciones en el número de letras en el archivo.

## Metadatos y documentación
Este README ofrece información de uso básico.

## Código fuente
El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso
Este script está disponible bajo la licencia [MIT License]. Consulte el archivo LICENSE para obtener más detalles.

## Como citar
Si utiliza este script en su trabajo, por favor cite: [https://github.com/sorozcob/proyecto_final].

## Contáctenos
Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [ximenagp@lcg.unam.mx] o [santiago@lcg.unam.mx].