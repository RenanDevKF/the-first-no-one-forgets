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






