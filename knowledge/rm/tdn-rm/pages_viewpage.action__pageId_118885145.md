---
content_hash: dcfe236da08f93e3325e5544abbb27d2939dda6de64fb51a6a46627089bf37c6
fetched_at: '2026-06-29T00:05:54.989131+00:00'
page_id: '118885145'
product: rm
source: tdn-rm
title: COMO FAZER - INSS AUTÔNOMO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=118885145
version: 17
---

**Produto: RMLabore**

Processo: Cálculo de INSS Autônomos

IVersão: 11.5X ou superior

**INSS AUTÔNOMO** **/ DIRETOR**  
**(Contempla carreteiros e também restituição de INSS)**  
   
**1º Passo:**  
Acessar o menu Administração Pessoal | Cadastros | Fórmulas e efetuar o cadastro das seguintes fórmulas:  
   
**Código:** CHAPA  
**Descrição:** CHAPA  
**Texto:** CHAPA  
   
**Código:** MES  
**Descrição:** MES  
**Texto:** MES  
   
**Código:** ANO  
**Descrição:** ANO  
**Texto:** ANO  
   
**Código:** PERIODO  
**Descrição:** PERIODO  
**Texto:** PERIODO  
   
   
**2º Passo:**  
Acessar o menu  Administração Pessoal | Cadastros | Eventos e efetuar o cadastro dos seguintes eventos respeitando a configuração abaixo:  
   
**Código**: **XXXX**  
**Título:** BASE INSS AUTÔNOMOS/OUTRO EMPREGO  
**Configuração do evento:** Código de cálculo 0, tipo base de cálculo/Valor, com prioridade 0.

**Código:** **YYYY**   
**Título:** INSS AUTÔNOMOS/OUTRO EMPREGO  
**Configuração do evento:** Código de cálculo 0, tipo base de cálculo/Valor, com prioridade 1.  
   
**Código:** **JJJJ**   
**Título:** Restituição de INSS de autônomo  
**Configuração do evento:** Código de calculo 0, tipo base de cálculo/Valor, com prioridade 0.  
***Obs.:*** *O evento JJJJ deve ser informado quando no mês anterior o INSS do autônomo tenha sido descontado a maior, o sistema então irá deduzir este valor do calculo do INSS atual.*  
   
**Código:** **WWWW**  
**Título:** Honorários autônomos/diretores  
**Configuração do evento:** Código de calculo 46, Provento, tipo valor, prioridade 0.

**Código:** **QQQQ**  
**Título:** INSS 11% AUTÔNOMOS  
**Configuração do evento:** Código de cálculo 85, desconto, tipo Valor, com prioridade 80   
  
  
***Obs.:*** *Onde **WWWW, JJJJ, YYYY, QQQQ*** ***e*** ***XXXX*** *correspondem ao código a ser criado a critério do cliente**.***

   
**3º Passo: (Executar este passo apenas se a empresa trabalhar com transportadores autônomos – carreteiros)**

Acessar o menu Administração Pessoal | Cadastros | Eventos e efetuar o cadastro do evento respeitando a configuração abaixo:  
**Código**: **BBBB**  
**Título:** Valor do frete de transporte  
**Configuração do evento:** Código de cálculo 0, tipo Provento/Valor, com prioridade 0.  
   
 Acessar o módulo Administração Pessoal | Cadastros | Fórmulas e criar a fórmula abaixo:  
**Código:** **PPPP**  
**Título:** Base de INSS Transportador  
**Texto:** C('**BBBB**')\*0.20  
    
Acessar o menu Administração Pessoal | Cadastros | Eventos e efetuar o cadastro do evento respeitando a configuração abaixo:  
**Código**: **ZZZZ**  
**Título:** Base de INSS autônomo carreteiro  
**Configuração do evento:** Código de cálculo 46, tipo base de cálculo/Valor, com prioridade 10.  
**Fórmula valor: PPPP**  
   
