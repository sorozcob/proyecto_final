import unittest
# Se importa leer_fasta del archivo file_io 
from proyecto_final.operations.frec_nt_intervalo import frecuencia_nt_intervalo
class TestATContent(unittest.TestCase):
    """
    Clase de pruebas unitarias para la función `frecuencia_nt_intervalo` del 
    módulo `frec_nt_intervalo`.
    
    Esta clase contiene métodos para probar el correcto funcionamiento de 
    la función
    
    Métodos:
        test_frec_nt_intervalo: Prueba varios casos para asegurar el correcto 
        comportamiento de la función `frecuencia_nt_intervalo`.
    """

    def test_calculate_at_content(self):
        self.assertEqual(frecuencia_nt_intervalo("ATC"), [[0.125, 0.0, 0.0], [0.125, 0.125, 0.0], [0.0, 0.0, 0.0], [0.125, 0.125, 0.125]])
        self.assertEqual(frecuencia_nt_intervalo("AAAA"), [[0.5, 0.375, 0.25, 0.125], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]])
        self.assertEqual(frecuencia_nt_intervalo("TGAAC"), [[0.25, 0.25, 0.25, 0.125, 0.0], [0.125, 0.0, 0.0, 0.0, 0.0], [0.125, 0.125, 0.0, 0.0, 0.0], [0.125, 0.125, 0.125, 0.125, 0.125]])

if __name__ == '__main__':
    unittest.main()