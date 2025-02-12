"""Criando uma Fila Genérica
Implemente uma classe FilaGenerica<T> que representa uma fila (FIFO - First In, First Out). Deve conter os métodos:

enfileirar(item: T): Adiciona um item ao final da fila.
desenfileirar() -> T: Remove e retorna o primeiro item da fila.
tamanho() -> int: Retorna o número de itens na fila.
💡 Teste com diferentes tipos de dados.
"""

from typing import Generic, TypeVar

T = TypeVar('T')  # Criando um tipo genérico

def __init__(self):
    self.item = []
    
def enfileirar(self, item: T):
    self.item.append(item)

def desenfileirar(self):
    if self.item:
        return self.item.pop(0)
    else:
        return None
    
def tamanho(self):
    return len(self.item)