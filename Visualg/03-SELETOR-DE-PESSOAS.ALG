algoritmo "SELETOR DE PESSOAS"
var
   S, CONTINUE: CARACTERE
   I, C, HOMEM, MULHER: INTEIRO

inicio
   HOMEM <- 0
   MULHER <- 0
   S <- ""
   CONTINUE <- ""
   I <-0
   C <- 0
   REPITA
      ESCREVAL ("============================")
      ESCREVAL ("     SELETOR DE PESSOAS     ")
      ESCREVAL ("============================")
      REPITA
         ESCREVA ("QUAL O SEXO? [M/F]: ")
         LEIA (S)
         SE (S <> "M") E (S <> "F") ENTAO
            ESCREVAL ("ENTRADA INVALIDA, DIGITE M PARA MASCULINO OU F PARA FEMENINO")
         FIMSE
      ATE (S = "M") OU (S = "F")
      ESCREVA ("QUAL IDADE? ")
      LEIA (I)

      ESCREVAL ("QUAL COR DE CABELO? ")
      ESCREVAL ("_ _ _ _ _ _ _ _ _ _ ")
      ESCREVAL ("[1] PRETO")
      ESCREVAL ("[2] CASTANHO")
      ESCREVAL ("[3] LOIRO")
      ESCREVAL ("[4] RUIVO")
      LEIA (C)
      REPITA
         SE (C < 1) OU (C > 4) ENTAO
            ESCREVAL ("ENTRADA INVALIDA, DIGITE UM NUMERO ENTRE 1 E 4")
            LEIA (C)
         FIMSE
      ATE (C >= 1) E (C <= 4)
      SE (S = "M") E (I >= 18) E (C = 2) ENTAO
         HOMEM <- HOMEM+1
      SENAO
         SE (S = "F") E (I >= 25) E (I <= 30) E (C = 3) ENTAO
            MULHER <-MULHER+1
         FIMSE
      FIMSE
      REPITA
         ESCREVA ("QUER CONTINUAR? [S/N]: ")
         LEIA (CONTINUE)
         SE (CONTINUE <> "S") E (CONTINUE <> "N") ENTAO
            ESCREVA ("ENTRADA INVALIDA, DIGITE COM LETRA MAISCULA 'S' PARA SIM E 'N' PARA NAO")
         FIMSE
      ATE (CONTINUE = "S") OU (CONTINUE = "N")
      LIMPATELA
   ATE (CONTINUE = "N")
   LIMPATELA
   ESCREVAL ("======================================")
   ESCREVAL ("RESULTADO FINAL")
   ESCREVAL ("======================================")

   ESCREVAL ("HOMENS ACIMA DE 18 ANOS E CABELOS CASTANHOS: ", HOMEM)
   ESCREVAL ("MULHERES ENTRE 25 E 30 ANOS E CABELOS LOIROS: ", MULHER)
fimalgoritmo