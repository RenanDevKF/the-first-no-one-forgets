algoritmo "SOMA PARAMETRO POR REFERENCIA"
// Disciplina  :  [Linguagem e Lógica de Programação]
// Professor   : [Nome do Professor]
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
var
    X, Y: INTEIRO
    
PROCEDIMENTO SOMA (A,B: INTEIRO)
    INICIO
    A <- A+1
    B <- A+2

    escreval("VALOR DE A = ",A)
    escreval("VALOR DE B = ",B)

    escreval("VALOR DE A+B = ", A+B)
FIMPROCEDIMENTO    
inicio

    X <- 4
    Y <- 8
    SOMA (X,Y)

    escreval("VALOR DE X = ", X)
    escreval("VALOR DE Y = ", Y)
    escreval("VALOR DE X+Y = ", X+Y)

fimalgoritmo