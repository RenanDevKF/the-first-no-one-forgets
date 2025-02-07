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
