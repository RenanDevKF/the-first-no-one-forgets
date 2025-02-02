# identtidicar uma array
# Dimensionar o tamanho da array
# Percorrer a array um numero de vezes
# Rotacionar os elementos da array a cada passo
# Imprimir a array depois do numero de rotações determinada

def reverse(arr, s, e):
    while s < e:
        arr[s], arr[e] = arr[e], arr[s] # swap
        s += 1
        e -= 1
    
def rotation(arr, n, k):
    reverse(arr, 0, n-1) # reverter toda a array
    reverse(arr, 0, k-1) # reverter os primeiros k elementos
    reverse(arr, k, n-1) # reverter os restantes elementos
    
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
        
# driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
n = len(arr)
k = 3
rotation(arr, n, k)
printArray(arr, n)