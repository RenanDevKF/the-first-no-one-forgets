# Minimum Sum

# Definir a lista de numeros
# Achar o menor numero da lista de numeros
# Comparar o menoro numero da lista A com os demais numeros da lista
# Tirar o maior numero da lista e copiar o menor para outra lista B
# Repetir ate que sobre apenas o menor numero na lista A
# Retornar a soma da lista B

def min_sum(arr):
    
    min_val = min(arr)
    
    return min_val * (len(arr) - 1)

# driver code 
A = [7, 2, 3, 4, 5, 6]  
print (min_sum(A))



