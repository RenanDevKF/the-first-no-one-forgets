"""
Tratamento de Erros e Exceções em POO com Python
📌 Introdução ao Tratamento de Erros e Exceções
Quando programamos em Python, erros podem acontecer por vários motivos, como entrada inválida do usuário, divisões por zero ou acessos a variáveis inexistentes. Em programação orientada a objetos (POO), o tratamento de exceções é essencial para tornar o código mais robusto e confiável.

O Python possui um mecanismo de try-except-finally para capturar e tratar erros, evitando que o programa quebre inesperadamente.

🔹 1. O Que São Exceções?
Uma exceção é um evento que ocorre durante a execução de um programa e interrompe seu fluxo normal. Alguns exemplos de exceções comuns em Python:

ZeroDivisionError: Quando tentamos dividir um número por zero.
ValueError: Quando um valor inválido é passado para uma função.
TypeError: Quando um tipo incorreto é utilizado em uma operação.
IndexError: Quando acessamos um índice inexistente em uma lista.
KeyError: Quando tentamos acessar uma chave inexistente em um dicionário.
"""

# Exemplo de erro sem tratamento:
def dividir(a, b):
    return a / b  # Isso pode causar ZeroDivisionError

print(dividir(10, 0))  # Vai gerar um erro e interromper o programa

# Isso resultará em:
# Para evitar que o programa quebre, utilizamos try-except.

'ZeroDivisionError: division by zero'

# 2. Usando Try e Except para Tratar Exceções
# Podemos capturar exceções usando um bloco try-except:

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero não é permitida"

print(dividir(10, 0))  # Agora o erro é tratado

#Saída:
#Erro: divisão por zero não é permitida

#Capturando Vários Tipos de Exceção
#Podemos capturar diferentes tipos de erro no mesmo bloco:

def processar_numero():
    try:
        num = int(input("Digite um número: "))
        resultado = 10 / num
        print("Resultado:", resultado)
    except ValueError:
        print("Erro: Você precisa digitar um número válido!")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
    except Exception as e:  # Captura qualquer outro erro
        print(f"Erro inesperado: {e}")

processar_numero()

# 3. Bloco Finally: Executando Código Sempre
# O finally é executado independentemente de um erro ter ocorrido ou não. Isso é útil para liberar recursos, fechar arquivos ou conexões com banco de dados.

def abrir_arquivo():
    try:
        arquivo = open("dados.txt", "r")
        conteudo = arquivo.read()
        print(conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado")
    finally:
        print("Finalizando operação")

abrir_arquivo()

# Mesmo que o arquivo não exista, o finally será executado

# 4. Lançando Exceções Personalizadas com raise
#  Podemos criar nossas próprias exceções usando raise. Isso é útil quando queremos validar condições específicas.

def verificar_idade(idade):
    if idade < 18:
        raise ValueError("Erro: A idade deve ser maior ou igual a 18")
    return "Acesso permitido"

try:
    print(verificar_idade(15))
except ValueError as e:
    print(e)

#Saída:
#Erro: A idade deve ser maior ou igual a 18

#5. Criando Exceções Personalizadas com Classes
# Podemos definir nossas próprias exceções herdando da classe Exception:

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor_saque):
        super().__init__(f"Erro: Saldo insuficiente! Saldo disponível: {saldo}, Saque solicitado: {valor_saque}")

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    saldo -= valor
    return saldo

try:
    saldo_atual = 100
    saldo_atual = sacar(saldo_atual, 200)
except SaldoInsuficienteError as e:
    print(e)

#Saída:
#Erro: Saldo insuficiente! Saldo disponível: 100, Saque solicitado: 200

#6. Exceções em Métodos de Classes
# Podemos tratar exceções dentro de classes para tornar nossos objetos mais seguros.

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def sacar(self, valor):
        try:
            if valor > self.saldo:
                raise SaldoInsuficienteError(self.saldo, valor)
            self.saldo -= valor
            return self.saldo
        except SaldoInsuficienteError as e:
            print(e)

conta = ContaBancaria(500)
conta.sacar(700)  # Vai gerar um erro tratado

"""
📌 Resumo:
✅ Exceções ajudam a tornar o código mais robusto e seguro.
✅ try-except-finally é usado para capturar e tratar erros.
✅ Podemos capturar múltiplas exceções com diferentes blocos except.
✅ Exceções personalizadas permitem maior controle e clareza nos erros.
✅ O uso de raise permite lançar exceções quando condições específicas são violadas.

💡 Agora pratique implementando exceções em suas classes e métodos!

1. Estrutura da Hierarquia de Exceções
Abaixo está um resumo das principais exceções organizadas hierarquicamente:

BaseException
│
├── SystemExit         # Sinaliza saída do sistema (não deve ser capturado normalmente)
├── KeyboardInterrupt  # Interrupção do usuário (Ctrl + C)
├── Exception          # Classe base para a maioria das exceções
│   │
│   ├── ArithmeticError    # Erros matemáticos
│   │   ├── ZeroDivisionError  # Divisão por zero
│   │   ├── OverflowError      # Número muito grande para ser representado
│   │   └── FloatingPointError # Erros em operações de ponto flutuante
│   │
│   ├── LookupError       # Erros em buscas (índices e chaves inválidas)
│   │   ├── IndexError     # Índice inválido em listas, tuplas
│   │   └── KeyError       # Chave inválida em dicionários
│   │
│   ├── ValueError        # Tipo correto, mas valor inválido
│   ├── TypeError         # Tipo de dado incompatível
│   ├── AttributeError    # Atributo não encontrado em um objeto
│   ├── FileNotFoundError # Arquivo não encontrado
│   ├── ImportError       # Erro ao importar módulos
│   ├── NameError         # Variável não definida
│   ├── RuntimeError      # Erros genéricos em tempo de execução
│   └── ... (Outras exceções específicas)

"""