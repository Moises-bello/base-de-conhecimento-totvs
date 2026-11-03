---
article_id: 115011785667
category: ADVPL - Ponto de Entrada
content_hash: 5827ac252ccc8388c6a736a850cc7ab74e8d9f62aca4b588c3fd4588df57d5d4
fetched_at: '2026-06-28T22:40:12.696613+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MTGRDVW
type: support-article
updated_at: '2022-06-21T17:51:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011785667-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MTGRDVW
---

**Dúvida**Não estou conseguindo incluir o registro no TBrowse da rotina, como proceder?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**

Segue exemplo de customização do ponto MTGRDVW

```
#include "protheus.ch"  
  
User Function MTGRDVW()  
Local ExpA1 := PARAMIXB[1]  
Local ExpO1 := PARAMIXB[2]  
Local ExpO2 := PARAMIXB[3]  
  
local aRet := {}  
local i  
  
for i := 1 to len(ExpO1:AHEADERS)  
  aAdd(aRet, ExpO1:AHEADERS[i])  
next i  
  
aAdd(aRet, "Teste")  
  
for i := 1 to len(ExpA1)  
  aAdd(ExpA1[i],"teste " + cValToChar(i))  
next i  
  
for i := 1 to len(aRet)  
  ExpO1:AddColumn(TCColumn():New(aRet[i],{||retCont(ExpO1,ExpA1)},,,,"LEFT",,.F.,.F.,,,,.F.,))  
next i  
  
Return  
  
static function retCont(ExpO1,ExpA1)  
  
if type("nCont") == "U"  
  public nCont := 0  
endIf  
  
if procname(1) == "{ ||RETCONT(EXPO1,EXPA1)}"  
  if nCont == len(ExpA1[ExpO1:NAT])  
     nCont := 1  
  else  
    nCont++  
  endIf  
endIf  
  
return ExpA1[ExpO1:NAT][iif(nCont = 0, 1,nCont)]
```

Com a tecla **F4** da rotina de cadastro de produto é possível visualizar o o exemplo.

![](https://tdn.totvs.com/download/attachments/286225360/image2017-8-22%2011%3A22%3A10.png?version=1&modificationDate=1503412017000&api=v2)

**Saiba mais**  
[ADV0033 Ponto de entrada MTGRDVW](http://tdn.totvs.com/display/PROT/ADV0033_PE_MTGRDVW)  
[MTGRDVW - Inclui campos na tela de Consulta ao estoque](https://tdn.totvs.com/display/public/PROT/MTGRDVW+-+Inclui+campos+na+tela+de+Consulta+ao+estoque)
