algoritmo "Nome do Programa"
// Disciplina  :  [Linguagem e Lógica de Programação]
// Professor   : [Nome do Professor]
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
var

NOME: VETOR[1..4] DE CARACTERE
N1: VETOR[1..4] DE REAL
N2: VETOR[1..4] DE REAL
M: VETOR[1..4] DE REAL
I, TOT: INTEIRO
SM, MT: REAL

inicio

PARA I <- 1 ATE 4 FACA
    escreval ("ALUNO ", I)
    ESCREVA ("NOME: ")
    LEIA (NOME[I])
    escreva("PRIMEIRA NOTA: ")
    LEIA (N1[I])
    escreva("SEGUNDA NOTA: ")
    LEIA (N2[I])
    M[I] <- (N1[1]+N2[I])/2
    SM <- SM + M[I]
FIMPARA
MT <- SM/4
LIMPATELA

escreval("LISTAGEM DE ALUNOS")
escreval("========================")
PARA I <- 1 ATE 4 FACA
    escreval(NOME[I]:15, M[I]:4:1)
    SE (M[I] > MT) ENTAO
        TOT <- TOT+1
    FIMSE    
FIMPARA    
ESCREVAL ("AO TODO TEMOS ", TOT, " ALUNOS ACIMA DA MEDIA DA TURMA QUE É ", MT:4:1)
fimalgoritmo