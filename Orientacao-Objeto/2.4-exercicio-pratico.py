class ContaBancaria:
    
    def __init__(self, titular, saldo, data_abertura):
        if saldo < 200:
            raise ValueError("Saldo inicial deve ser no mínimo R$ 200,00")
        
        self.titular = titular
        self.__saldo = saldo
        self._data_abertura = data_abertura
        
    def get_saldo(self):
        return self.__saldo
        
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Erro! O saldo não pode ser negativo.")
    
    def get_data_abertura(self):
        return self._data_abertura
    
    def set_data_abertura(self, nova_data):
        self._data_abertura = nova_data    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado! Novo saldo: R$ {self.__saldo:.2f}")
        else:
            print("Depósito inválido! O valor precisa ser maior que zero.")
                
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado! Novo saldo: R$ {self.__saldo:.2f}")
        else:
            print("Saque não permitido! Saldo insuficiente.")
    def transferencia(self, conta_destino, valor):
        if self == conta_destino:
            print("Não é possível transferir para a própria conta.")
            return
        
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R$ {valor:.2f} realizada para {conta_destino.titular}. Novo saldo: R$ {self.__saldo:.2f}")
        else:
            print("Transferência não permitida! Saldo insuficiente.")
            
    def exibir_saldo(self):
        print(f"Olá {self.titular}, seu saldo atual é R$ {self.__saldo:.2f}")
        
    def exibir_dados(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.__saldo:.2f} | Data de Abertura: {self._data_abertura}")

    # Exemplo de uso:
conta1 = ContaBancaria("João", 500, "06/02/2025")
conta2 = ContaBancaria("Maria", 300, "06/02/2025")

conta1.transferencia(conta2, 100)
conta1.exibir_dados()
conta2.exibir_dados()