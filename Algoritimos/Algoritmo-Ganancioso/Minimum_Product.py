# Calculando o menor produto

# 4 regras a serem seguidas:
# 1. Se houver um número par de números negativos e nenhum zero: Multiplica todos menos o maior negativo
# 2. Se houver um número ímpar de números negativos e nenhum zero: Multiplica todos menos o maior e o menor negativo
# 3. Se houver zeros e números positivos, mas nenhum número negativo: O menor produto será escolher o zero
# 4 Se não houver números negativos e todos os números forem positivos: O menor produto sera escolher o menor numero positivo
# Encontrar numero de negativos
# Encontrar numero de zeros
# Encontrar o minimo valor negativo
# Ecnotrar numero de não zeros
# Encontrar o produto da array


def minimumProduct(arr, n):
    if n == 1:
        return arr[0]
    
    max_neg = float('-inf')
    min_pos = float('inf')
    count_neg = 0
    count_zero = 0
    prod = 1
    
    for i in range(0, n):
        if (arr[i] == 0):
            count_zero += 1 # conta os zeros
            
        if (arr[i] < 0):
            count_neg += 1 # conta os negativos
            max_neg = max(max_neg, arr[i]) # encontrar o maior negativo
            
        if (arr[i] > 0):
            min_pos = min(min_pos, arr[i]) # encontrar o menor positivo
            
        prod *= arr[i] # encontrar o produto da array
        
    if count_neg == 0 and count_zero > 0: # se todos os numeros forem zero ou não tiver numeros negativos
        return 0        
    
    if (count_neg == 0): # se todos forem numero positivos
        return min_pos
    
    if ((count_neg & 1) == 0 and count_neg != 0): # se houver um par de numeros negativos e negativos diferente de zero
        prod = int(prod / max_neg)
        
    return prod

# Driver code
a = [-1, -1, -2, 4, 3]
n = len(a)
print(minimumProduct(a, n))