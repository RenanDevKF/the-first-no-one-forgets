algoritmo "DETECTOR DE PESADO"
    // Disciplina  :  [Linguagem e Lógica de Programação]
    // Professor   : [Nome do Professor]
    // Descrição   : Aqui você descreve o que o programa faz! (função)
    // Autor(a)    : Nome do(a) aluno(a)
    // Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
    var

    N, PESADO: CARACTERE
    P, MAI: REAL
    I: INTEIRO

    PROCEDIMENTO TOPO ()
    INICIO
    LIMPATELA
    escreval ("=================================================")
    escreval ("              DETECTOR DE PESADO                 ")
    escreval ("        MAIOR PESO ATE AGORA: ", MAI, "KG"        )
    escreval ("=================================================")
    FIMPROCEDIMENTO

    inicio
    TOPO()
    PARA I <- 1 ATE 5 PASSO 1 FACA
        escreva("DIGITE UM NOME: ")
        LEIA (N)
        escreva("DIGITE O PESO DE ", N, ": ")
        LEIA (P)
        SE (P>MAI) ENTAO 
        MAI <- P
        PESADO <- N
        FIMSE
        TOPO ()
    FIMPARA
    TOPO ()

fimalgoritmo