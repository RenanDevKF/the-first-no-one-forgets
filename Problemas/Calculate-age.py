# calculando idade a partir de data de aniversario

def calcular_idade (dia_atual, mes_atual, ano_atual, dia_aniversario, mes_aniversario, ano_aniversario):
    
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dia_aniversario > dia_atual:
        mes_atual = mes_atual - 1
        dia_atual = dia_atual + meses[mes_aniversario - 1]
    if mes_aniversario > mes_atual:
        ano_atual = ano_atual - 1
        mes_atual = mes_atual + 12
        
    calculando_data = dia_atual - dia_aniversario
    calculando_mes = mes_atual - mes_aniversario
    calculando_ano = ano_atual - ano_aniversario
    return calculando_ano, calculando_mes, calculando_data


def main():
    # Data atual
    dia_atual = 2
    mes_atual = 2
    ano_atual = 2025

    # Data de nascimento
    dia_aniversario = 31
    mes_aniversario = 12
    ano_aniversario = 1989

    # Chamando a função
    anos, meses, dias = calcular_idade(dia_atual, mes_atual, ano_atual, dia_aniversario, mes_aniversario, ano_aniversario)

    # Exibindo o resultado
    print("Idade calculada:")
    print(f"{anos} anos, {meses} meses e {dias} dias")

# Executar o driver code
if __name__ == "__main__":
    main()

