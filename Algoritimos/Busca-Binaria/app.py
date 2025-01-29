# versão feita baseada no raciocionio logico a ser seguido


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 23

inicio = 0
fim = len(arr) - 1  # Corrigindo fim para o último índice

while inicio <= fim:
    meio = (inicio + fim) // 2
    
    if arr[meio] == x:
        print(meio)  # Encontrou o elemento
        break
    elif x < arr[meio]:
        fim = meio - 1  # Ajusta o limite direito
    else:
        inicio = meio + 1  # Ajusta o limite esquerdo
else:
    print("Nao encontrado")  # Se sair do while, significa que x não está no array  




