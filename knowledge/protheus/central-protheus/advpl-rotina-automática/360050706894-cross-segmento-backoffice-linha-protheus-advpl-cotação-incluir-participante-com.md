---
article_id: 360050706894
category: ADVPL - Rotina Automática
content_hash: 3d5739063fa4838bbf76d2da12361cc7f54bb09be0ed0ea7a1459d8cc029a3ae
fetched_at: '2026-06-28T22:40:23.956839+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - Cotação: Incluir Participante
  com ExecAuto() MATA150'
type: support-article
updated_at: '2021-12-29T13:53:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050706894-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Cota%C3%A7%C3%A3o-Incluir-Participante-com-ExecAuto-MATA150
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Qual o exemplo de ExecAuto() para incluir um participante em uma cotação?

**Ambiente**Protheus – ADVPL – A partir da versão p12  
  
**Solução**Segue Exemplo.

```
#INCLUDE "RWMAKE.CH"  
#INCLUDE "TBICONN.CH"  
  
// MATA150 INCLUSÃO DE UM NOVO PARTICIPANTE  
  
User Function PartMat150()  
Local aCabec := {}  
Local aItens := {}  
PRIVATE lMsErroAuto := .F.  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "COM"  
  
    //| Posiciona a cotação em que o novo participante será incluído. |//  
  
    dbSelectArea("SC8")  
    dbSetOrder(1)  
    dbSeek(xFilial("SC8")+"000053")  
  
    aadd(aCabec,{"C8_FORNECE"   , "000001"})  
    aadd(aCabec,{"C8_LOJA"      , "02"})  
    aadd(aCabec,{"C8_COND"      , "001"})  
    aadd(aCabec,{"C8_CONTATO"   , "Alt-Exec"})  
    aadd(aCabec,{"C8_FILENT"    , "01"})  
    aadd(aCabec,{"C8_MOEDA"     , 1})  
    aadd(aCabec,{"C8_EMISSAO"   , dDataBase})  
    aadd(aCabec,{"C8_TOTFRE"    , 0})  
    aadd(aCabec,{"C8_VALDESC"   , 0})  
    aadd(aCabec,{"C8_DESPESA"   , 0})  
    aadd(aCabec,{"C8_SEGURO"    , 0})  
    aadd(aCabec,{"C8_DESC1"     , 0})  
    aadd(aCabec,{"C8_DESC2"     , 0})  
    aadd(aCabec,{"C8_DESC3"     , 0})  
  
    aadd(aItens,{{"C8_NUMPRO"   ,"01"                               ,Nil},;  
                 {"C8_PRODUTO"  ,"COTACAO                       "   ,Nil},;  
                 {"C8_ITEM"     ,"0001"                             ,Nil},;  
                 {"C8_UM"       ,"UN"                               ,Nil},;  
                 {"C8_QUANT"    ,10                                 ,Nil},;  
                 {"C8_PRECO"    ,0                                  ,NIL},;  
                 {"C8_TOTAL"    ,0                                  ,NIL}})  
  
    MSExecAuto({|v,x,y| MATA150(v,x,y)},aCabec,aItens,2)  
  
    If !lMsErroAuto  
            ConOut(" Novo participante incluído" )  
    Else            
            ConOut("Erro na inclusão!")  
    EndIf  
    ConOut("Fim: " + Time())  
  
RESET ENVIRONMENT  
Return
```

**Saiba mais**  
[MATA150 - Atualiza Cotação (Rotina Automática - EXECAUTO)](https://tdn.totvs.com/pages/releaseview.action?pageId=545250210)
