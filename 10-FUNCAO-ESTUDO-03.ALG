algoritmo "CALCULO DE FATORIAL COM FUNÇÃAO"
// Disciplina  :  [Linguagem e Lógica de Programação]
// Professor   : [Nome do Professor]
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
var

N, F: INTEIRO

FUNCAO FATORIAL (A: INTEIRO): INTEIRO
    VAR 
    T: INTEIRO
    INICIO
        T <- 1
        repita
            escreval(A)
            T <- T*A
            A <- A-1

        ate (A<1)
        RETORNE (T)
FIMFUNCAO
inicio

    escreva("DIGITE UM NUMERO: ")
    leia (N)

    F <- FATORIAL(N)

    escreval("O FATORIAL DE ", N, " E ", F)

fimalgoritmo