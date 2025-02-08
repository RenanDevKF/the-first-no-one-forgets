"""
Exercício 2 – Funcionários da Empresa
Crie uma classe Funcionario com os atributos nome e salario.
Depois, crie duas subclasses:
✔️ Gerente (com um bônus de 10% sobre o salário)
✔️ Programador (com um bônus de 5%)

Implemente o método calcular_salario() para retornar o salário com bônus incluído.
Crie uma lista com funcionários diferentes e exiba seus salários corrigidos.

✅ Conceitos praticados: Herança, polimorfismo, chamadas ao super()

"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return 0  # Definido pelas subclasses

    def calcular_salario(self):
        return self.salario + self.calcular_bonus()

    def descrever_salario(self):
        print(f"{self.__class__.__name__} {self.nome} recebe R$ {self.calcular_salario():.2f} por mês.")

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10  # Bônus de 10%

class Programador(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05  # Bônus de 5%

# Criando funcionários
gerente1 = Gerente("Alice", 5000)
dev1 = Programador("Bob", 6000)
gerente2 = Gerente("Carol", 7000)
dev2 = Programador("David", 8000)
gerente3 = Gerente("Eva", 9000)
dev3 = Programador("Fernando", 10000)

# Lista de funcionários
funcionarios = [gerente1, dev1, gerente2, dev2, gerente3, dev3]

# Exibindo os salários corrigidos
for funcionario in funcionarios:
    funcionario.descrever_salario()
