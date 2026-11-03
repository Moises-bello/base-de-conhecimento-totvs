---
content_hash: 40748995601ed2fac3b459818f431b5d2cacb4c30af179bf5097c79ebe982ded
fetched_at: '2026-06-29T00:10:06.816371+00:00'
page_id: '452719340'
product: rm
source: tdn-rm
title: Fórmulas / Funções – S
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719340
version: 5
---

**Função Salario Composto**  
Retorna o valor do salário composto cadastrado em Funcionário l Anexo l Folha Pagamento l Salario Composto   
SALARIOCOMPOSTO (VALOR)  
   
Onde  
**Valor-**Número do salário  
   
   
**Exemplo:**  
O funcionário possui o salario composto conforme abaixo:  
   
**Evento**     **Nº do salário    Valor Mensal    Ref     Jornada**      **Desc do Evento    Valor da Hora     J Mensal**   
 0001                 1                     1000                   0               220             Horas Normais               0                               0  
 0086                 2                     1500                   0                                        Extra                       10                               0  
   
   
             SALARIOCOMPOSTO (1) Irá retornar 1000  
             SALARIOCOMPOSTO (2) Irá retornar 1500  
   
   
   
**Função SALPER**  
Retorna valor do salário em um intervalo de datas.  
SALPER (DATA, DATA, STRING, VALOR, STRING)  
   
Onde  
**Parâmetro 1 - DATA DE INÍCIO - data**  
Data de início do período a ser considerado dentro da competência atual. Se informado data nula ('00/00/0000'), será assumido o primeiro dia do mês.  
**Parâmetro 2 - DATA FINAL - data**  
Data final do período a ser considerado dentro da competência atual. Se informado data nula ('00/00/0000'), será assumido o último dia do mês.  
**Parâmetro 3 - CÓDIGO DO EVENTO - string**  
Para funcionários que utilizam salário composto:   
Se informado string nula ('') , será considerado o valor total do salário composto.   
Se o código informado constar no salário composto, será considerado o valor do evento. Caso contrário, é retornado o valor 0 (zero).   
Para funcionários que não possuem salário composto:   
Dev ser informado string nula ('') nesse parâmetro.   
Será considerado o valor integral do salário.   
**Parâmetro 4 - FORMA DE CÁLCULO - valor**  
Informar 0 (zero) para cálculo com calendário comercial (30 dias) ou 1 (um) para cálculo com calendário gregoriano (normal).  
**Parâmetro 5 - AUSÊNCIAS CONSIDERADAS - string**  
Esse parâmetro permite que a fórmula flexibilize o cálculo, considerando ou não ausências no mês motivadas por férias, afastamentos, admissão e demissão.

O formato desse parâmetro é uma string com quatro letras: **'ABCD'**, onde: **A, B, C e D** representam posições para os caracteres 'S' (Sim) ou 'N' (Não).  
Na posição A, informar 'S' ou 'N', para deduzir ou não os dias ausentes decorrentes de FÉRIAS.  
Na posição B, informar 'S' ou 'N', para deduzir ou não os dias ausentes decorrentes de AFASTAMENTOS.  
Na posição C, informar 'S' ou 'N', para deduzir ou não os dias anteriores à ADMISSÃO.  
Na posição D, informar 'S' ou 'N', para deduzir ou não os dias posteriores à DEMISSÃO.  
String nula ('') é similar a todas as posições preenchidas com 'S'.  
   
**Exemplos de preenchimento:**  
' ' ou 'SSSS' - considera férias, afastamentos, admissão e demissão.  
'NNSS' - ignora férias e afastamentos, considera admissão e demissão.  
  'NNNN' - ignora quaisquer dias de ausência.  
   
   
   
**Função SALVAVALDEP**  
Esta variável é utilizada na montagem da fórmula de assistência médica, para que o sistema preencha os dados do Histórico de Assistência a Saúde no cadastro do funcionário.  
   
