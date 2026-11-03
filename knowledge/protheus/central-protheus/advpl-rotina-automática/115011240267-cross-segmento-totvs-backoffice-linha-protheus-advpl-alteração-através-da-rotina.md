---
article_id: 115011240267
category: ADVPL - Rotina Automática
content_hash: 79a8cec8e2190f23a1dc9bc1e0fbe1e0a5bf1b4ea4d9132a1f6a384782122239
fetched_at: '2026-06-28T22:40:24.221457+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alteração através
  da rotina automática ATFA010
type: support-article
updated_at: '2021-12-29T12:56:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011240267-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Altera%C3%A7%C3%A3o-atrav%C3%A9s-da-rotina-autom%C3%A1tica-ATFA010
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Através da rotina automática ATFA010 como realizar a alteração?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Quando existir a necessidade de alterar um item especifico da Getdados, existem dois campos que podem ser utilizados, os campos são: LINPOS e AUTDELETA.  
O primeiro deve ser utilizado para localizar o item do aCols que sofrerá alteração, o segundo instruí a rotina automática para deletar a linha.  
Caso não seja utilizado o LINPOS esta função irá reconstruir todo o aCols.  
  
Exemplo

```
#Include 'Protheus.ch'  
#include "TbiConn.ch"  
User Function MyATFA010()//  
Local aItens := {}  
// Array com os dados a serem enviados pela MsExecAuto() para gravacao automatica dos itens do ativo  
Local aDadosAuto := {}  
// Array com os dados a serem enviados pela MsExecAuto() para gravacao automatica da capa do bem  
Local aCab := {}  
// Determina se as mensagens de help devem ser direcionadas para o arq. de log  
Private lMsHelpAuto := .f.  
// Determina se houve alguma inconsistencia na execucao da rotina  
Private lMsErroAuto := .f.  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"  
aCab := { {'N1_FILIAL' ,'01' ,NIL},;  
{'N1_CBASE' ,'0000000005' ,NIL},;  
{'N1_ITEM' ,'0001' ,NIL},;  
{'N1_QUANTD' , 10 ,NIL},;  
{'N1_AQUISIC' ,dDataBase ,NIL},;  
{'N1_DESCRIC' ,'TESTE COM A ROTINA AUTOMATICA ATFA010 01' ,NIL},;  
{'N1_CHAPA' ,'000005' ,NIL}}  
//array com os dados a serem enviados pela MsExecAuto() para gravacao automatica do item tipo 01  
aAdd(aItens,{ {'N3_TIPO' ,'01' ,NIL},;  
{'N3_HISTOR' ,"TESTE COM A ROTINA AUTOMATICA 0000000001" ,NIL},;  
{'N3_TPSALDO' ,'1' ,NIL},;  
{'N3_TPDEPR' ,'1' ,NIL},;  
{'N3_CCONTAB' ,'00000000000000000008' ,NIL},;  
{'N3_VORIG1' ,1000 ,NIL},;  
{'N3_VORIG2' ,0.39999 ,NIL},;  
{'N3_VORIG3' ,3000 ,NIL},;  
{'N3_VMXDEPR' ,0 ,NIL},;  
{'N3_VLSALV1' ,0 ,NIL},;  
{'N3_PERDEPR' ,0 ,NIL},;  
{'N3_PRODMES' ,0 ,NIL},;  
{'N3_PRODANO' ,0 ,NIL},;  
{'N3_DINDEPR' ,dDataBase ,NIL},;  
{"LINPOS","N3_TIPO" ,'01'},;  
{"AUTDELETA","N" ,Nil}})  
//array com os dados a serem enviados pela MsExecAuto() para gravacao automatica do item tipo 10  
aAdd(aItens,{ {'N3_TIPO' ,'10' ,NIL},;  
{'N3_HISTOR' ,"TESTE COM A ROTINA AUTOMATICA 0000000001" ,NIL},;  
{'N3_TPSALDO' ,'1' ,NIL},;  
{'N3_TPDEPR' ,'1' ,NIL},;  
{'N3_CCONTAB' ,'00000000000000000008' ,NIL},;  
{'N3_VORIG1' ,10000 ,NIL},;  
{'N3_VORIG2' ,0.39999 ,NIL},;  
{'N3_VORIG3' ,30000 ,NIL},;  
{'N3_VMXDEPR' ,0 ,NIL},;  
{'N3_VLSALV1' ,0 ,NIL},;  
{'N3_PERDEPR' ,0 ,NIL},;  
{'N3_PRODMES' ,0 ,NIL},;  
{'N3_PRODANO' ,0 ,NIL},;  
{'N3_DINDEPR' ,dDataBase ,NIL},;  
{"LINPOS","N3_TIPO" ,'10' },;  
{"AUTDELETA","N" ,Nil}})  
ConOut("Inicio")  
MSExecAuto( {|X,Y,Z| ATFA010(X,Y,Z)} ,aCab ,aItens, 4)  
If !lMsErroAuto  
ConOut(OemToAnsi("Incluido com sucesso! "))  
Else  
ConOut(OemToAnsi("Erro na inclusao!"))  
MostraErro()  
EndIf  
ConOut(OemToAnsi("Fim : ")+Time())  
RESET ENVIRONMENT  
Return
```

**Saiba mais**  
[ADV0029 Rotina automática ATFA010](http://tdn.totvs.com/pages/viewpage.action?pageId=286003717)

#
