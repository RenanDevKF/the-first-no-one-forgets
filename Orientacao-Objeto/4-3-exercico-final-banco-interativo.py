class ContaBancaria:
    contas = {}
    proxima_conta = 1000
    
    def __init__(self, titular, saldo=0):
        self.conta = ContaBancaria.proxima_conta
        self.titular = titular
        self.saldo = saldo
        ContaBancaria.contas[self.conta] = self
        ContaBancaria.proxima_conta += 1

    @staticmethod
    def conta_existe(conta):
        return conta in ContaBancaria.contas


class CriarConta:
    @staticmethod
    def criar_conta():
        titular = input("Digite o nome do titular: ")
        nova_conta = ContaBancaria(titular)  # Criação da conta com saldo 0
        print(f"Conta criada com sucesso! Número da sua nova conta é: {nova_conta.conta}")


class Deposito:
    @staticmethod
    def depositar():
        conta = int(input("Digite o número da conta: "))
        if not ContaBancaria.conta_existe(conta):
            print("Conta inexistente")
            return

        try:
            valor = float(input("Digite o valor a ser depositado: "))
            if valor <= 0:
                print("Valor inválido, deve ser maior que zero")
            else:
                ContaBancaria.contas[conta].saldo += valor
                print("Depósito realizado com sucesso!")
        except ValueError:
            print("Erro: Valor inválido.")


class Saque:
    @staticmethod
    def sacar():
        conta = int(input("Digite o número da conta: "))
        if not ContaBancaria.conta_existe(conta):
            print("Conta inexistente")
            return

        try:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor <= 0:
                print("Erro: O valor do saque deve ser maior que zero.")
            elif valor > ContaBancaria.contas[conta].saldo:
                print("Erro: Saldo insuficiente.")
            else:
                ContaBancaria.contas[conta].saldo -= valor
                print("Saque realizado com sucesso!")
        except ValueError:
            print("Erro: Valor inválido.")


class TransferenciaInterna:
    @staticmethod
    def transferencia():
        conta_origem = int(input("Digite o número da conta de origem: "))
        if not ContaBancaria.conta_existe(conta_origem):
            print("Conta de origem inexistente")
            return

        conta_destino = int(input("Digite o número da conta de destino: "))
        if not ContaBancaria.conta_existe(conta_destino):
            print("Conta de destino inexistente")
            return

        try:
            valor = float(input("Digite o valor a ser transferido: "))
            if valor <= 0:
                print("Erro: O valor da transferência deve ser maior que zero.")
            elif valor > ContaBancaria.contas[conta_origem].saldo:
                print("Erro: Saldo insuficiente.")
            else:
                ContaBancaria.contas[conta_origem].saldo -= valor
                ContaBancaria.contas[conta_destino].saldo += valor
                print("Transferência realizada com sucesso!")
        except ValueError:
            print("Erro: Valor inválido.")


class ExibirSaldo:
    @staticmethod
    def obter_saldo(conta):
        conta_info = ContaBancaria.contas.get(conta)
        if conta_info:
            return conta_info.saldo
        return None
    
    @staticmethod
    def exibir_saldo():
        conta = int(input("Digite o número da conta: "))
        saldo = ExibirSaldo.obter_saldo(conta)
        if saldo is None:
            print("Conta inexistente")
        else:
            print(f"Saldo da conta {conta}: R$ {saldo:.2f}")


class MenuInterativo:
    def __init__(self):
        self.opcoes = {
            1: CriarConta.criar_conta,
            2: Deposito.depositar,
            3: Saque.sacar,
            4: TransferenciaInterna.transferencia,
            5: ExibirSaldo.exibir_saldo
        }

    def exibir_menu(self):
        while True:
            print("\n==== Menu Banco ====")
            for key, nome in self.opcoes.items():
                print(f"{key} - {nome.__name__.replace('_', ' ').capitalize()}")
            print("0 - Sair")

            try:
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 0:
                    print("Saindo do sistema...")
                    break
                if opcao in self.opcoes:
                    self.opcoes[opcao]()  # Chama a função escolhida
                    input("\nPressione Enter para continuar...")  # Adiciona pausa no menu
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Erro: Digite um número válido.")
