import unittest
# Se importa leer_fasta del archivo file_io 
from proyecto_final.operations.graf_int import graficar_int
class TestATContent(unittest.TestCase):
    """
    Clase de pruebas unitarias para la función `graficar_int` del 
    módulo `graf_int`.
    
    Esta clase contiene métodos para probar el correcto funcionamiento de 
    la función.
    
    Métodos:
        test_graf_int: Prueba varios casos para asegurar el correcto 
        comportamiento de la función `graficar_int`.
    """

    def test_calculate_at_content(self):
        self.assertEqual(graficar_int([[0.125, 0.0, 0.0], [0.125, 0.125, 0.0], [0.0, 0.0, 0.0], [0.125, 0.125, 0.125]]), [[0.125, 0.0, 0.0], [0.125, 0.125, 0.0], [0.0, 0.0, 0.0], [0.125, 0.125, 0.125]])
        self.assertEqual(graficar_int([[0.5, 0.375, 0.25, 0.125], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]), [[0.5, 0.375, 0.25, 0.125], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]])
        self.assertEqual(graficar_int([[0.25, 0.25, 0.25, 0.125, 0.0], [0.125, 0.0, 0.0, 0.0, 0.0], [0.125, 0.125, 0.0, 0.0, 0.0], [0.125, 0.125, 0.125, 0.125, 0.125]]), [[0.25, 0.25, 0.25, 0.125, 0.0], [0.125, 0.0, 0.0, 0.0, 0.0], [0.125, 0.125, 0.0, 0.0, 0.0], [0.125, 0.125, 0.125, 0.125, 0.125]])

if __name__ == '__main__':
    unittest.main()