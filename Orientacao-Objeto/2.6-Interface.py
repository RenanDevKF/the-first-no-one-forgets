"""
    O que é uma Interface em POO?
Uma interface define um conjunto de métodos que uma classe deve implementar, sem fornecer a implementação desses métodos.

✔️ Ela age como um contrato: qualquer classe que "assina" esse contrato precisa obrigatoriamente implementar os métodos definidos.
✔️ Diferente da herança tradicional, uma classe pode implementar múltiplas interfaces, garantindo flexibilidade.
✔️ Interfaces são amplamente utilizadas para garantir padronização e desacoplamento entre classes.
    
"""

#  Interfaces em Python
#  Python não tem uma palavra-chave interface, como Java ou C#, mas podemos usar classes abstratas com o módulo abc (Abstract Base Class).

from abc import ABC, abstractmethod

# Criamos a Interface
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

# Aqui, Forma define uma interface onde qualquer classe que herdar dela precisa implementar calcular_area().
# Agora, se criarmos uma classe concreta (normal), ela precisa implementar esse método:

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2  # Implementação obrigatória

# Criando um objeto
q = Quadrado(4)
print(q.calcular_area())  # Saída: 16

"""
Diferença Entre Interface e Herança:
Herança - Quando uma classe herda comportamento e dados de outra classe.
Interface - Apenas obriga a implementação de métodos, sem herdar atributos.

Benefícios de Usar Interfaces
Força um padrão - Garante que todas as classes sigam a mesma estrutura.
Facilita a manutenção - Como os métodos são bem definidos, as alterações são mais organizadas.
Flexibilidade - Uma classe pode implementar várias interfaces ao mesmo tempo.

"""

# Exercicio pratico:
"""
Exercício Prático
Crie uma interface chamada "Controlador" com os métodos:

ligar()
desligar()
reiniciar()
Depois, crie duas classes que implementem essa interface:
✔ Computador (deve implementar os métodos com comportamentos específicos).
✔ Televisão (deve implementar os métodos de forma diferente do computador).
"""

from abc import ABC, abstractmethod

class Controlador(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod 
    def desligar(self):
        pass

    @abstractmethod
    def reiniciar(self):
        pass
    
class Computador(Controlador):
    def ligar(self):
        print("Computador ligado, o que vamos estudar?")

    def desligar(self):
        print("Computador desligado, até logo!")

    def reiniciar(self):
        print("Computador reiniciado")

class Televisao(Controlador):
    def ligar(self):
        print("Televisão ligada, o que vamos assistir?")

    def desligar(self):
        print("Televisão desligada, descanse as vistas!")
    
    def reiniciar(self):
        print("Televisão não pode ser reiniciada")
        
# chmando os metodos
computador = Computador()
computador.ligar()
computador.desligar()
computador.reiniciar()

televisao = Televisao()
televisao.ligar()
televisao.desligar()
televisao.reiniciar()