import pandas as pd

# Nome do arquivo CSV original
arquivo_original = "resultados.csv"

# Nome do novo arquivo corrigido
arquivo_corrigido = "resultados_lotofacil_corrigido.csv"

# Lê o arquivo CSV, tratando os espaços nos números
with open(arquivo_original, "r", encoding="utf-8") as file:
    linhas = file.readlines()

# Corrige os espaços transformando-os em vírgulas
linhas_corrigidas = []
for linha in linhas:
    partes = linha.strip().split(",")  # Separa o concurso do restante
    if len(partes) > 1:
        numeros_corrigidos = partes[1].replace(" ", ",")  # Substitui espaços por vírgulas nos números
        linha_corrigida = f"{partes[0]},{numeros_corrigidos}\n"
    else:
        linha_corrigida = linha
    linhas_corrigidas.append(linha_corrigida)

# Salva o arquivo corrigido
with open(arquivo_corrigido, "w", encoding="utf-8") as file:
    file.writelines(linhas_corrigidas)

print("Arquivo corrigido salvo como:", arquivo_corrigido)
