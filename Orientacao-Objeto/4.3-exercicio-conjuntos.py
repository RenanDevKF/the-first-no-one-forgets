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
lista_alunos = ["Ana", "Carlos", "Maria", "Pedro", "João", "Bianca", "Lucas", "Juliana", "Felipe", "Laura"]

def marcar_presenca(nome):
    presentes.add(nome)
    print(f"{nome} marcou presença.")

def listar_presentes():
    print("\n📌 Alunos Presentes:")
    for aluno in sorted(presentes):
        print(aluno)
        
def confirmar_presenca(nome):
    qtd_presentes = 0
    qtd_ausentes = 0
    for nome in lista_alunos:
        if nome in presentes:
            qtd_presentes += 1
            print(f"{nome} esta presente.")
            
      
    ausentes = set(lista_alunos) - presentes
    qtd_ausentes = len(ausentes)
    print(f"Quantidade de alunos presentes: {qtd_presentes}")
    print(f"Quantidade de alunos ausentes: {qtd_ausentes}")
    print(f"Alunos presentes: {sorted(presentes)}")
    print(f"Alunos ausentes: {sorted(ausentes)}")

# Teste do sistema
marcar_presenca("Lucas")
marcar_presenca("Maria")
marcar_presenca("João")
marcar_presenca("Lucas")  # Não será adicionado novamente

listar_presentes()

confirmar_presenca()
