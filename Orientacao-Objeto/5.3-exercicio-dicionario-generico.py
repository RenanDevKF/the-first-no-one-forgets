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
        


