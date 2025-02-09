# Estudo Prático: Trabalhando com Coleções

# 1. Exercício com Listas
#  Objetivo: Criar um sistema de gerenciamento de tarefas usando listas.

# Lista para armazenar tarefas
tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!")

def remover_tarefa(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' removida!")
    else:
        print("Tarefa não encontrada!")

def listar_tarefas():
    print("\n📌 Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

# Teste do sistema
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer exercícios de POO")
adicionar_tarefa("Revisar encapsulamento")

listar_tarefas()

remover_tarefa("Estudar Python")
listar_tarefas()

"""
Pratique:

Adicione mais tarefas.
Tente remover uma tarefa inexistente.
Melhore o código, adicionando uma opção para editar tarefas.
"""

# 2. Exercício com Dicionários
# Objetivo: Criar um sistema de cadastro de alunos e notas usando dicionários.

# Dicionário para armazenar alunos e notas
alunos = {}

def adicionar_aluno(nome, nota):
    alunos[nome] = nota
    print(f"Aluno {nome} cadastrado com nota {nota}.")

def mostrar_notas():
    print("\n📌 Notas dos Alunos:")
    for nome, nota in alunos.items():
        print(f"{nome}: {nota}")

def calcular_media():
    if alunos:
        media = sum(alunos.values()) / len(alunos)
        print(f"\n📊 Média da turma: {media:.2f}")
    else:
        print("\n⚠️ Nenhum aluno cadastrado.")

# Teste do sistema
adicionar_aluno("Ana", 8.5)
adicionar_aluno("Carlos", 7.0)
adicionar_aluno("Bianca", 9.2)

mostrar_notas()
calcular_media()

"""
    Pratique:

Adicione mais alunos.
Crie uma função para buscar um aluno pelo nome.
Implemente uma opção para atualizar a nota de um aluno.
"""

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

#4. Exercício com Counter (Contagem de elementos)
# Objetivo: Contar quantas vezes cada palavra aparece em uma lista usando Counter

from collections import Counter

palavras = ["Python", "Java", "Python", "C++", "Java", "Python", "C#"]
contagem = Counter(palavras)

print("\n📊 Frequência das palavras:")
for palavra, qtd in contagem.items():
    print(f"{palavra}: {qtd}")

""" 
Pratique:

Teste com uma lista maior.
Modifique o código para contar letras em uma frase.

"""

""" 
Desafio Final
Agora, crie um sistema bancário com listas e dicionários para armazenar:

Contas bancárias (usando dicionários).
Depósitos e saques (atualizando os valores).
Um menu interativo para o usuário.
"""