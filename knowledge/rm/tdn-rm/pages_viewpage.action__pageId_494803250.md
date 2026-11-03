---
content_hash: 04e0fcac5f1d31f6c0672f7747d9b91b06f1f9c91a2b32122174bb7c05bfafc7
fetched_at: '2026-06-29T00:10:21.882840+00:00'
page_id: '494803250'
product: rm
source: tdn-rm
title: COMO FAZER - INSS // IRRF AUTÔNOMO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494803250
version: 18
---

**Produto: RMLabore**

Processo: Cálculo de  INSS // IRRF Autônomos

Os exemplos de fórmulas citados abaixo foram criados baseado em um modelo de cálculo específico. Cada empresa deverá avaliar a sua necessidade de cálculo e adaptar as fórmulas, caso seja necessário.

* Exemplos de tributação da categoria autônomo:  
  a) taxistas - base 20% para INSS, e 60% para IRRF;  
  b) transporte carga – base 20% para INSS, e 40% para IRRF;  
  c) demais – base total 11%

11Cálculo INSSCálculo INSS

**INSS AUTÔNOMO** **/ DIRETOR**  
**(Contempla carreteiros e também restituição de INSS)**  
   
**1º Passo:**

**Observação:** Verifique a necessidade do cadastro das formulas abaixo, caso já possua elas no cadastro seguir para o passo 2.

Acessar o menu "Cadastros -> Fórmulas" e efetuar o cadastro das seguintes fórmulas:  
   
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
Acessar o menu "Cadastros -> Eventos" e efetuar o cadastro dos seguintes eventos respeitando a configuração abaixo:  
   
**Código**: **MMMM**  
**Título:** BASE INSS AUTÔNOMOS/OUTRO EMPREGO  
**Configuração do evento:** Código de cálculo 0, tipo base de cálculo/Valor, com prioridade 0.  
   
**Código:** **RRRR**   
**Título:** INSS AUTÔNOMOS/OUTRO EMPREGO  
**Configuração do evento:** Código de cálculo 0, base de cálculo, tipo Valor, com prioridade 1.  
   
**Código:** **JJJJ**   
**Título:** Restituição de INSS de autônomo  
**Configuração do evento:** Código de calculo 0, Base de calculo, tipo valor, Prioridade 0.  
***Obs.:*** *O evento JJJJ deve ser informado quando no mês anterior o INSS do autônomo tenha sido descontado a maior, o sistema então irá deduzir este valor do calculo do INSS atual.*  
   
**Código:** **HHHH**  
**Título:** Honorários autônomos/diretores  
**Configuração do evento:** Código de calculo 46, Provento, tipo valor, prioridade 0.  
  
  
***Obs.:*** *Onde **HHHH, JJJJ, RRRR*** ***e*** ***MMMM*** *correspondem ao código a ser criado a critério do cliente**.***  
   
**3º Passo: (Executar este passo apenas se a empresa trabalhar com transportadores autônomos – carreteiros)**  
Acessar o menu "Cadastros -> Eventos" e efetuar o cadastro do evento respeitando a configuração abaixo:  
**Código**: **BBBB**  
**Título:** Valor do frete de transporte  
**Configuração do evento:** Código de cálculo 0, tipo Provento/Valor, com prioridade 0.  
   
   
Acessar o módulo "Cadastro | fórmulas" e criar a fórmula abaixo:  
**Código:** **PPPP**  
**Título:** Base de INSS Transportador  
**Texto:** C('**BBBB**')\*0.20  
   
   
Acessar o menu "Cadastros -> Eventos" e efetuar o cadastro do evento respeitando a configuração abaixo:  
**Código**: **ZZZZ**  
**Título:** Base de INSS autônomo carreteiro  
**Configuração do evento:** Código de cálculo 46, tipo base de cálculo/Valor, com prioridade 10.  
**Fórmula valor: PPPP**  
   
***Obs.:*** *Onde BBBB,PPPP e ZZZZ correspondem ao código a ser criado a critério do cliente**.***  
   
   
   
**4º Passo:**  
Acessar o menu "Utilitários -> Consultas SQL" e cadastrar as seguintes sentenças SQL:  
   
**Código:** INSSAA  
**Descrição:** INSS AUTONOMO  
**Texto:**   
SELECT SUM(VALOR) VALOR FROM PFFINANC  
WHERE CODEVENTO IN ( '**MMMM**', '**HHHH**',**'ZZZZ'**)   
AND CODCOLIGADA=CODCOLIGADA  
AND NROPERIODO<>:FRM\_PERIODO  
AND MESCOMP=:FRM\_MES  
AND ANOCOMP=:FRM\_ANO  
AND CHAPA=:FRM\_CHAPA  
   
