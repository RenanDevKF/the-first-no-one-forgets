# Continuacao Aula 02
# Atributos e Metodos

# Teoria sobre Atributos

"""
Tipos de Atributos:
- Atributos de Instância (mais comuns)
-- São específicos de cada objeto.
--Definidos dentro do método __init__().

-Atributos de Classe
--Compartilhados entre todas as instâncias de uma classe.
--Definidos diretamente dentro da classe (fora de __init__()).

Vide exeplo do arquivo 02-Denifinica-classe
"""
# Exemplo de Atributos de Classe

class Pessoa:
    especie = "Humano"  # Atributo de classe (compartilhado)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando objetos
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

print(pessoa1.especie)  # Saída: Humano
print(pessoa2.especie)  # Saída: Humano

# Alterando o atributo de classe
Pessoa.especie = "Ser Vivo"

print(pessoa1.especie)  # Saída: Ser Vivo
print(pessoa2.especie)  # Saída: Ser Vivo

# Teoria sobre Metodos

"""
Os métodos são funções dentro da classe que definem comportamentos dos objetos. Eles são chamados a partir de um objeto e podem acessar/modificar atributos.

Tipos de Métodos
1. Métodos de Instância

- Definidos com self.
- Podem acessar e modificar atributos do objeto.

2. Métodos de Classe

- Definidos com @classmethod e cls.
- Podem modificar atributos de classe.

3. Métodos Estáticos

- Definidos com @staticmethod.
- Não acessam atributos de instância ou de classe diretamente.
"""





