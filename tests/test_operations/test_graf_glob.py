

# Importar la biblioteca unittest para pruebas unitarias
import unittest
# Importar la funcion patch del modulo unittest.mock para simular comportamientos durante las pruebas
from unittest.mock import patch
# Importar la clase StringIO del modulo io para manejar cadenas de texto como archivos
from io import StringIO
# Importar la funcion graficar_frecuencia_global del modulo graf_glob para probarla
from proyecto_final.operations.graf_glob import graficar_frecuencia_global

# Definir la clase de prueba unitaria que hereda de unittest.TestCase
class TestGraficarFrecuenciaGlobal(unittest.TestCase):
    """
    Clase de prueba unitaria para la funcion graficar_frecuencia_global.

    Esta clase define pruebas para verificar el correcto funcionamiento
    de la funcion graficar_frecuencia_global, que genera una grafica circular
    de la frecuencia global de nucleotidos.
    """

    # Configuracion inicial para las pruebas
    def setUp(self):
        self.frecuencia_global = {'A': 30.0, 'C': 20.0, 'T': 25.0, 'G': 25.0}

    # Metodo de prueba para verificar que la grafica de pastel es generada correctamente
    def test_grafica_generada(self):
        """
        Verifica que la grafica de pastel es generada con los datos proporcionados.
        """
        # Redirigir la salida estandar a un objeto StringIO para capturarla
        stdout = StringIO()
        with patch('sys.stdout', stdout):  # Redirigir la salida estandar al objeto StringIO
            graficar_frecuencia_global(self.frecuencia_global)  # Generar la grafica de pastel

        # Obtener la salida capturada en el objeto StringIO
        output = stdout.getvalue()

        # Verificar que la salida contiene las etiquetas y tamanos esperados
        self.assertIn("'A', 'C', 'T', 'G'", output)  # Verificar etiquetas en la salida
        self.assertIn('30.0, 20.0, 25.0, 25.0', output)  # Verificar tamanos en la salida

# Verificar si el script se esta ejecutando como el programa principal
if __name__ == '__main__':
    # Iniciar la ejecucion de las pruebas unitarias
    unittest.main()
