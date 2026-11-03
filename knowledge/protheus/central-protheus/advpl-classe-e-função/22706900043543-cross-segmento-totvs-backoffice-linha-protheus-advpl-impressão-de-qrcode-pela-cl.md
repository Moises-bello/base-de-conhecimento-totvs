---
article_id: 22706900043543
category: ADVPL - Classe e Função
content_hash: fbb8715dccfe3c81b0037581d689bbd3c9b987dd3eac39632a4028683ad836c0
fetched_at: '2026-06-28T22:40:20.751875+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Impressão de QRcode
  pela classe TReport
type: support-article
updated_at: '2024-04-10T16:46:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22706900043543-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impress%C3%A3o-de-QRcode-pela-classe-TReport
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22706868088343) Tempo aproximado para leitura: **00:01:00 min****Dúvida**É possível imprimir o QRcode pela classe TReport?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

A classe [TReport](https://tdn.totvs.com/display/public/framework/TReport) não possui método para impressão de QrCode. Entretanto, existe a classe [FwQrCode](https://tdn.totvs.com/display/public/framework/FwQrCode), nela é gravado como imagem na pasta TEMP do Próprio Windows.

Dessa maneira pode ser gerado o QrCode pela classe [FwQrCode](https://tdn.totvs.com/display/public/framework/FwQrCode) e após pela classe [TReport](https://tdn.totvs.com/display/public/framework/TReport) utilizar o método SayBitmap para impressão da imagem.

**Exemplo:**

```
#Include "PROTHEUS.CH"  
#Include "RPTDEF.CH"  
#INCLUDE "TBICONN.CH"  
#INCLUDE "FWPrintSetup.ch"  
  
//Consulte: http://tdn.totvs.com.br/display/mp/FwQrCode  
User Function TstQrCode1()  
    Local oDLG := Nil  
    Local cCodigo := "http://www.totvs.com.br" + Space(60)  
    Private cLocalImg  
    Private oQrCode  
  
//Cria a Dialog  
    DEFINE MSDIALOG oDlg TITLE "RDMAKE para teste da classe FwQrCode" FROM 0,0 TO 400,800 PIXEL  
  
//Cria o objeto FwQrCode  
    oQrCode := FwQrCode():New({25,25,200,200},oDlg,cCodigo)  
    cLocalImg:= oQrCode:oQrCode:CBMPFILE  
  
//Exibe a Dialog em Video  
    ACTIVATE MSDIALOG oDlg CENTERED  
  
    U_TESTE03()  
Return  
  
user function teste03()  
    local oReport  
    RpcSetEnv("99","01")  
    oReport := reportDef(oReport)  
    oReport:printDialog()  
     
    FreeObj(oReport)  
    RpcClearEnv()  
Return  
  
static function reportDef(oReport)  
    local cTitulo := "Teste do metodo SayBitmap "  
    local cFile := 'TREPORT_'+ StrTran(Time(), ":", "-")  
  
    oReport := TReport():New(cFile, cTitulo, nil, {|oReport| PrintReport(oReport)},cTitulo)  
    oReport:SetPortrait()  
    oReport:SetTotalInLine(.F.)  
    oReport:ShowHeader()  
    oReport:lPreview:= .T.  
    oReport:nDevice := 6  
    oReport:nEnvironment:= 1  
  
Return oReport  
  
Static Function PrintReport(oReport)  
    oReport:SayBitmap( 600,100,cLocalImg,400,400 )  
Return
```

**Saiba Mais**

[TReport](https://tdn.totvs.com/display/public/framework/TReport)

[FwQrCode](https://tdn.totvs.com/display/public/framework/FwQrCode)
