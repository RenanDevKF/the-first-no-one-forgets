"""Criando uma Fila Genérica
Implemente uma classe FilaGenerica<T> que representa uma fila (FIFO - First In, First Out). Deve conter os métodos:

enfileirar(item: T): Adiciona um item ao final da fila.
desenfileirar() -> T: Remove e retorna o primeiro item da fila.
tamanho() -> int: Retorna o número de itens na fila.
💡 Teste com diferentes tipos de dados.
"""

from typing import Generic, TypeVar

T = TypeVar('T')  # Criando um tipo genérico

class FilaGenerica(Generic[T]):

    def __init__(self):
        self.item = []
    
    def enfileirar(self, item: T):
        self.item.append(item)

    def desenfileirar(self):
        if self.item:
            return self.item.pop(0)
        else:
            return "Lista Vazia, não tme o que retirar"
    
    def tamanho(self):
        return len(self.item)

# testando

fila = FilaGenerica[int]()

fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)

print(fila.desenfileirar())  # 10
print(fila.desenfileirar())  # 20
print(fila.desenfileirar())  # 30
print(fila.desenfileirar())

print(fila.tamanho())

# teste 2

fila = FilaGenerica[str]()

fila.enfileirar('a')
fila.enfileirar('b')
fila.enfileirar('c')

print(fila.desenfileirar())  # a
print(fila.desenfileirar())  # b

print(fila.tamanho())

# teste 3

fila = FilaGenerica[str]()

fila.enfileirar('Renan')
fila.enfileirar('Sarah')
fila.enfileirar('Adriana')

print(fila.desenfileirar())  # Renan
print(fila.desenfileirar())  # Sarah

print(fila.tamanho())