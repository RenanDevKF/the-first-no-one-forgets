"""Criando um Dicionário Genérico
Crie uma classe DicionarioGenerico<K, V> que funciona como um dicionário genérico. Ela deve ter:

adicionar(chave: K, valor: V): Adiciona um par chave-valor ao dicionário.
remover(chave: K) -> V: Remove e retorna o valor associado à chave.
obter(chave: K) -> V: Retorna o valor associado à chave.
mostrar_dicionario(): Exibe todos os pares chave-valor.
💡 Teste armazenando diferentes combinações de tipos.
"""

from typing import Generic, TypeVar

K = TypeVar('K')  # Criando um tipo genérico para a chave
V = TypeVar('V')  # Criando um tipo genérico para o valor

class DicionarioGenerico(Generic[K, V]):
    def __init__(self):
        self.dicionario = {}

    def adicionar(self, chave: K, valor: V):
        self.dicionario[chave] = valor

    def remover(self, chave: K) -> V:
        return self.dicionario.pop(chave)

    def obter(self, chave: K) -> V:
        return self.dicionario[chave]

    def mostrar_dicionario(self):
        print(self.dicionario)
        

# teste 1

dicionario = DicionarioGenerico[int, str]() # ou dicionario = DicionarioGenerico()

dicionario.adicionar(1, 'a')
dicionario.adicionar(2, 'b')
dicionario.adicionar(3, 'c')

print(dicionario.mostrar_dicionario())  # {1: 'a', 2: 'b', 3: 'c'}

# teste 2

dicionario = DicionarioGenerico[str, int]() # ou dicionario = DicionarioGenerico()

dicionario.adicionar('a', 1)
dicionario.adicionar('b', 2)
dicionario.adicionar('c', 3)

print(dicionario.mostrar_dicionario())  # {'a': 1, 'b': 2, 'c': 3}

# teste 3

dicionario = DicionarioGenerico[str, float]() # ou dicionario = DicionarioGenerico()

dicionario.adicionar('a', 1.1)
dicionario.adicionar('b', 2.2)
dicionario.adicionar('c', 3.3)

print(dicionario.mostrar_dicionario())  # {'a': 1.1, 'b': 2.2, 'c': 3.3}

# teste 4

dicionario = DicionarioGenerico[float, int]() # ou dicionario = DicionarioGenerico()

dicionario.adicionar(1.1, 1)
dicionario.adicionar(2.2, 2)
dicionario.adicionar(3.3, 3)

print(dicionario.mostrar_dicionario())  # {1.1: 1, 2.2: 2, 3.3: 3}

# teste 5 - remover

dicionario = DicionarioGenerico[int, str]() # ou dicionario = DicionarioGenerico()

dicionario.adicionar(1, 'a')
dicionario.adicionar(2, 'b')
dicionario.adicionar(3, 'c')    

print(dicionario.mostrar_dicionario())  # {1: 'a', 2: 'b', 3: 'c'}

print(dicionario.remover(2))  # b
print(dicionario.mostrar_dicionario())  # {1: 'a', 3: 'c'}

# teste 6 - obter

dicionario = DicionarioGenerico[int, str]() # ou dicionario = DicionarioGenerico()

dicionario.adicionar(1, 'a')
dicionario.adicionar(2, 'b')
dicionario.adicionar(3, 'c')

print(dicionario.obter(2))  # b
