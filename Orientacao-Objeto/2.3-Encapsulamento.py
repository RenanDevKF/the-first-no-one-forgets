"""
Encapsulamento é o conceito de restringir o acesso direto aos atributos e métodos de um objeto, permitindo que o acesso seja controlado através de métodos específicos.

Isso evita que o estado interno do objeto seja alterado de forma indevida e melhora a segurança e manutenção do código.

Em termos simples:

Protegemos os dados de acessos externos indesejados.
Controlamos como os dados podem ser modificados.

self.saldo = pode seracessado por qualquer parte do codigo
self._saldo = Pode ser acessado, mas indica que nao deveria ser modificado diretamente
self__saldo = Só pode ser acessado dentro da propia classe

conta = ContaBancaria("Renan", 500)
print(conta.__saldo)  # ❌ Isso vai gerar um erro!
conta.exibir_saldo()  # ✅ Isso funciona!
conta.__saldo = 10000  # ❌ Isso não funciona!
conta.exibir_saldo()   # Ainda exibe o saldo original

"""

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular   # Público
        self.__saldo = saldo     # Privado (não pode ser acessado diretamente)
    
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
    
    def exibir_saldo(self):
        print(f"Olá {self.titular}, seu saldo atual é R$ {self.__saldo:.2f}")
        
"""
        Criando Métodos "Getter" e "Setter"
Para permitir acesso controlado, usamos métodos especiais:

Getter (get_saldo) → Obtém o saldo de forma segura.
Setter (set_saldo) → Permite alterar o saldo com validação.
"""
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def get_saldo(self):  # Getter
        return self.__saldo
    
    def set_saldo(self, novo_saldo):  # Setter
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Erro! O saldo não pode ser negativo.")

# Agora podemos acessar e modificar o saldo de forma segura:

conta = ContaBancaria("Sarah", 300)

print(conta.get_saldo())  # ✅ Obtém o saldo

conta.set_saldo(500)  # ✅ Altera o saldo de forma controlada
print(conta.get_saldo())  # Mostra o saldo atualizado

conta.set_saldo(-100)  # ❌ Mensagem de erro, pois saldo negativo não é permitido

