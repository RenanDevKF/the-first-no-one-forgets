# 3. Exercício com Conjuntos
# Objetivo: Criar um sistema de controle de presença usando sets.

# Conjunto para armazenar alunos presentes
presentes = set()

def marcar_presenca(nome):
    presentes.add(nome)
    print(f"{nome} marcou presença.")

def listar_presentes():
    print("\n📌 Alunos Presentes:")
    for aluno in presentes:
        print(aluno)

# Teste do sistema
marcar_presenca("Lucas")
marcar_presenca("Maria")
marcar_presenca("João")
marcar_presenca("Lucas")  # Não será adicionado novamente

listar_presentes()

"""
    Pratique:

Adicione mais alunos.
Crie uma função para verificar se um aluno está presente.
Implemente um sistema para registrar faltas.
"""