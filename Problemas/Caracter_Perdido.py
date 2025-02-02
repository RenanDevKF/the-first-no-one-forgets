# Crie um conjunto vazio para fazer o controle de caracteres presentes
# Crie um laço para percorrer a string
# Verifique se o caracter pertence ao alfabeto
# Se o caracter foi minusculo, adicione-o ao conjunto
# Se for maiusculo, converta em minusculo e adicione-o ao conjunto
# Tenha uma string vazia para armazenar os caracteres ausentes
# Intere cada letra minuscula de "a" a "z" no conjunto
# Se a letra nao estiver no conjunto, adicione-a ao conjunto de caracteres ausentes
# Se a sequencia de caracteres ausentes estiver vazia, a entrada é um pangrama
#  Caso contrario, imprima a sequencia de caracteres ausentes

def main():
    entrada = "O rato roeu a roupa do rei de roma"
    conjunto = set()
    for i in entrada:
        if i.isalpha():
            conjunto.add(i.lower()) # add() adiciona um elemento ao conjunto e lower() converte para minusculo
            
    char_perdido = "".join(c for c in "abcdefghijklmnopqrstuvwxyz" if c not in conjunto) # .join() junta os caracteres em uma string e "c for c in" percorre o conjunto retornando cada caracter
    
    if not char_perdido:
        print("Esta frase já contém todas as letras do alfabeto! É um pangrama.")

    else:
        print(f" As Letras que faltam para formar um pangrama: {char_perdido}")
        
if __name__ == "__main__":
   main()
   