# Maximize Array

# Definir os numeros da lista
# Definir o tamanho da lista
# Percorrer a lista um numero K de vezes
# Achar um numero negativo da lista e transformar em positivo
# Se o Numero K vezes ainda nao estiver finalizado, fazer trocar de positivo e negativo com o menor numero da lista ate K = 0

def SomaMaxima (arr, n, k):

    for i in range(1, k+1): # Percorrer a lista K vezes
        min = +10000 # Definir o maior numero possivel
        index = -1 
        
        for j in range(n): # Percorrer a lista
            if (arr[j] < min):
                min = arr[j]
                index = j
        if (min==0):
            break
        arr[index] = -arr[index] # Transformar o numero negativo em positivo
        
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum

# Driver code
arr = [-2, 0, 5, -1, 2]
k = 4
n = len(arr)
print(SomaMaxima(arr, n, k))