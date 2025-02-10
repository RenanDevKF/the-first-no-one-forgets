# 3. Exercício com Conjuntos
# Objetivo: Criar um sistema de controle de presença usando sets.
"""
    Pratique:

Adicione mais alunos.
Crie uma função para verificar se um aluno está presente.
Implemente um sistema para registrar faltas.
"""
# Conjunto para armazenar alunos presentes
presentes = set()

def marcar_presenca(nome):
    presentes.add(nome)
    print(f"{nome} marcou presença.")

def listar_presentes():
    print("\n📌 Alunos Presentes:")
    for aluno in presentes:
        print(aluno)
        
def confirmar_presenca(nome):
    qtd_presentes = 0
    qtd_ausentes = 0
    if nome in presentes:
        qtd_presentes += 1
        print(f"{nome} esta presente.")
        print(f"Quantidade de alunos presentes: {qtd_presentes}")
    else:
        print(f"{nome} nao esta presente.")
        print(f"Quantidade de alunos ausentes: {qtd_ausentes}")

# Teste do sistema
marcar_presenca("Lucas")
marcar_presenca("Maria")
marcar_presenca("João")
marcar_presenca("Lucas")  # Não será adicionado novamente

listar_presentes()

