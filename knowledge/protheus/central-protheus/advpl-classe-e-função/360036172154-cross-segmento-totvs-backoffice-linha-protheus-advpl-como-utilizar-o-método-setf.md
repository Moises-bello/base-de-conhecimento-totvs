---
article_id: 360036172154
category: ADVPL - Classe e Função
content_hash: dfee324fa5a64b4206eb4eac3983b2499cb1fc70408d598fd8a50bc3e7295303
fetched_at: '2026-06-28T22:40:14.291478+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  Como utilizar o
  método SetFilter na classe TCBrowse
type: support-article
updated_at: '2021-12-28T20:26:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036172154-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-o-m%C3%A9todo-SetFilter-na-classe-TCBrowse
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como utilizar o método **SetFilter** na classe **TCBrowse**?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 11.8

**Solução**

```
#INCLUDE "TBICONN.CH"  
#INCLUDE 'Protheus.ch'  
  
User Function tstFBrowse()   
  
Private oDlg  
Private oBrowse   
Private aSize    := {}  
Private aObjects := {}  
Private aInfo    := {}  
Private aLargCol := {}   
Private bColor   
Private aCols    := Array(1,20)  
Private nAt      := 1  
Private cVar     :=""  
Private cCpofil  :=  "A1_FILIAL+A1_COD+A1_LOJA"  
Private cTopFun  := "FWXFILIAL('SA1')+'RS    '+'RS'"  
Private cBotFun  := cTopFun  
Private cCodNOME :="TESTE forn                              "  
  
oTFont1 := TFont():New('Courier new',,-08,.T.)  
aSize := MsAdvSize()  
  
AAdd( aObjects, { 100, 100, .T., .T. } )  
AAdd( aObjects, { 10,   10, .T., .T. } )  
  
aInfo := { aSize[ 1 ], aSize[ 2 ], aSize[ 3 ], aSize[ 4 ], 3, 3 }  
aPosObj := MsObjSize( aInfo, aObjects,.T.)  
  
DbSelectArea("SA1")  
dbGoTop()  
  
DEFINE DIALOG oDlg TITLE "Altera Grupos" FROM  aSize[7],0 To aSize[6],aSize[5] PIXEL //FONT oFont2  
  
// Cria Browse  
oBrowse := TCBrowse():New(aPosObj[1,1]+5,aPosObj[1,2],aPosObj[1,4],aPosObj[1,3],,,,;  
oDlg,,,,,,,oTFont1,,,,,.F.,"SA1",.T.,,.F.,,,)  
  
// Adiciona colunas  
oBrowse:AddColumn( TCColumn():New('Filial'      ,{ || A1_FILIAL },,,,"LEFT",25 ,.F.,.T.,,,,.F.,) )  
oBrowse:AddColumn( TCColumn():New('COD'         ,{ || A1_COD },,,,"LEFT",150,.F.,.T.,,,,.F.,) )  
oBrowse:AddColumn( TCColumn():New('Nome'        ,{ || A1_NOME },,,,"LEFT",150,.F.,.T.,,,,.F.,) )  
  
// Define o filtro  
oBrowse:SetFilter(cCpoFil, &cTopFun, &cBotFun)  
  
TButton():New( aPosObj[2,1]+15, aPosObj[2,2]+50, "Sair"  , oDlg, {|| oDlg:End()},40,010,,,.F.,.T.,.F.,,.F.,,,.F. )  
  
ACTIVATE DIALOG oDlg CENTERED    
Return          
```

**Saiba Mais**

[TCBrowse:SetFilter](https://tdn.totvs.com/display/tec/TCBrowse%3ASetFilter)
