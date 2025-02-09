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
        print("Tarefa nao encontrada!")
        
def listar_tarefas():
    print("\n Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
        
        # Teste do sistema
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer exercícios de POO")
adicionar_tarefa("Revisar encapsulamento")

listar_tarefas()

remover_tarefa("Estudar Python")
listar_tarefas()