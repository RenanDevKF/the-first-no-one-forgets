"""
1. O que são Classes e Métodos Genéricos?
- Classes genéricas são aquelas que podem operar com diferentes tipos de dados sem precisar definir explicitamente o tipo no momento da criação.
- Métodos genéricos são funções dentro de uma classe que podem aceitar diferentes tipos de entrada e ainda assim funcionar corretamente.

Em Python, conseguimos implementar isso utilizando tipagem dinâmica e tipos genéricos com typing.Generic.

"""
# 2. Exemplo Básico: Classe Genérica com Tipagem Dinâmica
# Como Python não exige declarar tipos, essa classe já é genérica por natureza.

class Caixa:
    def __init__(self, item):
        self.item = item

    def mostrar_item(self):
        print(f"Item armazenado: {self.item}")

# Testando com diferentes tipos
caixa1 = Caixa(10)        # Armazena um número
caixa2 = Caixa("Python")  # Armazena uma string
caixa3 = Caixa([1, 2, 3]) # Armazena uma lista

caixa1.mostrar_item()  # Item armazenado: 10
caixa2.mostrar_item()  # Item armazenado: Python
caixa3.mostrar_item()  # Item armazenado: [1, 2, 3]

# Usando typing.Generic para Especificar Tipos Genéricos
# Se quisermos ser mais explícitos sobre os tipos, podemos usar typing.Generic e TypeVar para definir classes realmente genéricas:

from typing import Generic, TypeVar

T = TypeVar('T')  # Criando um tipo genérico

class Caixa(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def mostrar_item(self) -> T:
        return self.item

# Testando com diferentes tipos
caixa_numero = Caixa(42)            # Armazena um número inteiro
caixa_texto = Caixa("Hello World")  # Armazena uma string

print(caixa_numero.mostrar_item())  # Saída: 42
print(caixa_texto.mostrar_item())   # Saída: Hello World


#4. Métodos Genéricos em Python
#Podemos ter métodos dentro da classe que também sejam genéricos e trabalhem com diferentes tipos.
#Exemplo: Criando um método que aceita qualquer tipo de dado
# Aqui o método inverter_lista pode trabalhar tanto com números quanto com strings.

from typing import List

class Processador:
    @staticmethod
    def inverter_lista(lista: List[T]) -> List[T]:
        return lista[::-1]

# Testando com listas de diferentes tipos
print(Processador.inverter_lista([1, 2, 3, 4]))       # [4, 3, 2, 1]
print(Processador.inverter_lista(["a", "b", "c"]))    # ['c', 'b', 'a']

# . Aplicação de Métodos Genéricos em Estruturas de Dados
#Podemos usar classes genéricas para criar estruturas de dados reutilizáveis.
#Exemplo: Criando uma Pilha Genérica

from typing import List, TypeVar, Generic

T = TypeVar('T')  # Criando um tipo genérico

class Pilha(Generic[T]):
    def __init__(self):
        self.itens: List[T] = []  # Lista genérica

    def empilhar(self, item: T):
        self.itens.append(item)

    def desempilhar(self) -> T:
        return self.itens.pop() if self.itens else None

    def topo(self) -> T:
        return self.itens[-1] if self.itens else None

# Testando com números
pilha_int = Pilha[int]()
pilha_int.empilhar(10)
pilha_int.empilhar(20)
print(pilha_int.desempilhar())  # 20

# Testando com strings
pilha_str = Pilha[str]()
pilha_str.empilhar("A")
pilha_str.empilhar("B")
print(pilha_str.topo())  # "B"

"""
Conclusão
✅ Classes e métodos genéricos em Python tornam o código mais reutilizável, escalável e seguro.
✅ O Python já é dinâmico, mas Generic[T] ajuda a manter tipagem mais clara.
✅ Aplicação comum: Estruturas de dados como pilhas, filas e coleções.

💡 Se estiver aprendendo POO, experimente usar tipos genéricos para melhorar seus projetos! 

"""