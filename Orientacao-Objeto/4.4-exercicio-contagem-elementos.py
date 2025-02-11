#4. Exercício com Counter (Contagem de elementos)

""" 
Pratique:

Teste com uma lista maior.
Modifique o código para contar letras em uma frase.

"""
# Objetivo: Contar quantas vezes cada palavra aparece em uma lista usando Counter

from collections import Counter

palavras = ["Python", "Java", "Python", "C++", "Java", "Python", "C#"]


def contagem_elementos(palavras):
    contagem = Counter(palavras)
    print("\n📊 Frequência das palavras:")
    for palavra, qtd in contagem.items():
        print(f"{palavra}: {qtd}")

def contagem_letras(letras):
    lista_completa = "".join(sorted(letras)) # junta as letras em uma string de forma ordenada
    lista_completa = lista_completa.lower()
    contagem = Counter(lista_completa) # conta quantas vezes cada letra aparece
    print("\n📊 Frequência das letras:")
    for letra, qtd in sorted(contagem.items()): # ordena as letras
        print(f"{letra}: {qtd}")
        


#chamando funcao
contagem_elementos(palavras)
contagem_letras(palavras)