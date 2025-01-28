algoritmo "Nome do Programa"
// Disciplina  :  [Linguagem e Lógica de Programação]
// Professor   : [Nome do Professor]
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
var

NOME: CARACTERE
SOC: VETOR[1..10] DE CARACTERE
C, TOT: INTEIRO

inicio

TOT <- 0
PARA C <- 1 ATE 10 FACA
    ESCREVA ("DIGITE SEU NOME: ")
    LEIA (NOME)
    SE (COPIA(maiusc(NOME), 1,1) = "C") ENTAO
        TOT <- TOT+1
        SOC[TOT] <- NOME
    FIMSE
FIMPARA

LIMPATELA
escreval("LISTAGEM FINAL")
PARA C <- 1 ATE TOT FACA
    ESCREVAL(SOC[C])
FIMPARA    

fimalgoritmo