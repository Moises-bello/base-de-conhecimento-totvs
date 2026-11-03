---
article_id: 360016495232
category: ADVPL - Rotina Automática
content_hash: 651aa9200db80781b5eb341e73d3a26fecbe14d76b36e6396feddca1c948bd2d
fetched_at: '2026-06-28T22:40:24.144720+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Modelo de uso da rotina
  automática para uso no arquivo fonte FINA110
type: support-article
updated_at: '2021-12-29T19:00:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016495232-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Modelo-de-uso-da-rotina-autom%C3%A1tica-para-uso-no-arquivo-fonte-FINA110
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Descrição do uso da rotina automática (**ExecAuto**) **FINA110** - Baixas a Receber - Automática  
  
**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

Deve ser passado um **array** (aTitulos), com oito posições, sendo que cada posição deverá conter a seguinte composição:

aTitulos [1]:= aRecnos   (array contendo os Recnos dos registros a serem baixados)

aTitulos [2]:= cBanco     (Banco da baixa)

aTitulos [3]:= cAgencia  (Agência da baixa)

aTitulos [4]:= cConta      (Conta da baixa)

aTitulos [5]:= cCheque   (Cheque da Baixa)

aTitulos [6]:= cLoteFin    (Lote Financeiro da baixa)

aTitulos [7]:= cNatureza (Natureza do movimento bancário)

aTitulos [8]:= dBaixa      (Data da baixa)

```
#INCLUDE  "protheus.ch"  
  
USER FUNCTION TSTF110Auto()  
  
LOCAL aTitulos  :=  Array(8)  
  
PRIVATE lMsErroAuto  :=  .F.  
  
aTitulos[1] :=  {4,5}  
  
aTitulos[2] :=  PAD("237",TAMSX3('A6_COD')[1])  
  
aTitulos[3] :=  PAD("200",TAMSX3('A6_AGENCIA')[1])  
  
aTitulos[4] :=  PAD("17085",TAMSX3('A6_NUMCON')[1])  
  
aTitulos[5] :=  PAD("20202",TAMSX3('EF_NUM')[1])  
  
aTitulos[6] :=  PAD("",TAMSX3('E1_LOTE')[1])  
  
aTitulos[7] :=  PAD("001",TAMSX3('ED_CODIGO')[1])  
  
aTitulos[8] := DATE()  
  
   
  
MSExecAuto({|x,y| Fina110(x,y)},3,aTitulos)  
  
   
  
IF lMsErroAuto  
  
    MostraErro()  
  
ENDIF  
  
RETURN nil
```

**Observações:**   
Caso a contabilização seja *online* e a tela de contabilização deva ser mostrada em caso de erro no lançamento (falta de conta, débito/crédito não batem, etc).

A baixa automática em lote não poderá ser utilizada. Somente será processada se:

**MV\_PRELAN    =** S

**MV\_CT105MS  =** N

**MV\_ALTLCTO   =** N
