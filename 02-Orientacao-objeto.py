# Inicio dos estudos Orientação ao Objeto
# Casse: Um modelo ou molde para criar objetos. Define atributos (dados) e metodos (comportamentos)
# Objetos: Instancias da classe. Criados a partir do molde da classe
# Metodos: Funcoes que estao dentro da classe que realizam tarefas
# Atributos: Variaveis que estao dentro da classe que representam os dados do objeto

# Exemplo usando carros:

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca #atributos
        self.modelo = modelo
        self.cor = cor
    
    def exibir_info(self): # metodo
        print(f"Carro: {self.marca}, {self.modelo}, {self.cor}")
        
    # Criando um objeto a partir da classe Carro
carro1 = Carro("Fiat", "Palio", "Preto")
carro2 = Carro("Honda", "Civic", "Branco")

    # Chamando o metodo do objeto (exibir_info)
carro1.exibir_info()
carro2.exibir_info()

# Exemplo pratico

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
    def exibir_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}m")
        
# Criando objetos a partir da classe Pessoas
pessoa1 = Pessoa("João", 30, 1.75)
pessoa2 = Pessoa("Maria", 25, 1.60)