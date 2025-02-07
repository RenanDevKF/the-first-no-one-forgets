""""
O que é Herança?
A herança é um conceito da Programação Orientada a Objetos (POO) que permite criar uma nova classe baseada em uma classe existente.

✔️ A nova classe herda os atributos e métodos da classe original.
✔️ Podemos adicionar novos atributos e métodos ou sobrescrever os métodos existentes.

Isso evita repetição de código e torna o programa mais organizado.

"""

# Classe Base (Superclasse)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Classe Derivada (Subclasse)
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)  # Chamando o construtor da classe Pai
        self.cargo = cargo
        self.salario = salario

    def apresentar_funcionario(self):
        print(f"{self.nome} trabalha como {self.cargo} e ganha R$ {self.salario:.2f}")

# Criando um objeto da subclasse
funcionario1 = Funcionario("Carlos", 30, "Engenheiro", 5000.00)

# Usando métodos da classe base e da classe derivada
funcionario1.apresentar()  # Método herdado de Pessoa
funcionario1.apresentar_funcionario()  # Método da subclasse

"""
✔️ A classe Funcionario herda os atributos e métodos da classe Pessoa.
✔️ O super().__init__(nome, idade) chama o construtor da classe Pai (Pessoa), evitando repetição de código.
✔️ A classe Funcionario adiciona novos atributos e métodos (cargo, salario, apresentar_funcionario).

Benefícios da Herança
🔹 Reutilização de código → Evita repetição e facilita a manutenção.
🔹 Organização → Torna o código mais estruturado e fácil de entender.
🔹 Facilidade na expansão → Podemos criar novas classes sem modificar a base.

    Podemos sobrescrever métodos da classe Pai?
Sim! Se quisermos que um método tenha um comportamento diferente na subclasse, podemos sobrescrevê-lo.
ex:
"""
# O método apresentar() foi reescrito na subclasse, então ele tem um comportamento diferente do método da classe Pessoa.
class Funcionario(Pessoa):
    def apresentar(self):  # Sobrescrevendo o método apresentar()
        print(f"Sou {self.nome}, tenho {self.idade} anos e sou funcionário.")

funcionario2 = Funcionario("Ana", 28, "Designer", 4500.00)
funcionario2.apresentar()  # Saída: Sou Ana, tenho 28 anos e sou funcionário.

"""
Conclusão
✔️ Herança permite que uma classe (subclasse) herde atributos e métodos de outra (superclasse).
✔️ Podemos adicionar novos métodos e atributos na subclasse.
✔️ Podemos sobrescrever métodos da classe base para alterar seu comportamento.
✔️ O super() chama métodos da classe Pai, evitando repetição de código.
"""

# 1️⃣ Exemplo com Várias Subclasses

# Classe Base (Superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        print("O animal faz um som.")

# Subclasse Cachorro
class Cachorro(Animal):
    def fazer_som(self):  # Sobrescrevendo o método
        print(f"{self.nome} diz: Au Au!")

# Subclasse Gato
class Gato(Animal):
    def fazer_som(self):  # Sobrescrevendo o método
        print(f"{self.nome} diz: Miau!")

# Criando objetos
cachorro = Cachorro("Rex")
gato = Gato("Mimi")

# Chamando métodos
cachorro.fazer_som()  # Saída: Rex diz: Au Au!
gato.fazer_som()      # Saída: Mimi diz: Miau!

"""
✔️ Criamos a superclasse Animal com um método genérico fazer_som().
✔️ As subclasses Cachorro e Gato sobrescrevem esse método com comportamentos específicos.
✔️ Isso permite criar diferentes tipos de animais sem modificar a classe base.
"""

# 2️⃣ Exemplo com super() e métodos adicionais
# Podemos chamar o método da classe Pai (super()) e ainda adicionar novos comportamentos na subclasse.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        print(f"Veículo: {self.marca} {self.modelo}")

# Subclasse Carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)  # Chamando o construtor da classe Pai
        self.portas = portas

    def descrever(self):  # Sobrescrevendo o método
        super().descrever()  # Chamando a versão da classe Pai
        print(f"Tem {self.portas} portas.")

# Criando um objeto da subclasse
meu_carro = Carro("Toyota", "Corolla", 4)
meu_carro.descrever()

