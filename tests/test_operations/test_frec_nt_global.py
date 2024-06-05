
# Importacion de la biblioteca unittest para pruebas unitarias
import unittest
# Importacion de la funcion frec_nt_global desde el modulo frec_nt_global
from proyecto_final.operations.frec_nt_global import frec_nt_global

class TestFrecuenciaNtGlobal(unittest.TestCase):
    """
    Clase de pruebas unitarias para la funcion frec_nt_global.

    Esta clase define pruebas para verificar el correcto funcionamiento
    de la funcion frec_nt_global, que calcula la frecuencia de nucleotidos
    en secuencias de ADN.

    Metodos:
        test_suma_100_por_ciento: Verifica que las frecuencias globales sumen 100%.
        test_frecuencias_por_secuencia: Verifica que las frecuencias por secuencia sean correctas.
    """

    def test_suma_100_por_ciento(self):
        """
        Verifica que las frecuencias globales sumen aproximadamente 100%.

        Se generan secuencias de ADN ficticias y se calculan las frecuencias.
        Luego se verifica que la suma de las frecuencias globales sea aproximadamente
        100% con una pequena tolerancia (delta).
        """
        secuencias = {
            "secuencia1": "ATCGATCGATCG",
            "secuencia2": "GCTAGCTAGCTA",
            "secuencia3": "ATAGCTAGCTAG",
        }
        frecuencias_por_secuencia, frecuencia_global = frec_nt_global(secuencias)
        
        suma_frecuencias = sum(frecuencia_global.values())
        # Verifica que dos valores sean aproximadamente iguales dentro de una tolerancia especificada
        self.assertAlmostEqual(suma_frecuencias, 100, delta=0.01)

    def test_frecuencias_por_secuencia(self):
        """
        Verifica que las frecuencias por secuencia sean calculadas correctamente.

        Se generan secuencias de ADN ficticias y se calculan las frecuencias.
        Luego se verifica que las frecuencias por secuencia sean las esperadas.
        """
        secuencias = {
            "secuencia1": "ATCGATCGATCG",
            "secuencia2": "GCTAGCTAGCTA",
            "secuencia3": "ATAGCTAGCTAG",
        }
        frecuencias_por_secuencia, frecuencia_global = frec_nt_global(secuencias)
        
        # Verificar que dos valores sean iguales
        self.assertEqual(frecuencias_por_secuencia['secuencia1']['A'], 3)
        self.assertEqual(frecuencias_por_secuencia['secuencia2']['C'], 3)
        self.assertEqual(frecuencias_por_secuencia['secuencia3']['G'], 3)

if __name__ == '__main__':
    unittest.main()