**1º Parâmetro**: Deverá informar o número do beneficiário. Sempre que o beneficiário for o funcionário deverá informar 0(zero).  
   
**2º Parâmetro**: Deverá informar o valor do desconto deste beneficiário.  
   
**Exemplo**  
O usuário já utiliza a fórmula abaixo para desconto da assistência médica, sendo que a fórmula verifica se o dependente tem incidência em 'Assistência Médica' e se a idade é maior ou menor e igual à 18 anos:  
   
DECL DEP,SOMADEP,SOMAFUN;  
SETVAR(DEP,1);  
SETVAR(SOMADEP,0);  
   
REPITA   
SE TABDEP ('INCASSISTMEDICA' ,'V', DEP)=1 ENTAO   
   SE NDEPIDADE (DEP,HOJE)<=18  
       ENTAO SETVAR(SOMADEP,SOMADEP+121)   
                    SENAO   
                       SE NDEPIDADE (DEP,HOJE)<=23  
                          ENTAO SETVAR(SOMADEP,SOMADEP+189)          
     SENAO 0 FIMSE FIMSE FIMSE;   
   
SETVAR(DEP,DEP+1) ATE DEP=10;  
   
SE TABCOMPL('ASSISTENCIAMEDICA','S')='S'   
      ENTAO SE IDADE(HOJE)<=18   
         ENTAO SETVAR(SOMAFUN,SOMAFUN+121)   
            SENAO SE IDADE(HOJE)<=23   
                ENTAO SETVAR(SOMAFUN,SOMAFUN+189)  
                   SENAO 0   
            FIMSE   
     FIMSE   
FIMSE;  
   
SOMADEP+SOMAFUN  
   
DECL DEP,SOMADEP,SOMAFUN;  
SETVAR(DEP,1);  
SETVAR(SOMADEP,0);  
   
REPITA   
SE TABDEP ('INCASSISTMEDICA' ,'V', DEP)=1 ENTAO   
   SE NDEPIDADE (DEP,HOJE)<=18  
      ENTAO   
**SALVAVALDEP(DEP,121);**  
            SETVAR(SOMADEP,SOMADEP+121)   
                    SENAO   
                       SE NDEPIDADE (DEP,HOJE)<=23  
                          ENTAO   
**SALVAVALDEP(DEP,189);**  
            SETVAR(SOMADEP,SOMADEP+189)      
SENAO 0 FIMSE FIMSE FIMSE;   
   
SETVAR(DEP,DEP+1) ATE DEP=10;  
   
SE TABCOMPL('ASSISTENCIAMEDICA','S')='S'   
      ENTAO SE IDADE(HOJE)<=18   
      ENTAO      
 **SALVAVALDEP(0,121);**   
                                           SETVAR(SOMAFUN,SOMAFUN+121)    
                         
            SENAO SE IDADE(HOJE)<=23   
                                      ENTAO    
  **SALVAVALDEP(0,189);**  
                                           SETVAR(SOMAFUN,SOMAFUN+189)   
  
 SENAO 0   
            FIMSE   
     FIMSE   
FIMSE;  
   
SOMADEP+SOMAFUN  
   
**Atenção:**  
**01 -** Quando houver restituição do valor da assistência à saúde, para que o sistema alimente a tabela automaticamente, o usuário deverá criar uma fórmula informando o valor negativo.   
**Exemplo:** -100

**Função SD**  
Retorna salário-família diário. (mensal dividido por 30)  
SD  
   
   
**Atenção:**  
As variáveis de fórmula que são relativas a movimentação do funcionário, como a **SD**, não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".  
   
   
**Função Secant**  
Retorna a seção onde estava locado um determinado funcionário na data informada.  
SECANT('DATA')  
   
   
**Função Setvar**  
Atribui um valor a uma variável.  
   
   
**Função SF**  
Retorna a base de salário-família, considerando inclusive os eventos CC(01) - Horas Normais e CC(02) Dias Trabalhados.  
SF  
   
