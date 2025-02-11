"""Criando uma Lista Genérica
Crie uma classe ListaGenerica que pode armazenar uma lista de qualquer tipo de dado. Implemente os seguintes métodos:

adicionar(item: T): Adiciona um item à lista.
remover() -> T: Remove e retorna o último item da lista.
mostrar_lista(): Exibe todos os itens da lista.
💡 Teste armazenando números, strings e objetos personalizados.
"""

from typing import Generic, TypeVar

T = TypeVar ('T')   # Criando um tipo genérico

class ListaGenerica(Generic[T]):
    
    def __init__(self):
        self.item = []
    
    def adicionar(self, item: T):
        self.item.append(item)
    
    def remover(self):
        if self.item:
            return self.item.pop()
        else:
            return None
        
    def remover_especifico(self, item: T):
        if item in self.item:
            self.item.remove(item)
            return f"Item removido -> {item}"
        else:
            return f"Item nao encontrado -> {item}"
    
    def mostrar_lista(self) -> T:
        return self.item.copy() # Retorna uma cópia da lista para evitar alterações externas
    
lista = ListaGenerica() # Criando uma instância da classe
    
lista.adicionar(10)
lista.adicionar("Renan")
lista.adicionar([1, 2, 3])
print(lista.mostrar_lista())

print(lista.remover())
print(lista.mostrar_lista())
print(lista.remover_especifico("Renan"))
print(lista.mostrar_lista())