***Obs.:*** *Onde BBBB,PPPP e ZZZZ correspondem ao código a ser criado a critério do cliente**.***  
   
   
   
**4º Passo:**  
Acessar o menu Gestão | Ferramentas de Análise | Visões de Dados e cadastrar as seguintes sentenças SQL:  
   
**Código:** INSSAA  
**Descrição:** INSS AUTONOMO  
**Texto:**   
SELECT SUM(VALOR) VALOR FROM PFFINANC  
WHERE CODEVENTO IN ( '**XXXX**', '**WWWW**',**'ZZZZ'**)   
AND CODCOLIGADA=CODCOLIGADA  
AND NROPERIODO<>:FRM\_PERIODO  
AND MESCOMP=:FRM\_MES  
AND ANOCOMP=:FRM\_ANO  
AND CHAPA=:FRM\_CHAPA  
   
**Código:** INSSVV  
**Descrição:** VALOR JÁ DESC. DE INSS  
**Texto:**  
SELECT SUM(VALOR) VALOR FROM PFFINANC  
WHERE CODEVENTO IN ('**QQQQ**', **'YYYY**') */\***Onde o evento YYYY*** ***e QQQQ(conforme passo 6)* *será o código utilizado para desc. do INSS autônomos outro emprego\*****/*  
AND CODCOLIGADA=CODCOLIGADA  
AND NROPERIODO<>:FRM\_PERIODO  
AND MESCOMP=:FRM\_MES  
AND ANOCOMP=:FRM\_ANO  
AND CHAPA=:FRM\_CHAPA  
   
**Código:** INSSRR  
**Descrição:** VALOR DE RESTITUIÇÃO JÁ INFORMADO EM PERÍODOS ANTERIORES  
**Texto:**  
SELECT SUM(VALOR) VALOR FROM PFFINANC  
WHERE CODEVENTO IN ('**JJJJ**') */\***Onde o evento JJJJ será o código utilizado para informar a Restitiução de INSS de autônomo\***/*  
AND CODCOLIGADA=CODCOLIGADA  
AND NROPERIODO<>:FRM\_PERIODO  
AND MESCOMP=:FRM\_MES  
AND ANOCOMP=:FRM\_ANO  
AND CHAPA=:FRM\_CHAPA  
   
***Substituindo os códigos MMMM, WWWW, YYYY, JJJJ, XXXX******,*** ***YYYY*** ***e ZZZZ pelos seus respectivos de acordo com o cadastro de fórmulas.***  
   
   
**5º Passo:**  
Acessar o menu Administração Pessoal | Cadastros | Fórmulas e cadastrar da seguinte fórmula:  
   
**Código:** INSSAA  
**Descrição:** INSS AUTÔNOMOS 11%  
**Texto:**  
DECL MAXIMO;  
SETVAR(MAXIMO, TABCALCULO ('LIMITESUPERIOR','***CCCC*** ',MTDATA (1, INCMES(MES,1), INCANO(MES,ANO,1)),***4***)\*0.11 ); */\***Onde o CCCC  é o código da tabela de cálculo de finalidade 5 (INSS\_REFORMA)\***/*  
SE PERIODO=1 ENTAO   
     MIN(MAXIMO,(C('XXXX')+ C('WWWW')+ C('ZZZZ'))\*.11) - C('YYYY')-C('JJJJ')  
SENAO SE PERIODO>1 ENTAO   
     EXECSQL('INSSAA'); EXECSQL('INSSVV'); EXECSQL('INSSRR');  
     MIN(MAXIMO,(RESULTSQL('INSSAA' , 'VALOR') +C('XXXX') + C('WWWW')+ C('ZZZZ'))\*.11) - RESULTSQL('INSSVV' , 'VALOR') - C('YYYY')   
     - RESULTSQL('INSSRR' , 'VALOR') - C('JJJJ')  
SENAO 0  
FIMSE FIMSE  
   
***Substituindo os códigos MMMM, WWWW, YYYY, JJJJ, XXXX, YYYY e ZZZZ  pelos seus respectivos de acordo com o cadastro de fórmulas.***  
  
  
**6º Passo:**  
Acessar o menu Administração Pessoal | Cadastros | Eventos e efetuar a alteração do evento abaixo associando a fórmula INSSAA criada no 5º Passo:  
   
**Código:** **QQQQ**  
**Título:** INSS 11% AUTÔNOMOS  
**Configuração do evento:** Código de cálculo 85, desconto, tipo Valor, com prioridade 80 e associar a fórmula INSSAA, no campo fórmula valor.  
  
***Obs.:*** *Onde **QQQQ** corresponde ao código a ser criado a critério do cliente**.***  
   
   
**7º Passo:**  
Lançar estes eventos junto ao evento de código de cálculo 46 (utilizado para pagamento dos autônomos)  
  
  
***O Autônomo deve estar cadastrado no sistema e no seu cadastro a opção "Caclula INSS" deve estar marcada.***  
***Não lance o evento WWWW para carreteiros.***   
   
   
     
**Exemplo de parametrização realizada para carreteiros.**

 **Criar fórmulas:**   
 

**1 -** **Código:** ANO  
 **Descrição:** ANO  
 **Fórmula:** ANO   
 

**2 -** **Código:** MES  
 **Descrição:** MES  
 **Fórmula:** MÊS   
 

**3 -** **Código:** MESCAIXA  
 **Descrição:** MÊS CAIXA  
 **Fórmula:** MESCX   
 

**4 -** **Código:** CHAPA  
 **Descrição:** CHAPA  
 **Fórmula:** CHAPA   
 

**5 -** **Código:** COLIGADA  
 **Descrição:** COLIGADA  
 **Fórmula:** COLIGADACORRENTE   
 

**6 -** **Código:** PERIODO  
 **Descrição:** PERIODO  
 **Fórmula:** PERIODO   
**Criar eventos:** 1 -  Código: 0251 Descrição: Pagamento de **Autônomo****Carreteiro** CC 0, provento, valor, sem incidência alguma. 2 -  Código: 0256 Descrição: **INSS** 11% **Autônomo**s Fórmula: **INSS**AUT CC 85, desconto, valor, sem incidência alguma. 3 -  Código: 3400 Descrição: IRRF **Autônomo**s Fórmula: IRRFAUT CC 84, desconto, valor, sem incidência alguma, prioridade 81.   
**OBS.:** Caso os eventos já existam com outro código, alterar o código correspondente no processo abaixo. O mesmo para casos onde já exista o código sugerido e há necessidade de criar outro código 

| SQL | Oracle |
| --- | --- |
| **1 -**  **Código:** IRRFAUT **Título:** IRRF Autônomos | **1 -**  **Código:** IRRFAUT **Título:** IRRF Autônomos |
| SELECT TAB1.VAL + TAB2.VAL RESULT FROM (SELECT ISNULL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**0251**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.NROPERIODO <>:FRM\_PERIODO AND PFPERFF.MESCOMP =:FRM\_MES /\***MES ATUAL\***/ ) TAB1, (SELECT ISNULL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**0251**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.MESCOMP <:FRM\_MES /\***MESES ANTERIORES\***/ ) TAB2 | SELECT TAB1.VAL + TAB2.VAL RESULT FROM (SELECT NVL (SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**0251**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.NROPERIODO <>:FRM\_PERIODO AND PFPERFF.MESCOMP =:FRM\_MES /\***MES ATUAL\***/ ) TAB1, (SELECT NVL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**0251**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.MESCOMP <:FRM\_MES /\***MESES ANTERIORES\***/ ) TAB2 |
| **2 -**  **Código:** IRRFAUT1 **Título:** IRRF Autônomos 1 | **2 -**  **Código:** IRRFAUT1 **Título:** IRRF Autônomos 1 |
| SELECT TAB1.VAL + TAB2.VAL RESULT FROM (SELECT ISNULL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**0256**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.NROPERIODO <>:FRM\_PERIODO AND PFPERFF.MESCOMP =:FRM\_MES /\***MES ATUAL\***/ ) TAB1, (SELECT ISNULL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**0256**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.MESCOMP <:FRM\_MES /\***MESES ANTERIORES\***/ ) TAB2 | SELECT TAB1.VAL + TAB2.VAL RESULT FROM (SELECT NVL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**0256**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.NROPERIODO <>:FRM\_PERIODO AND PFPERFF.MESCOMP =:FRM\_MES /\***MES ATUAL\***/ ) TAB1, (SELECT NVL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**0256**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.MESCOMP <:FRM\_MES /\***MESES ANTERIORES\***/ ) TAB2 |
| **3 -**  **Código:** IRRFDESC **Título:** IRRF Desconta do de Autônomos | **3 -**  **Código:** IRRFDESC **Título:** IRRF Desconta do de Autônomos |
| SELECT TAB1.VAL + TAB2.VAL RESULT FROM (SELECT ISNULL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**3400**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.NROPERIODO <>:FRM\_PERIODO AND PFPERFF.MESCOMP =:FRM\_MES /\***MES ATUAL\***/ ) TAB1, (SELECT ISNULL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**3400**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.MESCOMP <:FRM\_MES /\***MESES ANTERIORES\***/ ) TAB2 | SELECT TAB1.VAL + TAB2.VAL RESULT FROM (SELECT NVL(SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**3400**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.NROPERIODO <>:FRM\_PERIODO AND PFPERFF.MESCOMP =:FRM\_MES /\***MES ATUAL\***/ ) TAB1, (SELECT NVL (SUM(PFFINANC.VALOR),0) VAL FROM PFFINANC, PFPERFF WHERE  PFFINANC.CODEVENTO ='**3400**'AND PFPERFF.ANOCOMP=:FRM\_ANO AND PFPERFF.CHAPA=:FRM\_CHAPA AND PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA AND PFPERFF.CODCOLIGADA=:FRM\_Coligada AND PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA AND PFPERFF.CHAPA=PFFINANC.CHAPA and  PFPERFF.anocomp=PFFINANC.anocomp and  PFPERFF.mescomp=PFFINANC.mescomp and PFPERFF.nroperiodo=PFFINANC.nroperiodo  AND PFPERFF.MESCOMP <:FRM\_MES /\***MESES ANTERIORES\***/ ) TAB2 |

**Criar fórmula:**   
 **7 -**  **Código:** IRRFAUT  
 **Descrição:** IRRFAUT  
 **Fórmula:**   
 

EXECSQL ('IRRFDESC');  
 EXECSQL ('IRRFAUT1');  
 EXECSQL ('IRRFAUT') ;  
 SE TFUNC ='A' ENTAO TR ( ( (RESULTSQL ('IRRFAUT' , 'RESULT')+C(**'0251'**))\*0.40) - ((C(**'0256'**) + RESULTSQL ('IRRFAUT1' , 'RESULT'))))-RESULTSQL ('IRRFDESC' , 'RESULT') SENAO FALSO FIMSE   
  
 **8 -**  **Código:** INSSAUT  
 **Descrição:** INSS Autônomos  
 **Fórmula:**   
 

**T ('0003'**, (LI (**'0251'**))\*0.20) - (**T ('0003'**, (LI (**'0251'**) -C**('0251'**))\*0.20))   
  
 **9 -**  **Código:** 0096  
 **Descrição:** Base INSS Autônomos  
 

**Fórmula:** C(**'0251'**) \* 0.20

**10 -**  **Código:** 0097  
 **Descrição:** Base IRRF Autônomos  
 

**Fórmula:** C(**'0251'**) \* 0.40   
  
  
Deverá lançar os eventos 0251, 0256, 3400 no envelope e pedir recálculo.  
**OBS: O único que deverá ser informado o valor é o** **0251** **(Pagamento).**
