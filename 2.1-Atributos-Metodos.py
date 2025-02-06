# Continuacao Aula 02
# Atributos e Metodos

# Teoria sobre Atributos

"""
Tipos de Atributos:
- Atributos de Instância (mais comuns)
-- São específicos de cada objeto.
--Definidos dentro do método __init__().

-Atributos de Classe
--Compartilhados entre todas as instâncias de uma classe.
--Definidos diretamente dentro da classe (fora de __init__()).

Vide exeplo do arquivo 02-Denifinica-classe
"""
# Exemplo de Atributos de Classe

class Pessoa:
    especie = "Humano"  # Atributo de classe (compartilhado)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando objetos
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

print(pessoa1.especie)  # Saída: Humano
print(pessoa2.especie)  # Saída: Humano

# Alterando o atributo de classe
Pessoa.especie = "Ser Vivo"

print(pessoa1.especie)  # Saída: Ser Vivo
print(pessoa2.especie)  # Saída: Ser Vivo

# Teoria sobre Metodos

"""
Os métodos são funções dentro da classe que definem comportamentos dos objetos. Eles são chamados a partir de um objeto e podem acessar/modificar atributos.

Tipos de Métodos
1. Métodos de Instância

- Definidos com self.
- Podem acessar e modificar atributos do objeto.

2. Métodos de Classe

- Definidos com @classmethod e cls.
- Podem modificar atributos de classe.

3. Métodos Estáticos

- Definidos com @staticmethod.
- Não acessam atributos de instância ou de classe diretamente.
"""

# Por que usar @classmethod e nao pessoa.especie = "Alien"? ou pessoa1.especie = "Alien"?
class Pessoa:
    especie = "Humano"

    @classmethod
    def mudar_especie(cls, nova_especie):
        cls.especie = nova_especie

# Criando objetos
pessoa1 = Pessoa()
pessoa2 = Pessoa()

# Chamando o método de classe a partir de um objeto
pessoa1.mudar_especie("Alien")

print(pessoa1.especie)  # Saída: Alien
print(pessoa2.especie)  # Saída: Alien
print(Pessoa.especie)   # Saída: Alien


"""
- Se precisar alterar o atributo da classe de qualquer lugar (objeto ou classe), @classmethod é a melhor opção.
- Se for apenas um ajuste pontual, modificar Pessoa.especie diretamente também funciona.
- Se modificar via objeto (pessoa1.especie = "Alien"), um novo atributo de instância será criado e não alterará os outros objetos.

- Abaixo segue outro exemplo a respeito da utilização de multiplos metodos de classe diferentes.
"""
class Usuario:
    nivel_acesso = "Básico"
    usuarios_online = 0

    @classmethod
    def mudar_nivel_acesso(cls, novo_nivel):
        cls.nivel_acesso = novo_nivel

    @classmethod
    def adicionar_usuario(cls):
        cls.usuarios_online += 1

    @classmethod
    def remover_usuario(cls):
        if cls.usuarios_online > 0:
            cls.usuarios_online -= 1

    @classmethod
    def mostrar_status(cls):
        print(f"Nível de Acesso: {cls.nivel_acesso}, Usuários Online: {cls.usuarios_online}")

# Chamando os métodos
Usuario.adicionar_usuario()
Usuario.adicionar_usuario()
Usuario.mostrar_status()  # Nível de Acesso: Básico, Usuários Online: 2

Usuario.mudar_nivel_acesso("Admin")
Usuario.remover_usuario()
Usuario.mostrar_status()  # Nível de Acesso: Admin, Usuários Online: 1

# Exepmlo pratico
"""Exercício Prático
Crie uma classe ContaBancaria com os seguintes requisitos:

Atributos: titular, saldo
Métodos:
depositar(valor): Adiciona dinheiro ao saldo.
sacar(valor): Subtrai dinheiro do saldo (se houver saldo suficiente).
exibir_saldo(): Mostra o saldo atual."""

class ContaBancaria:
        
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Seu novo saldo é {self.saldo}")
    def sacar(self, valor):
        if  valor <= self.saldo:
            self.saldo -= valor
            print(f"Seu novo saldo é {self.saldo}")
        else:
            print("Saque não permitido")
    def exibir_saldo(self):
        print(f"Olá {self.titular}, seu saldo em conta é R$ {self.saldo}.")
        
#criando objetos
    
pessoa1 = ContaBancaria("Renan", 0)
pessoa2 = ContaBancaria("Sarah", 100)
pessoa3 = ContaBancaria("Adriana", 500)
    
#chamando metodo
    
pessoa1.depositar(300)
pessoa1.sacar(400)
pessoa1.depositar(200)
pessoa1.exibir_saldo()

pessoa2.depositar(100)
pessoa2.depositar(300)
pessoa2.depositar(200)
pessoa2.depositar(100)
pessoa2.sacar(400)
pessoa2.exibir_saldo()

pessoa3.exibir_saldo()

