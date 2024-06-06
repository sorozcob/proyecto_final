# Casos de prueba o escenarios

Este documento describe los casos de prueba para el paquete de Python, está orientado a la graficación de la frecuencia de nucleótidos en una secuencia de DNA en un archivo FASTA. El objetivo de estas pruebas es validar y garantizar que el paquete funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

calc_frec_nt_global.py, calcula la frecuencia de los cuatro nucleótidos de todas las secuencias en un archivo FASTA, y después las grafica en una gráfica de pastel; y calc_frec_nt_intervalo.py que toma una, varias, o todas las secuencias de un archivo FASTA y por secuencia calcula la frecuencia de los cuatro nucleótidos en intervalos de ocho nucleótidos, después grafica estas frecuencias.

Los casos de prueba están dirigidos al formato del archivo de input.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

    
### Caso de prueba 1 (Excepción): Comprobación de error cuando el formato del archivo de entrada no es FASTA

- Descripción: Verificar que el script reconozca cuando el archivo de entrada esté en un formato no adecuado
- Datos de entrada: test1.txt

**calc_frec_nt_global.py**
```
python -m proyecto_final.scripts.calc_frec_nt_global proyecto_final/utils/test1.txt
```
- Resultado esperado: 
  Mensaje de error

**calc_frec_nt_intervalo.py**
```
python -m proyecto_final.scripts.calc_frec_nt_intervalo proyecto_final/utils/test1.txt
```
- Resultado esperado: 
  Mensaje de error

### Caso de prueba 2 (Excepción): Comprobación de error cuando el usuario pasa el archivo con caracteres inválidos

- Descripción: Verificar que el script reconozca cuando las secuencias tengan caracteres inválidos, caracteres diferentes de A, T, C, G, N.
- Datos de entrada: test2.txt

**calc_frec_nt_global.py**
```
python -m proyecto_final.scripts.calc_frec_nt_global proyecto_final/utils/test2.txt
```
- Resultado esperado: 
  Mensaje de error

**calc_frec_nt_intervalo.py**
```
python -m proyecto_final.scripts.calc_frec_nt_intervalo proyecto_final/utils/test2.txt
```
- Resultado esperado: 
  Mensaje de error

### Caso de prueba 3: Comprobación de formato FASTA del archivo de entrada

- Descripción: Verificar que el script reconozca cuando el archivo de entrada esté en el formato adecuado
- Datos de entrada: archivo.fasta

**calc_frec_nt_global.py**
```
python -m proyecto_final.scripts.calc_frec_nt_global proyecto_final/utils/archivo.fasta
```
- Resultado esperado: 
  Mensaje de error
**calc_frec_nt_intervalo.py**
```
python -m proyecto_final.scripts.calc_frec_nt_intervalo proyecto_final/utils/archivo.fasta
```
- Resultado esperado: 
  Mensaje de error