**Código:** INSSVV  
**Descrição:** VALOR JÁ DESC. DE INSS  
**Texto:**  
SELECT SUM(VALOR) VALOR FROM PFFINANC  
WHERE CODEVENTO IN ('**XXXX**', **'RRRR**') */\***Onde o evento RRRR*** ***e XXXX**será* *o código utilizado para desc. do INSS autônomos outro emprego\*****/*  
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
   
***Substituindo os códigos HHHH, RRRR, JJJJ, MMMM e ZZZZ pelos seus respectivos de acordo com o cadastro de fórmulas.***  
   
   
**5º Passo:**  
Acessar o menu "Cadastros -> Fórmulas" e cadastrar da seguinte fórmula:  
   
**Código:** INSSAA  
**Descrição:** INSS AUTÔNOMOS 11%  
**Texto:**  
DECL MAXIMO;  
SETVAR(MAXIMO, TABCALCULO ('LIMITESUPERIOR','INSS',MTDATA (1, INCMES(MES,1), INCANO(MES,ANO,1)),3)\*0.11 );  
SE PERIODO=1 ENTAO   
     MIN(MAXIMO,(C('MMMM')+ C('HHHH')+ C('ZZZZ'))\*.11) - C('RRRR')-C('JJJJ')  
SENAO SE PERIODO>1 ENTAO   
     EXECSQL('INSSAA'); EXECSQL('INSSVV'); EXECSQL('INSSRR');  
     MIN(MAXIMO,(RESULTSQL('INSSAA' , 'VALOR') +C ('MMMM') + C('HHHH')+ C('ZZZZ'))\*.11) - RESULTSQL('INSSVV' , 'VALOR') - C('RRRR')   
     - RESULTSQL('INSSRR' , 'VALOR') - C('JJJJ')  
SENAO 0  
FIMSE FIMSE  
   
***Substituindo os códigos  HHHH, RRRR, JJJJ, MMMM e ZZZZ  pelos seus respectivos de acordo com o cadastro de fórmulas.***  
  
  
**6º Passo:**  
Acessar o menu "Cadastros -> Eventos" e efetuar o cadastro dos seguintes eventos respeitando a configuração abaixo:  
   
**Código:** XXXX  
**Título:** INSS 11% AUTÔNOMOS  
**Configuração do evento:** Código de cálculo 85, desconto, tipo Valor, com prioridade 85 e associar a fórmula INSSAA, no campo fórmula valor.  
  
***Obs.:*** *Onde XXXX corresponde ao código a ser criado a critério do cliente**.***  
   
   
**7º Passo:**  
Lançar estes eventos junto ao evento de código de cálculo 46 (utilizado para pagamento dos autônomos)  
  
  
***O Autônomo deve estar cadastrado no sistema e no seu cadastro a opção "Caclula INSS" deve estar marcada.***  
***Não lance o evento HHHH para carreteiros.***   
 

2Cálculo IRRFCálculo IRRF

**Passo 1:**

**Observação:** Verifique a necessidade do cadastro das formulas abaixo, caso já possua elas no cadastro seguir para o passo 2.

**Criar fórmulas:** 

**1 -** **Código:** ANO  
**Descrição:** ANO  
**Fórmula:** ANO 

**2 -** **Código:** MES  
**Descrição:** MES  
**Fórmula:** MES

**3 -** **Código:** MESCAIXA  
**Descrição:** MÊS CAIXA  
**Fórmula:** MESCX 

**4 -** **Código:** CHAPA  
**Descrição:** CHAPA  
**Fórmula:** CHAPA 

**5 -** **Código:** COLIGADA  
**Descrição:** COLIGADA  
**Fórmula:** COLIGADACORRENTE 

**6 -** **Código:** PERIODO  
**Descrição:** PERIODO  
**Fórmula:** PERIODO

**7-** **Código:** PESSOA  
**Descrição:** PESSOA  
**Texto:** **TABFUNC**('CODPESSOA','S')

**Passo 2:**

**Criar eventos:**

1 -  Código: 0046 Descrição: PAGAMENTO DE AUTÔNOMOS CC 46, provento, valor, sem incidências.

2 -  Código: XXXX Descrição: INSS AUTÔNOMOS CC 85, desconto, valor, sem incidências. Observação: exemplo de cadastro deste evento em aba **Cálculo INSS**.

3 -  Código: YYYY Descrição: IRRF AUTÔNOMOS Fórmula: IRRFAUT CC 84, desconto, valor, sem incidências, prioridade 99.

4 - Código: WWWW Descrição: BASE TRIBUTADA DE INSS AUTÔNOMO MÚLTIPLOS VÍNCULOS,CC 417 base de calculo, valor, sem incidências, prioridade 81.

**OBS.:** Caso os eventos já existam com outro código, alterar o código correspondente no processo abaixo. O mesmo para casos onde já exista o código sugerido e há necessidade de criar outro código.

**Passo 3:**

Acessar o menu "Utilitários -> Consultas SQL" e cadastrar as seguintes sentenças SQL

|  |  |
| --- | --- |
| **SQL** | **Oracle** |
| **SQL** | **Oracle** |
| **1 -**  **Código:** IRRFAUT **Título:** Base Autônomos | **1 -**  **Código:** IRRFAUT **Título:** Base Autônomos |
| **SELECT** TAB1.VAL + TAB2.VAL RESULT  **FROM**  (**SELECT** ISNULL (**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO **IN** ('0046')**AND /*\*Onde o evento 0046****será**o código utilizado para pagamento do autônomos \*****/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP=PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP=PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO=PFFINANC.NROPERIODO **AND** PFPERFF.MESCOMP =:FRM\_MES /\*MES ATUAL\*/ ) TAB1,  (**SELECT** ISNULL(**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO **IN** ('0046') **AND**  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO=PFFINANC.NROPERIODO **AND** PFPERFF.MESCOMP <:FRM\_MES /\*MESES ANTERIORES\*/ ) TAB2 | **SELECT** TAB1.VAL + TAB2.VAL RESULT  **FROM**  (**SELECT** **NVL** (**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA  **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO **IN** ('0046') **AND /*\*Onde o evento 0046**será**o código utilizado para pagamento do autônomos \***/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO=PFFINANC.NROPERIODO **AND** PFPERFF.MESCOMP =:FRM\_MES /\*MES ATUAL\*/ ) TAB1,  (**SELECT** **NVL**(**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO **IN** ('0046') **AND**  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.V=PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO=PFFINANC.NROPERIODO **AND** PFPERFF.MESCOMP <:FRM\_MES /\*MESES ANTERIORES\*/ ) TAB2 |
| **2 -**  **Código:** IRRFAUT1 **Título:** Desconto de INSS Autônomos | **2 -**  **Código:** IRRFAUT1 **Título:** Desconto de INSS Autônomos |
| **SELECT** TAB1.VAL + TAB2.VAL RESULT  **FROM**  (**SELECT** ISNULL (**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CODPESSOA <>:FRM\_CHAPA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO **IN** ('XXXX') **AND */\*Onde o evento XXXX**será* *o código utilizado para desc. do INSS autônomos\***/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO =PFFINANC.NROPERIODO **AND**  PFPERFF.MESCOMP =:FRM\_MES /\*MES ATUAL\*/ ) TAB1,  (**SELECT** ISNULL (**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO **IN** ('XXXX') **AND */\*Onde o evento XXXX**será* *o código utilizado para desc. do INSS autônomos\***/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO =PFFINANC.NROPERIODO **AND**  PFPERFF.MESCOMP <:FRM\_MES /\*MESES ANTERIORES\*/ ) TAB2 | **SELECT** TAB1.VAL + TAB2.VAL RESULT  **FROM**  (**SELECT** **NVL**(**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CODPESSOA <>:FRM\_CHAPA**AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO **IN** ('XXXX') **AND */\*Onde o evento XXXX**será* *o código utilizado para desc. do INSS autônomos\***/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO =PFFINANC.NROPERIODO **AND**  PFPERFF.MESCOMP =:FRM\_MES /\*MES ATUAL\*/ ) TAB1,  (**SELECT** **NVL**(**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO **IN** ('XXXX') **AND */\*Onde o evento XXXX**será* *o código utilizado para desc. do INSS autônomos\***/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO =PFFINANC.NROPERIODO **AND**  PFPERFF.MESCOMP <:FRM\_MES /\*MESES ANTERIORES\*/ ) TAB2 |
| **3 -**  **Código:** IRRFDESC **Título:** IRRF Desconto de Autônomos | **3 -**  **Código:** IRRFDESC **Título:** IRRF Desconto de Autônomos |
| **SELECT** TAB1.VAL + TAB2.VAL RESULT  **FROM**  (**SELECT** ISNULL (**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CHAPA <> :FRM\_CHAPA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO IN ('YYYY')  **AND */\*Onde o evento YYYY* *será* *o código utilizado para desc. do IRRF autônomos \***/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO =PFFINANC.NROPERIODO **AND**  PFPERFF.MESCOMP =:FRM\_MES /\*MES ATUAL\*/ ) TAB1,  (**SELECT** ISNULL (**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CHAPA <> :FRM\_CHAPA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFFINANC.CODEVENTO IN ('YYYY') **AND */\*Onde o evento YYYY* *será* *o código utilizado para desc. do IRRF autônomos \***/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO =PFFINANC.NROPERIODO **AND**  PFPERFF.MESCOMP <:FRM\_MES /\*MESES ANTERIORES\*/ ) TAB2 | **SELECT** TAB1.VAL + TAB2.VAL RESULT  **FROM**  (**SELECT** **NVL**(**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CHAPA <> :FRM\_CHAPA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFUNC.CHAPA = PFFINANC.CHAPA **AND**  PFFINANC.CODEVENTO IN ('YYYY') **AND */\*Onde o evento YYYY* *será* *o código utilizado para desc. do IRRF autônomos \***/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO =PFFINANC.NROPERIODO **AND**  PFPERFF.MESCOMP =:FRM\_MES /\*MES ATUAL\*/ ) TAB1,  (**SELECT** **NVL** (**SUM**(PFFINANC.VALOR),0) VAL  **FROM** PFUNC, PFFINANC, PFPERFF  **WHERE**  PFUNC.CODCOLIGADA =:FRM\_COLIGADA **AND**  PFUNC.CODPESSOA =:FRM\_PESSOA **AND**  PFUNC.CHAPA <> :FRM\_CHAPA **AND**  PFUNC.CODCOLIGADA = PFFINANC.CODCOLIGADA **AND**  PFFINANC.CODEVENTO IN ('YYYY')  **AND */\*Onde o evento YYYY* *será* *o código utilizado para desc. do IRRF autônomos \***/***  PFPERFF.ANOCOMP=:FRM\_ANO **AND**  PFPERFF.MESCAIXACOMUM=:FRM\_MESCAIXA **AND**  PFPERFF.CODCOLIGADA=:FRM\_COLIGADA **AND**  PFPERFF.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND**  PFPERFF.CHAPA=PFFINANC.CHAPA **AND**  PFPERFF.ANOCOMP =PFFINANC.ANOCOMP **AND**  PFPERFF.MESCOMP =PFFINANC.MESCOMP **AND**  PFPERFF.NROPERIODO =PFFINANC.NROPERIODO **AND**  PFPERFF.MESCOMP <:FRM\_MES /\*MESES ANTERIORES\*/ ) TAB2 |

**Passo 4:**

Criar as formulas

**1 -**  **Código:** IRRFAUT  
**Descrição:** IRRFAUT  
**Fórmula:**

EXECSQL ('IRRFDESC');

EXECSQL ('IRRFAUT1');

EXECSQL ('IRRFAUT');

SE TFUNC ='A' ENTAO (TR ((((RESULTSQL ('IRRFAUT' , 'RESULT')))\*0.40) - (( RESULTSQL ('IRRFAUT1' , 'RESULT')+ FOR('INSSAA' /\* Acrescentar aqui a formula do calculo do INSS, código de calculo 85\*/))))- RESULTSQL ('IRRFDESC' , 'RESULT')) SENAO FALSO FIMSE

o exemplo acima trata um calculo de IRRF com a base no autônomo com tributação para transporte de carga, base para o calculo de 40% , caso possua mais de uma tributação será necessário a criação de outra formula e outro evento para associação ao funcionário.

**Passo 5:**  
 Deverá lançar os eventos 0046, XXXX, YYYY no envelope e pedir recálculo.  
**OBS: O único que deverá ser informado o valor é o** **0046****(Pagamento).**

**Exemplo:** Funcionário b) transporte carga – base 20% para INSS, e 40% para IRRF; com múltiplos vínculos, na primeira chapa foram lançados os seguintes eventos:

* 0046 - PAGAMENTO DE AUTÔNOMOS no valor de R$ 7.000,00
* XXXX - INSS AUTÔNOMOS sem valor e
* YYYY - IRRF AUTÔNOMOS sem valor

Feito o calculo e o recalculo. Sistema realizou corretamente o cálculo de IRRF.

Na segunda chapa foram lançados os eventos:

* 0046 - PAGAMENTO DE AUTÔNOMOS no valor de R$ 8.000,00
* XXXX - INSS AUTÔNOMOS sem valor e
* YYYY - IRRF AUTÔNOMOS sem valor.

Feito o calculo e o recálculo. Sistema considerou os descontos e base da outra chapa e realizou o cálculo de IRRF corretamente.
