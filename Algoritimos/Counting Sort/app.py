# Exercicio de Counting Sort

# idientificar o maior numero da lista
# Criar um vetor com o tamanho do maior numero + 1
# Todos elementos do vetor iniciam com 0
# Percorrer a lista e contar o numero de vezes que cada elemento aparece e preencher +1 no indice do vetor
# Preencher o vetor com a soma de 2 a 2 dos indices subsequentes. Sendo sempre um indice somado com o anterior. 
# Criar uma nova lista com quantidade de elementos igual ao da lista original
# Percorrer a lista original de tras para frente e preencher a nova lista com os elementos da lista original com o indice correspondente no vetor
# Após preencher a nova lista, decrementar 1 no indice do vetor de acordo com o elemento da nova lista
# Repetir até todos os numeros da primeira lista forem preenchidos

def count_sort(arr):
    M = max(arr)
    
    count = [0] * (M+1) # Criando um vetor com o tamanho do maior numero + 1
    
    for num in arr:
        count[num] += 1
        
    for i in range(1, M+1):
        count[i] += count[i-1]
        
    out = [0] * len(arr) # Criando saida do tamanho da lista principal
    
    for i in range(len(arr) -1, -1, -1):
        out[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        
    return out

# Driver code
if __name__ == "__main__":
    # Input array
    arr = [4, 3, 12, 1, 5, 5, 3, 9]

    # Output array
    out = count_sort(arr)

    for num in out:
        print(num, end=" ")
    
     