---
article_id: 360024727053
category: ADVPL - Classe e Função
content_hash: bdf519ea995df0b83e51b633558776ce18a4fff63a95363d507dee0c001c76a9
fetched_at: '2026-06-28T22:40:16.941666+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Impressão de códigos
  de barras MsBar3
type: support-article
updated_at: '2022-03-09T19:14:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024727053-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impress%C3%A3o-de-c%C3%B3digos-de-barras-MsBar3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Tenho um fonte customizado que imprime códigos de barras no formato EAN13 utilizando a função MsBar3(), contudo o mesmo tem apresentado algumas inconsistências na impressão.

```
MsBar3("EAN13", 0.5, 0.9, cCode, oPrinter, .F., NIL, .T., 0.029, 0.6, .F., NIL, NIL, .F.)
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**A função MsBar3() pertence a classe TMSPrinter(), a qual foi descontinuada, desta forma, não sofrendo mais manutenções ou melhorias.  
Contudo, para a mesma tratativa, foi disponibilizada a classe FwMsPrinter()em conjunto com o método método FwMsBar().  
  
**Exemplo**

```
#Include "TOTVS.ch"  
#Include "RPTDEF.ch"  
  
User Function INT25()  
    Local cFile    := "0001"  
    Local cCode    := "1234567890128"  
    Local lLegacy  := .T.  
    Local lSetup   := .T.  
    Local oPrinter := NIL  
  
    RPCSetEnv("99", "01")  
        oPrinter := FwMsPrinter():New(cFile, IMP_PDF, lLegacy, NIL, lSetup, NIL, NIL, NIL, NIL, .F.)  
        oPrinter:SetPaperSize(DMPAPER_A4)  
        oPrinter:SetResolution(72)  
        oPrinter:SetPortrait()  
  
        oPrinter:StartPage()  
            oPrinter:cPathPDF := "C:\Temp\"  
            oPrinter:FwMsBar("EAN13", 0.5, 0.9, cCode, oPrinter, .F., NIL, .T., 0.029, 0.6, .F., NIL, NIL, .F.)  
        oPrinter:EndPage()  
  
        oPrinter:Preview()  
  
        FreeObj(oPrinter)  
    RPCClearEnv()  
Return (NIL)
```

 **Saiba mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Método INT25](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016376212)

[MSBAR3 -Impressão de código de barras na deskjet HP e laser](https://tdn.totvs.com/pages/releaseview.action?pageId=6090908)

[FWMsPrinter](http://tdn.totvs.com/display/PROT/FWMsPrinter)
