# Encontrar os 3 maiores elementos da array
# Percorrer a array 
# Encontar o maior elemento da array
# Encontar o segundo maior elemento da array
# Encontar o terceiro maior elemento da array
# Retornar os 3 maiores elementos da array
# se os elementos forem iguais, retornar apenas uma vez

def finding_three(arr):
    arr_size = len(arr)
    if arr_size < 3:
        return arr
    
    # Encontrar os 3 maiores elementos
    max1, max2, max3 = float('-inf'),float('-inf'), float('-inf')
    
    # Percorrer a array
    for i in range(arr_size):
        if arr[i] > max1: 
            max3 = max2
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] != max1:
            max3 = max2 
            max2 = arr[i]
        elif arr[i] > max3 and arr[i] != max1 and arr[i] != max2:
            max3 = arr[i]
    
    print("Os tres maiores elementos são", max1, max2, max3)
    
# Driver code
arr = [4, 3, 12, 1, 5, 5, 3, 9]
finding_three(arr)

