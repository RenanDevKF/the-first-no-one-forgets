"""
O Problema da Herança: Por que evitar?
A herança pode parecer conveniente, mas pode levar a problemas de flexibilidade e manutenção do código. Aqui estão algumas razões para evitar herança sempre que possível:

1. Acoplamento Forte (Dependência Excessiva)
Quando uma classe herda outra, ela fica fortemente acoplada à classe base. Se a classe base mudar, todas as subclasses também serão afetadas.

2. Herança Múltipla Pode Ser Confusa
Em algumas linguagens (como Python), é possível herdar múltiplas classes, mas isso pode levar a conflitos difíceis de resolver.
Problema:
O Python segue a ordem do Method Resolution Order (MRO), mas pode ser difícil prever o comportamento quando há múltiplas classes.

3. Dificuldade de Reutilização
Se você precisar criar uma classe que compartilhe algumas, mas não todas as funcionalidades da classe base, a herança pode forçá-lo a herdar métodos desnecessários
class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def ligar_motor(self):
        return "Motor ligado"

class Bicicleta(Veiculo):
    pass  # Bicicletas não têm motor!

bike = Bicicleta("Caloi")
print(bike.ligar_motor())  # Mas bicicletas não têm motor!

A classe Bicicleta herdou um método que não faz sentido para ela, mostrando que a herança pode ser inadequada.

"""

"""
O Que é Composição?
Em vez de dizer que "um objeto É um outro objeto" (herança), usamos a composição para dizer que "um objeto TEM outro objeto". Isso reduz o acoplamento e melhora a flexibilidade.

- Composição significa que criamos objetos dentro de outros objetos, em vez de estendê-los diretamente.

class Motor:
    def ligar(self):
        return "Motor ligado"

class Carro:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor()  # O Carro TEM um Motor

    def ligar_carro(self):
        return self.motor.ligar()

carro = Carro("Toyota")
print(carro.ligar_carro())  # Saída: Motor ligado

Vantagem:

O Carro pode ter um Motor, mas também poderíamos mudar o motor facilmente.
Se quisermos criar um Carro elétrico, podemos apenas substituir o Motor


Comparação Direta entre Herança e Composição
Critério - 	Herança - 	Composição
Acoplamento	- Forte (subclasse depende da classe base) /	Fraco (os objetos apenas se comunicam)
Flexibilidade - 	Baixa (mudanças afetam muitas classes) /	Alta (pode trocar componentes facilmente)
Reutilização -	Ruim (herda métodos desnecessários)	/ Ótima (usa apenas o necessário)
Herança Múltipla- 	Confusa e propensa a erros	/ Simples e modular
"""

"""
Quando Usar Herança e Quando Usar Composição?
 Use Herança quando:

Existe uma clara relação de "É UM" (exemplo: "Cachorro é um Animal").
Você quer reutilizar código comum sem precisar duplicá-lo.
Você tem certeza de que as subclasses não precisarão mudar muito.
 Use Composição quando:

Existe uma relação de "TEM UM" (exemplo: "Carro tem um Motor").
Você quer evitar acoplamento forte e aumentar a flexibilidade.
Você deseja que os objetos possam ser trocados facilmente sem afetar o código.

Conclusão
Embora a herança seja útil, o abuso dela pode causar código difícil de manter e inflexível. Por isso, a composição é geralmente preferida, pois permite uma estrutura mais modular, reutilizável e fácil de modificar.

 Resumo:
 Evite herança quando possível.
 Prefira composição para maior flexibilidade.
 Se usar herança, faça com moderação e apenas quando for necessário.
"""

# Exemplo 1: Sistema de Funcionários e Departamentos

class Departamento:
    def __init__(self, nome):
        self.nome = nome

    def obter_departamento(self):
        return f"Departamento: {self.nome}"

class Funcionario:
    def __init__(self, nome, cargo, departamento):
        self.nome = nome
        self.cargo = cargo
        self.departamento = departamento  # Composição

    def exibir_informacoes(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}, {self.departamento.obter_departamento()}"

# Criando departamentos
dep_TI = Departamento("TI")
dep_RH = Departamento("Recursos Humanos")

# Criando funcionários e associando a um departamento
func1 = Funcionario("Carlos", "Desenvolvedor", dep_TI)
func2 = Funcionario("Ana", "Gerente", dep_RH)

print(func1.exibir_informacoes())  
# Saída: Funcionário: Carlos, Cargo: Desenvolvedor, Departamento: TI

print(func2.exibir_informacoes())  
# Saída: Funcionário: Ana, Cargo: Gerente, Departamento: Recursos Humanos


# Exemplo 3: Sistema de Pedidos em um Restaurante

class ItemMenu:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def detalhes(self):
        return f"{self.nome}: R$ {self.preco:.2f}"

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

    def exibir_pedido(self):
        detalhes_itens = "\n".join(item.detalhes() for item in self.itens)
        return f"Pedido:\n{detalhes_itens}\nTotal: R$ {self.calcular_total():.2f}"

# Criando itens do menu
hamburguer = ItemMenu("Hambúrguer", 15.90)
batata_frita = ItemMenu("Batata Frita", 8.50)
refrigerante = ItemMenu("Refrigerante", 5.00)

# Criando pedido e adicionando itens
pedido1 = Pedido()
pedido1.adicionar_item(hamburguer)
pedido1.adicionar_item(batata_frita)
pedido1.adicionar_item(refrigerante)

print(pedido1.exibir_pedido())
# Saída:
# Pedido:
# Hambúrguer: R$ 15.90
# Batata Frita: R$ 8.50
# Refrigerante: R$ 5.00
# Total: R$ 29.40

# Exemplo 4: Jogo - Personagens com Habilidades

class Habilidade:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def usar(self):
        return f"Usando {self.nome}, causando {self.dano} de dano!"

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.habilidades = []

    def adicionar_habilidade(self, habilidade):
        self.habilidades.append(habilidade)

    def atacar(self):
        return [habilidade.usar() for habilidade in self.habilidades]

# Criando habilidades
fogo = Habilidade("Bola de Fogo", 50)
gelo = Habilidade("Lança de Gelo", 40)

# Criando personagens e adicionando habilidades
guerreiro = Personagem("Guerreiro")
guerreiro.adicionar_habilidade(fogo)

mago = Personagem("Mago")
mago.adicionar_habilidade(fogo)
mago.adicionar_habilidade(gelo)

# Exibir ataques dos personagens
print("\n".join(guerreiro.atacar()))
print("\n".join(mago.atacar()))
