# 2. Exercício com Dicionários
# Objetivo: Criar um sistema de cadastro de alunos e notas usando dicionários.

# Dicionário para armazenar alunos e notas

alunos = {}

def adicionar_aluno(nome,nota):
    alunos[nome] = nota
    print(f"Aluno {nome} cadastrado com nota {nota}.")

def mostrar_notas():
    print("\n Notas dos Alunos:")
    for nome,nota in alunos.items():
        print(f"{nome}: {nota}")
        
def calcular_media():
    if alunos:
        media = sum(alunos.values()) / len(alunos)
        print(f"\n Média da turma: {media:.2f}")
    else:
        print("\n Nenhum aluno cadastrado.")

def corrigir_nota(nome,nota_nova):
    if nome in alunos:
        alunos[nome] = nota_nova
        print(f"Nota de {nome} corrigida para {nota_nova}.")
    else:
        print(f"Aluno {nome} nao encontrado.")
        
# Teste do sistema
adicionar_aluno("Ana", 8.5)
adicionar_aluno("Carlos", 7.0)
adicionar_aluno("Bianca", 9.2)

mostrar_notas()
calcular_media()
corrigir_nota("Ana", 9.0)
calcular_media()