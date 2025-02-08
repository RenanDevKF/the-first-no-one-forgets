"""
    Exercício 1 – Criando Subclasses
Crie uma classe Veiculo com os atributos marca e modelo.
Depois, crie as subclasses Carro e Moto, sobrescrevendo o método descrever() de maneira única para cada tipo de veículo.
No final, crie uma lista com diferentes veículos e exiba suas descrições usando um laço for.

✅ Conceitos praticados: Herança, sobrescrita de métodos, polimorfismo.

"""

class Veiculo:
    
    def __init__ (self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descrever(self):
        print(f"Veiculo: {self.marca} {self.modelo}")
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
    def descrever(self):
        super().descrever()
        print(f"Tem {self.portas} portas.")

class Moto(Veiculo):        
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    def descrever(self):
        super().descrever()
        print(f"Tem {self.cilindrada} cilindradas.")
        
# criando objetos
carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Honda", "CG", 150)
carro2 = Carro("Ford", "Mustang", 2)
moto2 = Moto("Yamaha", "Fazer", 250)

# exibindo informacoes

for veiculo in [carro1, moto1, carro2, moto2]:
    veiculo.descrever()

