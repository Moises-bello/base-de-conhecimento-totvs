---
article_id: 360016513352
category: ADVPL - Rotina Automática
content_hash: 224ad0a59865145d94ce086f2229a518dce7c4acc551344b1738ee7bf86785da
fetched_at: '2026-06-28T22:40:24.231684+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como realizar um
  apontamento de  produção a Maior via ExecAuto MATA250
type: support-article
updated_at: '2021-12-29T12:58:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016513352-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-realizar-um-apontamento-de-produ%C3%A7%C3%A3o-a-Maior-via-ExecAuto-MATA250
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como realizar um apontamento de Produção via rotina automática, onde a quantidade é maior que a ordem de produção?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL -  A partir da versão 11.80  
  
**Solução**Para que possa realizar o apontamento de produção, onde a produção é maior que a ordem, você precisa informar a quantidade a maior no *array*(D3\_QTMAIOR)

Exemplo de Fonte, onde a ordem de produção é 15 e foi produzido 20, precisamos informar que 5 foi a quantidade a maior da produção.

```
#Include 'Protheus.ch'  
#include "tbiconn.ch"  
  
User Function MATA250()  
  
Local aVetor  
  
Local dData  
  
Local nOpc := 3 //-Opção de execução da rotina,  
  
Local cOp := "OP021201001 "  
  
Local cCod := "000000000000001"  
  
Local cLocal:= "01"  
  
Local cChave:= ""  
  
prepare environment empresa "99" filial "01" modulo "est"  
  
lMsErroAuto := .F.  
  
aVetor := {}  
  
dData:=dDataBase  
  
aVetor := { {"D3_OP" ,"OP021201001 " ,NIL},;  
 {"D3_COD" ,"000000000000001" ,NIL},;  
 {"D3_QUANT" ,20 ,NIL},; // {"D3_PARCTOT" , "P" ,NIL},;  
 {"D3_TM" ,"010" ,NIL},;  
 {"D3_QTMAIOR" , 5 ,NIL}}  
   
MSExecAuto({|x, y| mata250(x, y)},aVetor, nOpc )  
  
If lMsErroAuto  
 CONOUT("Erro")  
 mostraerro()  
Else  
 //CONOUT("Incluido com sucesso")  
 CONOUT("Incluido com sucesso")  
Endif  
  
return nil
```

**Saiba mais  
[Documentação ExecAuto Mata250](http://tdn.totvs.com/pages/viewpage.action?pageId=6087461)**
