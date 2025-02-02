# Contar tipos diferentes de strings em uma frase
# Pesrcorrer toda string do indice 0 ao final
# Verificar se o elemento da  string é minusculo, maisculos, um numero ou caracter especial
# Contar quantos minusculos, quantos maiusculos, quantos numeros e quantos caracteres especiais tem na frase

def count (string):
    lower = 0
    upper = 0
    number = 0
    special = 0
    for i in range(len(string)):
        if string[i].islower():
            lower += 1
        elif string[i].isupper():
            upper += 1
        elif string[i].isdigit():
            number += 1
        else:
            special += 1
    return lower, upper, number, special

# Driver Code

if __name__ == "__main__":
    # Exemplo 1
    string_1 = "Olá Mundo! 123"
    print("Exemplo 1:")
    print(f"Entrada: {string_1}")
    lower, upper, number, special = count(string_1)
    print(f"Letras minúsculas: {lower}")
    print(f"Letras maiúsculas: {upper}")
    print(f"Números: {number}")
    print(f"Caracteres especiais: {special}")
    
    # Exemplo 2
    string_2 = "Python 3.9! #É muito bom!"
    print("\nExemplo 2:")
    print(f"Entrada: {string_2}")
    lower, upper, number, special = count(string_2)
    print(f"Letras minúsculas: {lower}")
    print(f"Letras maiúsculas: {upper}")
    print(f"Números: {number}")
    print(f"Caracteres especiais: {special}")
    
    # Exemplo 3
    string_3 = "1234567890"
    print("\nExemplo 3:")
    print(f"Entrada: {string_3}")
    lower, upper, number, special = count(string_3)
    print(f"Letras minúsculas: {lower}")
    print(f"Letras maiúsculas: {upper}")
    print(f"Números: {number}")
    print(f"Caracteres especiais: {special}")
    
    # Exemplo 4
    string_4 = "!!@#$%^&*()_+"
    print("\nExemplo 4:")
    print(f"Entrada: {string_4}")
    lower, upper, number, special = count(string_4)
    print(f"Letras minúsculas: {lower}")
    print(f"Letras maiúsculas: {upper}")
    print(f"Números: {number}")
    print(f"Caracteres especiais: {special}")