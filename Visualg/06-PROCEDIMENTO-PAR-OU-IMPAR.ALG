algoritmo "PROCEDIMENTO PAR OU IMPAR"
// Disciplina  :  [Linguagem e Lógica de Programação]
// Professor   : [Nome do Professor]
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
var

N: INTEIRO

PROCEDIMENTO PAROUIMPAR (V: INTEIRO)
INICIO
    SE (V % 2 = 0) ENTAO
        escreval("O NUMERO ",V, " É PAR")
        SENAO
        escreval("O NUMERO ",V, " É IMPAR")
    FIMSE
FIMPROCEDIMENTO

inicio
    escreva("DIGITE UM NUMERO: ")
    LEIA (N)
    PAROUIMPAR (N)

fimalgoritmo