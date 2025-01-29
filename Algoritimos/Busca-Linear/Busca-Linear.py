#logica a ser seguida
#identificar a lista e seus numeros inteiros
#averiguar o numero que deve ser achado
#verificar se o numero esta na lista
#se estiver, imprimir a posicao
#se nao estiver, imprimir a mensagem de nao encontrado

def encontrar_indice(arr, x):
    for i in range(len(arr)):  # Percorre o array
        if arr[i] == x:  # Compara cada elemento com x
            return i  # Retorna o índice da primeira ocorrência
    return -1  # Retorna -1 se x não for encontrado

# Exemplo de uso:
arr = [3, 5, 7, 9, 5]
x = 5
print(encontrar_indice(arr, x))  # Saída: 1

    

