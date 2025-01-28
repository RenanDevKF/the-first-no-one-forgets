algoritmo "Nome do Programa"
// Disciplina  :  [Linguagem e Lógica de Programação]
// Professor   : [Nome do Professor]
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
var

N: CARACTERE
C: INTEIRO
inicio

escreva("DIGITE SEU NOME: ")
leia(N)
escreval("TOTAL DE LETRAS DO SEU NOME: ", compr(N))
escreval("SEU NOME EM MAISCULAS E ", maiusc(N))
escreval("SEU NOME EM MINUSCULA E ", minusc(N))
escreval("A PRIMEIRA LETRA DO SEU NOME É ", COPIA(N, 1, 1))
escreval("A ULTIMA LETRA DO SEU NOME É ", COPIA(N, compr(N), 1))
escreval("SEU NOME TEM A LETRA A NA POSIÇÃO ", pos("A", maiusc(N)))
escreval("O CODIGO DA LETRA A E ", asc("A"))
escreval("A LETRA DE CODIGO 1 E ", CARAC(1))

PARA C<- compr(N) ATE 1 PASSO -1 FACA
    escreval (copia (maiusc(N),C,1))
FIMPARA    
fimalgoritmo