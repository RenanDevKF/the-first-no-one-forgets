algoritmo "Nome do Programa"
// Disciplina  :  [Linguagem e Lógica de Programação]
// Professor   : [Nome do Professor]
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
var

VAL: VETOR[1..7] DE INTEIRO
I, TOTPAR: INTEIRO

inicio

PARA I <- 1 ATE 7 FACA
    ESCREVA ("DIGITE O ", I, "o. VALOR: ")
    LEIA(VAL[I])
FIMPARA 

PARA I <- 1 ATE 7 FACA
    SE (VAL[I] % 2 = 0) ENTAO
        TOTPAR <- TOTPAR+1
        ESCREVAL ("VALOR PAR NA POSICAO ", I)
    FIMSE
FIMPARA  
escreval("O TOTA DE NUMEROS PAR É, ", TOTPAR)
fimalgoritmo