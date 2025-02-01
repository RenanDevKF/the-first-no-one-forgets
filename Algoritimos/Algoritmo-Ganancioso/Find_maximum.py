# Calcular a soma maxima de Stacks e conferir se a soma delas são iguais

# Definir a lista de numeros de cada stack
# Definir o tamanho da lista
# achar a soma inicial de cada Stack
# Encontar o primeiro elemento do topo da Stack


def maxSum(stack1, stack2, stack3, n1 , n2, n3):
    sum1, sum2, sum3 = sum(stack1), sum(stack2), sum(stack3) # encontra a soma de todas as stacks
    
    top1, top2, top3 = 0, 0, 0 # encontra o primeiro elemento do topo de cada stack
    
    while (1):
        if (top1 == n1 or top2 == n2 or top3 == n3):
            return 0 # se todos os elementos do topo forem iguais, retorna 0
        
        if (sum1 == sum2 and sum2 == sum3):
            return sum1 # se as somas forem iguais, retorna a soma
        
        if (sum1 >= sum2 and sum1 >= sum3):
            sum1 -= stack1[top1] # subtrai o topo da stack 1
            top1 += 1 
        
        elif (sum2 >= sum1 and sum2 >= sum3):
            sum2 -= stack2[top2] # subtrai o topo da stack 2
            top2 += 1
        
        else:
            sum3 -= stack3[top3] # subtrai o topo da stack 3
            top3 += 1
            
            # Driven Program
stack1 = [3, 2, 1, 1, 1]
stack2 = [4, 3, 2]
stack3 = [1, 1, 4, 1]

n1 = len(stack1)
n2 = len(stack2)
n3 = len(stack3)

print(maxSum(stack1, stack2, stack3, n1, n2, n3))
    
    
