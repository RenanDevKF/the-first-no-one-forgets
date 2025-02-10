# 1. Exercício com Listas
#  Objetivo: Criar um sistema de gerenciamento de tarefas usando listas.

"""
Pratique:

Adicione mais tarefas.
Tente remover uma tarefa inexistente.
Melhore o código, adicionando uma opção para editar tarefas.
"""

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
        print(f"Tarefa '{tarefa}' nao encontrada!")
        
def listar_tarefas():
    print("\n Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
        
def editar_tarefa(tarefa, nova_tarefa):
    if tarefa in tarefas:
        index = tarefas.index(tarefa)
        tarefas[index] = nova_tarefa
        print(f"Tarefa '{tarefa}' editada para '{nova_tarefa}'!")
    else:
        print(f"Tarefa '{tarefa}' nao encontrada!")
        
        # Teste do sistema
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer exercícios de POO")
adicionar_tarefa("Revisar encapsulamento")

listar_tarefas()

remover_tarefa("Estudar Python")
listar_tarefas()

adicionar_tarefa("Atualizar Wakatime")
adicionar_tarefa("Fazer commit dos exercicios")

listar_tarefas()

remover_tarefa("Atualizar Wakatime")
remover_tarefa("Estudar Python")

listar_tarefas()

editar_tarefa("Fazer exercícios de POO", "Fazer Praticas de POO")

listar_tarefas()




