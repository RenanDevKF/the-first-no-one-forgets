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
        


#chamando funcao
contagem_elementos(palavras)