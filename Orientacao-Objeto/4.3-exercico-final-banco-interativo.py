class ContaBancaria:
    
    contas = {}
    proxima_conta = 1000
    
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo
        ContaBancaria.contas[conta] = {"titular": titular, "saldo": saldo}
    
class CriarConta:
    def __init__(self):
        self.conta_bancaria = ContaBancaria(None, None, None)

    def criar_conta(self):
        titular = input("Digite o nome do titular: ")
        conta = ContaBancaria.proxima_conta+len(ContaBancaria.contas)
        self.conta_bancaria.titular = titular
        self.conta_bancaria.conta = conta
        self.conta_bancaria.saldo = 0
        ContaBancaria.contas[conta] = {"titular": titular, "saldo": 0}
        ContaBancaria.proxima_conta += 1
        return conta
    
class Deposito:
    def __init__(self):
        self.conta_bancaria = ContaBancaria(None, None, None)

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
    def __init__(self):
        self.conta_bancaria = ContaBancaria(None, None, None)

    def sacar(self):
        conta = int(input("Digite o numero da conta: "))
        if conta not in ContaBancaria.contas:
            print("Conta inexistente")
        else:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor < 0 and valor > ContaBancaria.contas[conta]["saldo"]:
                print("Saldo insuficiente")
            else:
                ContaBancaria.contas[conta]["saldo"] -= valor   
                print("Saque realizado com sucesso!")

class TransferenciaInterna:
    def __init__(self):
        self.conta_bancaria = ContaBancaria(None, None, None)
        
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
                if valor < 0 and valor > ContaBancaria.contas[conta_origem]["saldo"]:
                    print("Saldo insuficiente")
                else:
                    ContaBancaria.contas[conta_origem]["saldo"] -= valor
                    ContaBancaria.contas[conta_destino]["saldo"] += valor
                    print("Transferencia realizada com sucesso!")           