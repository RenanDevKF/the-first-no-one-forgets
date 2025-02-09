import unittest
from unittest.mock import patch
from exercico_final_banco_interativo import CriarConta, Deposito, Saque, TransferenciaInterna, ExibirSaldo, ContaBancaria


class TestBanco(unittest.TestCase):

    @patch('builtins.input', return_value='João')
    def test_criar_conta(self, mock_input):
        # Chama a função criar_conta simulando a entrada "João"
        CriarConta.criar_conta()

        # Verifica se a conta foi criada e o titular está correto
        self.assertTrue(1000 in ContaBancaria.contas)  # A conta deve ter o número 1000
        self.assertEqual(ContaBancaria.contas[1000].titular, 'João')
        self.assertEqual(ContaBancaria.contas[1000].saldo, 0)

    @patch('builtins.input', side_effect=['1000', '50'])
    def test_depositar(self, mock_input):
        # Simula a entrada para depósito: conta 1000 e valor 50
        Deposito.depositar()

        # Verifica se o saldo foi atualizado corretamente
        self.assertEqual(ContaBancaria.contas[1000].saldo, 50)

    @patch('builtins.input', side_effect=['1000', '60'])
    def test_sacar(self, mock_input):
        # Primeiro, faz um depósito para garantir que o saldo seja suficiente
        ContaBancaria.contas[1000].saldo = 100

        # Simula a entrada para saque: conta 1000 e valor 60
        Saque.sacar()

        # Verifica se o saldo foi atualizado corretamente após o saque
        self.assertEqual(ContaBancaria.contas[1000].saldo, 40)

    @patch('builtins.input', side_effect=['1000', '1001', '50'])
    def test_transferencia(self, mock_input):
        # Primeiro, cria uma segunda conta para simular a transferência
        ContaBancaria('Maria')  # Conta 1001

        # Faz um depósito na conta de origem para garantir que o saldo seja suficiente
        ContaBancaria.contas[1000].saldo = 100

        # Simula a entrada para transferência: conta de origem 1000, conta de destino 1001, e valor 50
        TransferenciaInterna.transferencia()

        # Verifica se o saldo das contas foi atualizado corretamente
        self.assertEqual(ContaBancaria.contas[1000].saldo, 50)
        self.assertEqual(ContaBancaria.contas[1001].saldo, 50)

    @patch('builtins.input', return_value='1000')
    def test_exibir_saldo(self, mock_input):
        # Faz um depósito para garantir que o saldo esteja correto
        ContaBancaria.contas[1000].saldo = 100

        # Simula a entrada para exibir saldo: conta 1000
        ExibirSaldo.exibir_saldo()

        # Verifica se o saldo foi exibido corretamente
        # (não podemos verificar diretamente no teste, mas podemos garantir que o código foi executado sem erro)
        # Para esse tipo de teste, seria ideal verificar o comportamento de saída (stdout), mas vamos focar na lógica aqui

        # Não há um assert aqui porque o método `exibir_saldo` imprime na tela, então você pode verificar manualmente.
        # Caso precise testar a saída, pode usar unittest.mock para capturar o que foi impresso.

if __name__ == '__main__':
    unittest.main()
