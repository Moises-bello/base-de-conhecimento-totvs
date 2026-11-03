---
article_id: 360027593472
category: ADVPL - Rotina Automática
content_hash: a9427b15a6978af1ab287170018ec531d5a056d496a619544447713954d2bd15
fetched_at: '2026-06-28T22:40:24.236725+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Definir a revisão
  a ser alterada na rotina automática MATA200
type: support-article
updated_at: '2021-10-29T18:15:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027593472-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Definir-a-revis%C3%A3o-a-ser-alterada-na-rotina-autom%C3%A1tica-MATA200
---

**Dúvida**Estamos implementando a automatização de alguns processos e entre eles o de manutenção de estruturas utilizando a rotina automática MATA200. Verificamos na documentação do TDN e não localizamos forma de repassar para a rotina automática qual a revisão do produto está sendo alterada no momento da chamada da rotina. No exemplo que testamos, precisamos alterar a revisão 001 de um produto que atualmente está na revisão 002 (B1\_REVATU).  
Existe alguma variável que pode ser repassada para a rotina para esta implementação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões.   
  
**Solução**Quando o processo de alteração da estrutura é realizado por ExecAuto, a rotina define a revisão automaticamente de acordo com a revisão atual do produto(**B1\_REVATU**), porém a variável **cRevisao,**que guarda a revisão a qual irá processar, possui escopo Private e, portanto, é possível altera-la em qualquer momento, através de um ponto de entrada, após ela ter sido definida.   
No exemplo de ExecAuto a seguir, estou alterando a estrutura do produto PA-001, e a revisão atual deste produto é a '002'. O componente MP-003 está somente na revisão '001', então para que a alteração deste componente ocorra na revisão '001', defino o escopo da revisão, informando os campos **G1\_REVINI** e **G1\_REVFIM,**e utilizo o ponto de entrada [MTA200](http://tdn.totvs.com/display/public/PROT/MTA200+-+Estrutura+dos+produtos) para definir qual será a revisão do processo:

```
#Include 'Protheus.ch'  
#Include 'TBICONN.ch'  
  
User Function altMT200()  
Local aCab := {}  
Local aGets := {}  
Local aItens := {}  
PRIVATE lMsErroAuto := .F.  
  
PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01'  
  
aCab := {{"G1_COD","PA-001 ",NIL},;   
 {"G1_QUANT",1,NIL},;   
 {"NIVALT","S",NIL},;  
 {"ATUREVSB1","N",NIL}}   
   
aadd(aGets,{"G1_COD","PA-001 ",NIL})   
aadd(aGets,{"G1_COMP","MP-001 ",NIL})   
aadd(aGets,{"G1_TRT",Space(3),NIL})   
aadd(aGets,{"G1_QUANT",1,NIL})   
aadd(aGets,{"G1_PERDA",0,NIL})   
aadd(aGets,{"G1_INI",dDataBase,NIL})   
aadd(aGets,{"G1_FIM",CTOD("31/12/49"),NIL})  
aadd(aGets,{"G1_REVINI",'001',NIL})   
aadd(aGets,{"G1_REVFIM",'002',NIL})  
aadd(aItens,aGets)   
   
aGets := {}   
aadd(aGets,{"G1_COD","PA-001 ",NIL})   
aadd(aGets,{"G1_COMP","MP-003 ",NIL})   
aadd(aGets,{"G1_TRT",Space(3),NIL})   
aadd(aGets,{"G1_QUANT",5,NIL})   
aadd(aGets,{"G1_PERDA",0,NIL})   
aadd(aGets,{"G1_INI",dDataBase,NIL})   
aadd(aGets,{"G1_FIM",CTOD("31/12/49"),NIL})   
aadd(aGets,{"G1_REVINI",'001',NIL})   
aadd(aGets,{"G1_REVFIM",'001',NIL})  
aadd(aItens,aGets)   
   
ConOut("Teste de Alteração")   
ConOut("Inicio: "+Time())   
   
MSExecAuto({|x,y,z| mata200(x,y,z)},aCab,aItens,4)   
   
If lMsErroAuto  
 MostraErro()  
Else  
 ConOut("Alterado com sucesso: "+Time())  
EndIf   
   
ConOut("Fim: "+Time())  
  
RESET ENVIRONMENT  
  
Return
```

```
#Include 'Protheus.ch'  
  
User Function MTA200()  
Local cOpc := PARAMIXB  
Local lRet := .T.  
  
cRevisao := '001'  
  
Return lRet
```
