# versão feita para otmisação a partir de uma função

def busca_binaria(arr, menor, maior, x):
    
    while menor <= maior:
        meio = (menor + maior) // 2
        if arr[meio] == x:
            return meio
        elif x < arr[meio]:
            maior = meio - 1
        else:
            menor = meio + 1
    return -1