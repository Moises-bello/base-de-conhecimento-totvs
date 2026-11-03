---
article_id: 11096432428951
category: ADVPL - Classe e Função
content_hash: 3991580b7f6e9bdd1a996708f4bf820fb57d7abc74e660d11ca6273deecde0b6
fetched_at: '2026-06-28T22:40:15.808806+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - erro fwmsprinter:applydefinitions
  ao cancelar impressão FWMSPRINTER
type: support-article
updated_at: '2022-12-20T17:11:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11096432428951-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-erro-fwmsprinter-applydefinitions-ao-cancelar-impress%C3%A3o-FWMSPRINTER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como cancelar a impressão da fwmsprinter sem gerar erro variable is not an object on FWMSPRINTER:APPLYDEFINITIONS(FWMSPRINTER.PRW)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 12  
  
**Solução**

A FWMsPrinter possui a propriedade método ***nModalResult*** esta indica quando é confirmado ou cancelada a ação na *Dialog* de impressão.

**Exemplo:**

```
#INCLUDE "TOTVS.CH"  
#INCLUDE "APWIZARD.CH"  
#INCLUDE "FILEIO.CH"  
#INCLUDE "TBICONN.CH"  
#INCLUDE "COLORS.CH"  
#INCLUDE "RPTDEF.CH"  
#INCLUDE "FWPrintSetup.ch"  
  
User Function MyCodtst()  
  
Local lAdjustToLegacy := .F.  
Local lDisableSetup := .F. //Se .F. irá apresentar a tela, .T.ou não  
Local cLocal := "\spool"  
Local oPrinter  
  
RpcSetEnv('99','01','Administrador','')  
  
oPrinter := FWMSPrinter():New("exemplo.rel", IMP_PDF, lAdjustToLegacy,cLocal, lDisableSetup, , , , , , .F., )  
  
IF !lDisableSetup //se possuir tela valida o botão caso não tenha não irá validar  
if oPrinter:nModalResult == PD_OK  
oPrinter:Say( 20, 30, "Código de barras EAN13:")  
  
oPrinter:Ean13(180/*nRow*/ ,280/*nCol*/,"876543210987"/*cCode*/,100/*nWidth*/,95/*nHeigth*/)  
oPrinter:Ean13(230/*nRow*/ ,450/*nCol*/,"987654321098"/*cCode*/,100/*nWidth*/,45/*nHeigth*/)  
oPrinter:Ean13(150/*nRow*/ ,30 /*nCol*/,"098765432109"/*cCode*/,186/*nWidth*/,95/*nHeigth*/)  
oPrinter:Ean13(300/*nRow*/ ,30 /*nCol*/,"123456789012"/*cCode*/,200/*nWidth*/,95/*nHeigth*/)  
oPrinter:Ean13(300/*nRow*/ ,300/*nCol*/,"900223631103"/*cCode*/,250/*nWidth*/,95/*nHeigth*/)  
  
oPrinter:Preview()  
EndIf  
Else  
  
oPrinter:Say( 20, 30, "Código de barras EAN13:")  
  
oPrinter:Ean13(180/*nRow*/ ,280/*nCol*/,"876543210987"/*cCode*/,100/*nWidth*/,95/*nHeigth*/)  
oPrinter:Ean13(230/*nRow*/ ,450/*nCol*/,"987654321098"/*cCode*/,100/*nWidth*/,45/*nHeigth*/)  
oPrinter:Ean13(150/*nRow*/ ,30 /*nCol*/,"098765432109"/*cCode*/,186/*nWidth*/,95/*nHeigth*/)  
oPrinter:Ean13(300/*nRow*/ ,30 /*nCol*/,"123456789012"/*cCode*/,200/*nWidth*/,95/*nHeigth*/)  
oPrinter:Ean13(300/*nRow*/ ,300/*nCol*/,"900223631103"/*cCode*/,250/*nWidth*/,95/*nHeigth*/)  
  
oPrinter:Preview()  
EndIf  
  
Return
```

**Saiba Mais:****[FWMsPrinter](https://tdn.totvs.com/display/public/framework/FWMsPrinter)**
