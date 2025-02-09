class ContaBancaria:
    
    contas = {}
    proxima_conta = 1000
    
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo
        ContaBancaria.contas[conta] = {"titular": titular, "saldo": saldo}
    
class CriarConta:
    
    @staticmethod
    def criar_conta():
        titular = input("Digite o nome do titular: ")
        conta = ContaBancaria.proxima_conta
        ContaBancaria.proxima_conta += 1
        ContaBancaria.contas[conta] = {"titular": titular, "saldo": 0}        
        print(f"Conta criada com sucesso! Numero da sua nova conta é: {conta}")
    
class Deposito:
    
    @staticmethod
    def depositar():
        conta = int(input("Digite o numero da conta: "))
        if conta not in ContaBancaria.contas:
            print("Conta inexistente")
        else:
            valor = float(input("Digite o valor a ser depositado: "))
            if valor <= 0:
                print("Valor inválido, o valor de deposito deve ser maior que zero")
            else:
                ContaBancaria.contas[conta]["saldo"] += valor
                print("Deposito realizado com sucesso!")
                
class Saque:
    @staticmethod
    def sacar():
        conta = int(input("Digite o número da conta: "))
        if conta not in ContaBancaria.contas:
            print("Conta inexistente")
        else:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor <= 0:
                print("Erro: O valor do saque deve ser maior que zero.")
            elif valor > ContaBancaria.contas[conta]["saldo"]:
                print("Erro: Saldo insuficiente.")
            else:
                ContaBancaria.contas[conta]["saldo"] -= valor
                print("Saque realizado com sucesso!")

class TransferenciaInterna:
    @staticmethod
    def transferencia():
        conta_origem = int(input("Digite o número da conta de origem: "))
        if conta_origem not in ContaBancaria.contas:
            print("Conta de origem inexistente")
        else:
            conta_destino = int(input("Digite o número da conta de destino: "))
            if conta_destino not in ContaBancaria.contas:
                print("Conta de destino inexistente")
            else:
                valor = float(input("Digite o valor a ser transferido: "))
                if valor <= 0:
                    print("Erro: O valor da transferência deve ser maior que zero.")
                elif valor > ContaBancaria.contas[conta_origem]["saldo"]:
                    print("Erro: Saldo insuficiente.")
                else:
                    ContaBancaria.contas[conta_origem]["saldo"] -= valor
                    ContaBancaria.contas[conta_destino]["saldo"] += valor
                    print("Transferência realizada com sucesso!")
                    
class ExibirSaldo:
    
    @staticmethod    
    def exibir_saldo():
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

        self.nomes_opcoes = {
            1: "Criar Conta",
            2: "Depositar",
            3: "Sacar",
            4: "Transferir",
            5: "Exibir Saldo"
        }

    def exibir_menu(self):
        while True:
            print("\n==== Menu Banco ====")
            for key, nome in self.nomes_opcoes.items():
                print(f"{key} - {nome}")
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
  
  
      