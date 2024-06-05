"""

calc_frec_nt_global.py: Script para calcular la frecuencia por secuencia y global de nucleotidos y 
generar una grafica circular en terminos de porcentaje. 

Este script lee una secuencia de ADN desde un archivo en formato FASTA y calcula la frecuencia de 
cada nucleotido por secuencia y la frecuencia global de los nucleotidos, ademas genera una grafica 
circular (o de pastel) de la frecuencia global en terminos de porcentaje. 
Las secuencias de ADN deben estar en un archivo en formato FASTA. 

Uso:
    python calc_frec_nt_global.py <filename> 

Argumentos:
    <filename> : nombre del archivo fasta que contiene la secuencia de ADN.

"""

# ===========================================================================
# =                            Imports
# ===========================================================================

# Importar libreria argparse
import argparse
# Importar la funcion frec_nt_global del modulo frec_nt_global
from proyecto_final.operations.frec_nt_global import frec_nt_global
# Importar la funcion graficar_frecuencia_global del modulo graf_glob
from proyecto_final.operations.graf_glob import graficar_frecuencia_global
# Importar la funcion leer_fasta del modulo file_io
from proyecto_final.utils.file_io import leer_fasta

# ===========================================================================
# =                            Main
# ===========================================================================

def main():

    # Definir argumentos
    parser = argparse.ArgumentParser(description="Programa para calcular la frecuencia global de nucleotidos y generar una grafica circular")
    parser.add_argument("filename", help="Nombre del archivo FASTA")
    # Parsear argumentos 
    args = parser.parse_args()
    
    try: # Permite manejar posibles excepciones durante la ejecucion del programa
        # Llamar a funciones
        fasta_secuencias = leer_fasta(args.filename) # Leer el archivo fasta
        frecuencias_por_secuencia, frecuencia_global = frec_nt_global(fasta_secuencias) # Calcular frecuencias
        
        # Imprimir frecuencias
        print("Frecuencias por secuencia:")
        for id, frecuencias in frecuencias_por_secuencia.items():
            print(f"ID: {id}, Frecuencias: {frecuencias}")
        
        print("\nFrecuencia global de nucleotidos:")
        for nuc, frecuencia in frecuencia_global.items():
            print(f"{nuc}: {frecuencia:.2f}%")
        
        # Generar la grafica circular de frecuencia global
        graficar_frecuencia_global(frecuencia_global)
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
