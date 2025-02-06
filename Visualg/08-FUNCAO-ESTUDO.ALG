algoritmo "parImpar com FUNCAO"
// Disciplina  :  [Linguagem e Lógica de Programação]
// Professor   : [Nome do Professor]
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
var
    N: INTEIRO
    R: CARACTERE

    FUNCAO PAROUIMPAR(A: INTEIRO): CARACTERE

    INICIO
        SE (A % 2 = 0) ENTAO
            RETORNE "PAR"
            SENAO
            RETORNE "IMPAR"
        FIMSE
        
    FIMFUNCAO        
inicio
    escreval("DIGITE UM NUMERO: ")
    LEIA (N)
    R <- PAROUIMPAR (N)
    escreva("O NUMERO ", N, " E UM VALOR ", R)
    
fimalgoritmo