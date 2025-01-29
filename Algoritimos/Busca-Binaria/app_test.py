import unittest     
import app2

class TestBuscaBinaria(unittest.TestCase):

    def test_elemento_presente(self):
        """Teste para verificar se um número presente no array é encontrado"""
        arr = [2, 3, 4, 10, 40]
        x = 10
        resultado = app2.busca_binaria(arr, 0, len(arr) - 1, x)
        self.assertEqual(resultado, 3)  # Índice esperado

    def test_elemento_ausente(self):
        """Teste para um número que não está no array"""
        arr = [2, 3, 4, 10, 40]
        x = 5
        resultado = app2.busca_binaria(arr, 0, len(arr) - 1, x)
        self.assertEqual(resultado, -1)  # Deve retornar -1

    def test_primeiro_elemento(self):
        """Teste para verificar se encontra o primeiro elemento"""
        arr = [2, 3, 4, 10, 40]
        x = 2
        resultado = app2.busca_binaria(arr, 0, len(arr) - 1, x)
        self.assertEqual(resultado, 0)  # Primeiro índice

    def test_ultimo_elemento(self):
        """Teste para verificar se encontra o último elemento"""
        arr = [2, 3, 4, 10, 40]
        x = 40
        resultado = app2.busca_binaria(arr, 0, len(arr) - 1, x)
        self.assertEqual(resultado, 4)  # Último índice

    def test_array_vazio(self):
        """Teste para um array vazio"""
        arr = []
        x = 10
        resultado = app2.busca_binaria(arr, 0, len(arr) - 1, x)
        self.assertEqual(resultado, -1)  # Array vazio deve retornar -1

    def test_array_um_elemento_presente(self):
        """Teste para um array de um único elemento que contém x"""
        arr = [10]
        x = 10
        resultado = app2.busca_binaria(arr, 0, len(arr) - 1, x)
        self.assertEqual(resultado, 0)  # Deve retornar índice 0

    def test_array_um_elemento_ausente(self):
        """Teste para um array de um único elemento que NÃO contém x"""
        arr = [10]
        x = 5
        resultado = app2.busca_binaria(arr, 0, len(arr) - 1, x)
        self.assertEqual(resultado, -1)  # Deve retornar -1

if __name__ == '__main__':
    unittest.main()