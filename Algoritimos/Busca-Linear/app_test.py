import unittest

def encontrar_indice(arr, x):
    for i in range(len(arr)):  # Percorre o array
        if arr[i] == x:  # Compara cada elemento com x
            return i  # Retorna o índice da primeira ocorrência
    return -1  # Retorna -1 se x não for encontrado

class TestEncontrarIndice(unittest.TestCase):
    def test_elemento_presente(self):
        self.assertEqual(encontrar_indice([3, 5, 7, 9, 5], 5), 1)  # Primeira ocorrência no índice 1

    def test_elemento_nao_presente(self):
        self.assertEqual(encontrar_indice([3, 5, 7, 9, 5], 10), -1)  # Elemento não existe

    def test_elemento_no_inicio(self):
        self.assertEqual(encontrar_indice([10, 20, 30, 40], 10), 0)  # Elemento no primeiro índice

    def test_elemento_no_fim(self):
        self.assertEqual(encontrar_indice([1, 2, 3, 4, 5], 5), 4)  # Elemento no último índice

    def test_array_vazio(self):
        self.assertEqual(encontrar_indice([], 1), -1)  # Array vazio sempre retorna -1

if __name__ == '__main__':
    unittest.main()
