    algoritmo "SOMA FUNCAO"
    // Disciplina  :  [Linguagem e Lógica de Programação]
    // Professor   : [GUSTAVO GUANABARA]
    // Descrição   : Aqui você descreve o que o programa faz! (função)
    // Autor(a)    : Nome do(a) aluno(a)
    // Data atual  : DATA_ATUAL/MES_ATUAL/ANO_ATUAL
        var
        N1, N2, RES: INTEIRO

        FUNCAO SOMA (A, B: INTEIRO): INTEIRO
        VAR
        S: INTEIRO // EU PODERIA SUBSTITUIR TODO ESSE PASSO DE VAR ATE RETORNE PARA UM SIMPLES (RETORNE A + B)
        INICIO
            S <- A + B 
            RETORNE S 
            FIMFUNCAO

            inicio
            ESCREVA ("DIGITE UM VALOR: ")
            LEIA (N1)
            escreva("DIGITE OUTRO VALOR: ")
            LEIA (N2)
            
            RES <- SOMA(N1,N2)

            ESCREVAL ("A SOMA É ", RES)
        
    fimalgoritmo