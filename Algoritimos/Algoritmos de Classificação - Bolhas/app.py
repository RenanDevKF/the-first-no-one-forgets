# Exercicio de algoritmos de classificação - Bolhas

#Idenditficar o tamanho da lista
#Percorrer a lista
#Comparar os elementos adjacentes
#ordenar a lista

def bubblesort(lista):
    n=len(lista)
    for i in range(n):
        troca = False
    
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                troca = True
            
        if (troca == False):
            break    

# Driver code to test above
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]

    bubblesort(lista)

    print("Lista ordenada:")
    for i in range(len(lista)):
        print("%d" % lista[i], end=" ")