"""
✔️ super().__init__(marca, modelo) chama o construtor da classe base.
✔️ O método descrever() da subclasse chama o da classe Pai e adiciona novas informações.
✔️ Resultado esperado:

Veículo: Toyota Corolla
Tem 4 portas.

"""

# Exemplo de Herança Múltipla
# Em Python, uma classe pode herdar de múltiplas classes ao mesmo tempo.

class Mamifero:
    def __init__(self):
        print("Mamífero criado.")

    def amamentar(self):
        print("Este animal amamenta seus filhotes.")

class Ave:
    def __init__(self):
        print("Ave criada.")

    def voar(self):
        print("Este animal pode voar.")

# Subclasse que herda de Mamifero e Ave
class Morcego(Mamifero, Ave):
    def __init__(self):
        super().__init__()  # Chama o construtor da primeira classe herdada
        print("Morcego criado.")

# Criando um objeto da subclasse
morcego = Morcego()
morcego.amamentar()  # Método da classe Mamifero
morcego.voar()       # Método da classe Ave

"""
✔️ Morcego herda de Mamifero e Ave.
✔️ Ele pode usar métodos de ambas as classes (amamentar() e voar()).
✔️ A chamada de super().__init__() executa apenas o construtor da primeira classe listada (Mamifero).
✔️ Se precisar chamar todos os construtores, devemos chamar explicitamente Ave.__init__(self).
ex:
# Subclasse que herda de Mamifero e Ave
class Morcego(Mamifero, Ave):
    def __init__(self):
        Mamifero.__init__(self)  # Chamando explicitamente o construtor de Mamifero
        Ave.__init__(self)       # Chamando explicitamente o construtor de Ave
        print("Morcego criado.")
"""

# Criando Métodos Genéricos na Superclasse
# Podemos criar métodos genéricos na classe Pai e especializá-los nas subclasses.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return 0  # Método genérico

# Subclasse Gerente
class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10  # 10% de bônus

# Subclasse Desenvolvedor
class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20  # 20% de bônus

# Criando funcionários
gerente = Gerente("Alice", 5000)
dev = Desenvolvedor("Bob", 6000)

print(f"Bônus do Gerente: R$ {gerente.calcular_bonus():.2f}")
print(f"Bônus do Desenvolvedor: R$ {dev.calcular_bonus():.2f}")

"""
✔️ Funcionario define um método genérico calcular_bonus() que retorna 0.
✔️ Gerente e Desenvolvedor sobrescrevem esse método com cálculos específicos.
✔️ Resultado esperado:

ruby
Copiar
Editar
Bônus do Gerente: R$ 500.00
Bônus do Desenvolvedor: R$ 1200.00

Conclusão
✔️ Herança permite criar classes novas baseadas em classes existentes.
✔️ Subclasses podem sobrescrever métodos da superclasse.
✔️ O super() chama métodos da classe base, evitando duplicação de código.
✔️ Herança múltipla é possível, mas deve ser usada com cuidado.

"""

# O que é Polimorfismo?
# O Polimorfismo permite que métodos com o mesmo nome tenham comportamentos diferentes dependendo da classe que os implementa.
# Herança + Polimorfismo na Prática

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibir_saldo(self):
        print(f"{self.titular}, seu saldo é R$ {self.saldo:.2f}")

class ContaPoupanca(ContaBancaria):
    def exibir_saldo(self):
        print(f"[Conta Poupança] {self.titular}, saldo disponível: R$ {self.saldo:.2f}")

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def exibir_saldo(self):
        print(f"[Conta Corrente] {self.titular}, saldo disponível: R$ {self.saldo:.2f} com limite de R$ {self.limite:.2f}")

# Criando diferentes contas
conta1 = ContaPoupanca("Carlos", 1500)
conta2 = ContaCorrente("Mariana", 2000, 500)

# Chamando o método polimórfico
contas = [conta1, conta2]

for conta in contas:
    conta.exibir_saldo()

"""
Saída esperada:

[Conta Poupança] Carlos, saldo disponível: R$ 1500.00
[Conta Corrente] Mariana, saldo disponível: R$ 2000.00 com limite de R$ 500.00
🔹 O mesmo método (exibir_saldo()) se comporta de maneira diferente nas subclasses.
🔹 Isso é um exemplo prático de Polimorfismo!

"""
