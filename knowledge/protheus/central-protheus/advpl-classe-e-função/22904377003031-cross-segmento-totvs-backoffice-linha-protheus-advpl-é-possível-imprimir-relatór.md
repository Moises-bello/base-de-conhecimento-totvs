---
article_id: 22904377003031
category: ADVPL - Classe e Função
content_hash: 1fb17f20339e6bb4cdcafa8900941d5f80f54081ba00d4469063855acf83df30
fetched_at: '2026-06-28T22:40:20.647322+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  É possível imprimir
  relatório TReport Zebrado?
type: support-article
updated_at: '2024-04-18T19:11:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22904377003031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-imprimir-relat%C3%B3rio-TReport-Zebrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22904367691159)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**É possível imprimir o relatório TReport Zebrado?  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**

A classe Treport não tem como definir somente um cabeçalho ou sessão se será em negrito, somente o relatório todo. O que pode ser feito é definir uma cor para a coluna através da trsection.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22904376935575)

**Exemplo:**

```
#include "protheus.ch"  
  
User function trepcor()  
  
 Local oReport  
 oReport := ReportDef()  
 oReport:PrintDialog()  
  
Return  
  
Static Function ReportDef()  
 Local oReport  
 Local oSection  
  
 oReport:= TReport():New("TSTREPORT","Relatorio Teste de Cor de fundo",,{|oReport| PrintReport(oReport)},"Teste de Relatorio.")  
  
 oReport:SetLandscape()  
 oReport:HideParamPage()  
  
 oSection:= TRSection():New(oReport,"Cliente",{},{})  
  
 TRCell():New(oSection,"CNPJ"  ,,"CNPJ" ,"@!",30,/*lPixel*/,/*{|| code-block de impressao }*/)  
  
 TRCell():New(oSection,"CODIGO"  ,,"Codigo" ,"@!",25,/*lPixel*/,/*{|| code-block de impressao }*/)  
  
 TRCell():New(oSection,"LOJA"  ,,"Loja" ,"@!",15,/*lPixel*/,/*{|| code-block de impressao }*/)  
  
 TRCell():New(oSection,"NOME"  ,,"Nome" ,"@!",50,/*lPixel*/,/*{|| code-block de impressao }*/)  
  
 TRCell():New(oSection,"CIDADE"  ,,"Cidade"  ,"@!",50,/*lPixel*/,/*{|| code-block de impressao }*/)  
  
 oSection:SetLineStyle()  
  
Return oReport  
  
Static Function PrintReport(oReport)  
  
 Local oSection := oReport:Section(1)  
 Local aCliente := {}  
 Local i  
  
 oSection:SetTotalInLine(.F.)  
  
 aadd(aCliente,{"28154847000101","000001","01","NOME EMPRESA 1","SAO PAULO"})  
 aadd(aCliente,{"28154847000102","000002","01","NOME EMPRESA 2","SAO PAULO"})  
 aadd(aCliente,{"28154847000103","000003","01","NOME EMPRESA 3","SAO PAULO"})  
 aadd(aCliente,{"28154847000104","000004","01","NOME EMPRESA 4","RIO DE JANEIRO"})  
  
 oReport:SetMeter(Len(aCliente))  
  
 oReport:IncMeter()  
 oSection:Init()  
  
 For i:= 1 to len(aCliente)  
  
 If oReport:Cancel()  
 Exit  
  
 EndIf  
  
 oReport:IncMeter()  
  
 oSection:Cell("CNPJ"):SetClrBack(CLR_BLACK)            // alterando a cor de fundo da linha  
  
 oSection:Cell("CNPJ"):SetClrFore(CLR_WHITE)          // alterando cor da fonte  
  
 //oSection:Cell("CODIGO"):SetClrBack(CLR_RED)  
  
 //oSection:Cell("LOJA"):SetClrBack(CLR_RED)  
  
 //oSection:Cell("NOME"):SetClrBack(CLR_RED)  
  
 //oSection:Cell("CIDADE"):SetClrBack(CLR_RED)  
  
 oSection:Cell("CIDADE"):SetSize(50)  
  
 oSection:PrintLine()  
  
 oReport:ThinLine()  
  
 Next  
  
 oReport:ThinLine()  
  
 oSection:Finish()  
  
Return
```

**Saiba mais**

[Treport](https://tdn.totvs.com/display/public/framework/TReport)

[TrSection](https://tdn.totvs.com/display/public/framework/TRSection)
