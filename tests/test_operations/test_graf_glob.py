
# Importar la biblioteca unittest para pruebas unitarias
import unittest  
# Importar la funcion graficar_frecuencia_global del modulo graf_glob 
from proyecto_final.operations.graf_glob import graficar_frecuencia_global  

class TestGraficarFrecuenciaGlobal(unittest.TestCase):
    """
    Clase de prueba unitaria para la funcion graficar_frecuencia_global.

    Esta clase define pruebas para verificar el correcto funcionamiento
    de la funcion graficar_frecuencia_global, que genera una grafica circular
    de la frecuencia global de nucleotidos.

    Metodos:
        test_etiquetas_correctas: Verifica que las etiquetas de la grafica sean correctas.
        test_tamanos_correctos: Verifica que los tamanos de los segmentos de la grafica sean correctos.
    """

    def setUp(self):
        """
        Configuracion inicial para las pruebas.
        """
        self.frecuencia_global = {'A': 30.0, 'C': 20.0, 'T': 25.0, 'G': 25.0}

    def test_labels_correctas(self):
        """
        Verifica que las etiquetas de la grafica sean correctas.
        """
        # Etiquetas esperadas en la grafica
        labels_esperadas = {'A', 'C', 'T', 'G'}
        # Obtener las etiquetas generadas por la funcion
        labels_generadas = set(graficar_frecuencia_global(self.frecuencia_global).get_label()) # Set crea un conjunto de etiquetas unicas

        # Verificar que las etiquetas generadas sean las esperadas
        self.assertEqual(labels_esperadas, labels_generadas)

    def test_sizes_correctos(self):
        """
        Verifica que los tamanos de los segmentos de la grafica sean correctos.
        """
        # Tamanos esperados de los segmentos de la grafica
        sizes_esperados = [30.0, 20.0, 25.0, 25.0]
        # Obtener los tamanos de los segmentos generados por la funcion
        sizes_generados = graficar_frecuencia_global(self.frecuencia_global).get_sizes()

        # Verificar que los tamanos generados sean los esperados
        self.assertEqual(sizes_esperados, sizes_generados)

if __name__ == '__main__':
    unittest.main()
