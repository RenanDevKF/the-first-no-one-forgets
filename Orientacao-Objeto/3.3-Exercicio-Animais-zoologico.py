"""
Exercício 3 – Animais no Zoológico (Desafio!)
Crie uma classe Animal com o método emitir_som(), mas sem implementá-lo (apenas pass).
Depois, crie três subclasses: Leão, Papagaio e Cobra, cada uma sobrescrevendo emitir_som() com sons específicos.

No final, crie uma lista de animais e faça com que todos emitam seus sons.

✅ Conceitos praticados: Herança, polimorfismo, classes abstratas (se quiser ir além).

    """
    
from abc import ABC, abstractmethod

# Definição da classe abstrata
class Animal(ABC):  
    @abstractmethod
    def emitir_som(self):
        """Método abstrato que deve ser implementado pelas subclasses"""
        pass  

# Subclasse Leão
class Leao(Animal):
    def emitir_som(self):
        print("Rugir")

# Subclasse Papagaio
class Papagaio(Animal):
    def emitir_som(self):
        print("Piu Piu")

# Subclasse Cobra
class Cobra(Animal):
    def emitir_som(self):
        print("Hiss")

# Criando uma lista de animais
animais = [Leao(), Papagaio(), Cobra()]

# Fazendo os animais emitirem seus sons
for animal in animais:
    animal.emitir_som()
