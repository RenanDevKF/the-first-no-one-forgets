class ContaBancaria:
    
    contas = {}
    
def __init__(self, titular, conta, saldo):
    self.titular = titular
    self.conta = conta
    self.saldo = saldo
    ContaBancaria.contas[conta] = titular