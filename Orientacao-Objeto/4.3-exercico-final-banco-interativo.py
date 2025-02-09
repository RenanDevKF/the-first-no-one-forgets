class ContaBancaria:
    
    contas = {}
    proxima_conta = 1000
    
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo
        ContaBancaria.contas[conta] = {"titular": titular, "saldo": saldo}
    
class CriarConta:
    
    def criar_conta(self):
        titular = input("Digite o nome do titular: ")
        conta = ContaBancaria.proxima_conta+len
        ContaBancaria.proxima_conta += 1
        self.conta_bancaria.titular = titular
        self.conta_bancaria.conta = conta
        self.conta_bancaria.saldo = 0
        ContaBancaria.contas[conta] = {"titular": titular, "saldo": 0}
        ContaBancaria.proxima_conta += 1
        return conta
    
class Deposito:
    

    def depositar(self):
        conta = int(input("Digite o numero da conta: "))
        if conta not in ContaBancaria.contas:
            print("Conta inexistente")
        else:
            valor = float(input("Digite o valor a ser depositado: "))
            if valor < 0:
                print("Valor inválido, o valor de deposito deve ser maior que zero")
            else:
                ContaBancaria.contas[conta]["saldo"] += valor
                print("Deposito realizado com sucesso!")
                
class Saque:
    

    def sacar(self):
        conta = int(input("Digite o numero da conta: "))
        if conta not in ContaBancaria.contas:
            print("Conta inexistente")
        else:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor < 0 or valor > ContaBancaria.contas[conta]["saldo"]:
                print("Saldo insuficiente")
            else:
                ContaBancaria.contas[conta]["saldo"] -= valor   
                print("Saque realizado com sucesso!")

class TransferenciaInterna:
    
        
    def transferencia(self):
        conta_origem = int(input("Digite o numero da conta de origem: "))
        if conta_origem not in ContaBancaria.contas:
            print("Conta de origem inexistente")
        else:
            conta_destino = int(input("Digite o numero da conta de destino: "))
            if conta_destino not in ContaBancaria.contas:
                print("Conta de destino inexistente")
            else:
                valor = float(input("Digite o valor a ser transferido: "))
                if valor < 0 or valor > ContaBancaria.contas[conta_origem]["saldo"]:
                    print("Saldo insuficiente")
                else:
                    ContaBancaria.contas[conta_origem]["saldo"] -= valor
                    ContaBancaria.contas[conta_destino]["saldo"] += valor
                    print("Transferencia realizada com sucesso!")
                    
class ExibirSaldo:
    
        
    def exibir_saldo(self):
        conta = int(input("Digite o numero da conta: "))
        if conta not in ContaBancaria.contas:
            print("Conta inexistente")
        else:
            print(f"Saldo da conta {conta}: R$ {ContaBancaria.contas[conta]['saldo']:.2f}")
            
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
            print("\n1 - Criar Conta")
            print("2 - Depositar")
            print("3 - Sacar")
            print("4 - Transferir")
            print("5 - Exibir Saldo")
            print("0 - Sair")

            try:
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 0:
                    print("Saindo do sistema...")
                    break
                elif opcao in self.opcoes:
                    self.opcoes[opcao]()
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")        