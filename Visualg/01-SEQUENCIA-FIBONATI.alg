algoritmo "Sequencia de Fibonati"
// Disciplina  :  [Linguagem e Lógica de Programação]
// Professor   : GUSTAVO GUANABARA DO CURSO EM VIDEO
// Descrição   : ESSE PROGRAMA CALCULA A SEQUENCIA DE FIBONACCI
// Autor(a)    : RENAN KIRCHMAIER FAYER
// DATA_ATUAL  : 20/01/2025
var

C1, C2, CC, CT: inteiro

inicio
    C1 <- 0
    C2 <- 1
    ESCREVA (C1)
    ESCREVA (C2) 
            CC <- C1+C2  
    PARA CT <- 3 ate 15 passo 1 FACA 
            escreva (CC)
            C1 <- C2
            C2 <- CC 
    FIMPARA
    ESCREVAL ("")
    ESCREVAL ("")
    ESCREVAL ("SEQUENCIA DE FIBONACCI ESCRITA COM SUCESSO")     


fimalgoritmo