**Atenção:**  
As variáveis de fórmula que são relativas a movimentação do funcionário, como a **SF**, não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".  
   
**Função SFUNC**  
Retorna a situação do funcionário (ativo, afastado, etc.)  
SFUNC  -String  
   
   
**Função SFUNCDATA**   
Retorna a situação do funcionário em uma determinada data (ativo, afastado, etc.)  
SFUNCDATA(DATA)  
   
**Exemplo:**  
-SFUNCDATA('01/01/2015')  
/**Retorna a situação do funcionário na data 01/01/2015**/  
-SFUNCDATA(MTDATA(1,MES,ANO))  
/\*Primeiro dia do mês \*/  
   
   
**Função SM**  
Retorna o salário mínimo nacional.  
SM  
   
   
**Função SMSIND**  
Retorna salário mínimo do sindicato.  
SMSIND  
   
   
   
**Função STR**  
Retorna número de acordo com máscara informada, que pode ser composta da seguinte forma:  
com noves: o número será completado com espaços brancos à esquerda; com zeros ou 'z' (minúsculo ou maiúsculo): o número será completado com zeros à esquerda  
(Pode-se usar separador de decimais: '.' (ponto) ou ',' (vírgula)  
STR (VALOR, STRING)  
   
**Exemplo:**  
STR (RC, '999') - retornará o salário do empregado do empregado com zeros à esquerda.   
STR (27, '000') - retornará 027  
STR (12, '99,99') - retornará 12,00  
STR (5, '00.00') - retornará 05.00  
   
   
   
**Função STRLEFT**  
Retorna "n" caracteres da string a partir da direita para a esquerda.  
STRLEFT (STRING, Nº DE CARACTERES)  
   
**Exemplo:**  
*STRLEFT (TABPESSOA ('NOME', 'S'), 5)*  
Nome do funcionário: ITAMAR MENDES DA SILVEIRA.Retornará "VEIRA  
   
**Função STRRIGHT**  
Retorna "n" caracteres da string a partir da esquerda para a direita.  
STRRIGHT (STRING, Nº DE CARACTERES)  
   
**Exemplo:**  
**STRRIGHT ((TABPESSOA ('NOME', 'S'), 6)**  
Nome do funcionário: ITAMAR MENDES DA SILVEIRA

Retornará: ITAMAR.    
   
   
**Função SUBSTR**  
Retorna pedaço de uma string, a partir de uma posição determinada.  
SUBSTR ( STRING, INÍCIO, NÚMERO DE CARACTERES)  
   
   
**Exemplo:**  
**SUBSTR( TABPESSOA ('NOME' , 'S'), 1 , 10)**  
Essa fórmula retornará o nome do funcionário com dez caracteres a partir da primeira posição do nome.  
Sobre a função TABPESSOA, incluída no exemplo, ver o tópico **Funções - T**.   
**SUBSTR( TABPESSOA ('NOME' , 'S'), 8 , 18)**  
Nome do funcionário: ITAMAR MENDES DA SILVEIRA.   
Retornará: MENDES DA SILVEIRA.  
   
   
   
**Função SUBTRAIDATAS**   
Retorna a subtração entre duas datas.  
SUBTRAIDATAS (DATA, DATA)  
   
**Exemplo:**  
SUBTRAIDATAS('30/01/2014','01/12/2013')=60  
   
**Função SALDOBANCOHORASCHRONUS** Retorna o valor do saldo de banco de horas do funcionário até a data informada. SALDOBANCOHORASCHRONUS('DATA')  
   
**Função SALDOCOMPBANCOHORASCHRONUS** Retorna o valor de Extras que foram utilizadas na Compensação de Banco de Horas até a data informada. SALDOCOMPBANCOHORASCHRONUS('DATA')
