# Opção 1:
# Encontrar a data futura mais proxima
# Definir array com datas disponiveius
# Definir array de consulta para encontrar a data futura mais proxima a ela
# Para cada data de consulta, percorrer o array de datas disponiveis e encontrar a data futura mais proxima
# Retornar a data futura mais proxima

#Opção 2:
# identificar a lista de datas disponiveis
# identificar a lista de datas de consulta
# Ordenar a lista de datas disponiveis de forma crescente
# Buscar a data futura mais proxima na lista de datas disponiveis usando busca binaria
# Retornar a data futura mais proxima

# Python3 program for the above approach
from bisect import bisect_right

def analise_data(date):
    """
    Converte uma string de data ("D/M/Y") para uma tupla numérica (Y, M, D),
    facilitando comparações e ordenações.
    """
    d, m, y = map(int, date.split("/"))
    return (y, m, d)

def data_futura(arr, query):
    """
    Retorna a data futura mais próxima de 'query' na lista 'arr'.
    Se não houver uma data futura, retorna "-1".
    """
    # Converter todas as datas para tuples (ano, mês, dia)
    arr_tuples = sorted(analise_data(date) for date in arr)  # Ordenação eficiente
    
    # Converter a query para o mesmo formato de comparação
    query_tuple = analise_data(query)
    
    # Usar busca binária para encontrar a primeira data futura
    index = bisect_right(arr_tuples, query_tuple)
    
    # Se houver uma data futura, retorna no formato original; senão, retorna "-1"
    return "{:02d}/{:02d}/{}".format(arr_tuples[index][2], arr_tuples[index][1], arr_tuples[index][0]) if index < len(arr_tuples) else "-1"


def main():
    arr = ["22/4/1233", "1/3/633", "23/5/56645", "4/12/233"]
    queries = ["23/3/4345", "12/3/2"]
    
    print("Datas disponíveis:", arr)
    print("Consultas:", queries)
    
    for query in queries:
        print(f"Para a data {query}, a próxima data mais próxima é:", data_futura(arr, query))

if __name__ == "__main__":
    main()