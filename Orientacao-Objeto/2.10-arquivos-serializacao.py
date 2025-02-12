"""
Arquivos e Serialização em Python
Ao trabalhar com dados persistentes, frequentemente precisamos ler e gravar arquivos. Além disso, podemos serializar objetos Python para armazená-los ou 
transmiti-los. Vamos explorar esses conceitos em detalhes.

"""

#1. Manipulação de Arquivos em Python
#Podemos abrir, ler e escrever arquivos usando a função open().

# Abrindo e Lendo Arquivos
with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

"""
Explicação:

"r" → Modo de leitura.
encoding="utf-8" → Evita problemas com acentos.
with open(...) → Fecha o arquivo automaticamente.

Outros Modos de Abertura:
Modo	Descrição
"r"	Leitura (padrão). O arquivo deve existir.
"w"	Escrita (apaga o conteúdo anterior).
"a"	Acrescenta conteúdo ao final do arquivo.
"x"	Cria um novo arquivo (erro se já existir).
"b"	Modo binário (exemplo: imagens).
"""

# Escrevendo em Arquivos
with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Segunda linha do arquivo.\n")
"""
Explicação:

"w" → Apaga o conteúdo anterior e escreve novos dados.
write() → Escreve strings no arquivo.
"""

# Lendo Arquivo Linha por Linha
with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove quebras de linha extras

"""
O loop percorre cada linha do arquivo.
strip() remove espaços extras e \n
"""

#Adicionando Conteúdo a um Arquivo
with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Nova linha adicionada.\n")

# 2. Serialização de Objetos em Python
#A serialização converte objetos Python em um formato que pode ser salvo em arquivo ou enviado pela rede.
#O módulo pickle é o mais comum para serializar objetos Python.

import pickle

dados = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

with open("dados.pkl", "wb") as arquivo:
    pickle.dump(dados, arquivo)  # Serializa e salva o objeto

"""
Explicação:

pickle.dump(objeto, arquivo) → Salva o objeto no arquivo.
"wb" → Modo binário (obrigatório para pickle).
"""

#Lendo um Objeto Serializado (pickle)
with open("dados.pkl", "rb") as arquivo:
    dados_carregados = pickle.load(arquivo)  # Lê e desserializa
    print(dados_carregados)

"""
Explicação:

pickle.load(arquivo) reconstrói o objeto original.
"rb" → Modo leitura binário.
"""

#Serializando com json (Mais Portável)
#O formato JSON é mais legível e compatível com outras linguagens.

import json

dados = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

# Salvando como JSON

with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

"""
Explicação:

json.dump(objeto, arquivo) → Salva em JSON.
indent=4 → Formata com identação.

"""

# Lendo JSON
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)
    print(dados_carregados)

"""
3. Diferenças Entre pickle e json
Característica	pickle	json
Legibilidade	Binário (não legível)	Texto (legível)
Portabilidade	Apenas Python	Qualquer linguagem
Segurança	Inseguro para dados desconhecidos	Seguro
Velocidade	Rápido	Mais lento
- Use pickle para objetos Python complexos (classes, listas de objetos).
- Use json para compatibilidade entre linguagens e APIs.

Conclusão
✅ Manipular arquivos é essencial para armazenar e recuperar dados.
✅ A serialização permite salvar objetos Python para reutilização.
✅ pickle é útil para dados Python internos, enquanto json é universal.
✅ Saber a diferença entre pickle e json evita erros de compatibilidade e segurança. 
Tem alguma dúvida ou quer um exemplo específico? 
"""