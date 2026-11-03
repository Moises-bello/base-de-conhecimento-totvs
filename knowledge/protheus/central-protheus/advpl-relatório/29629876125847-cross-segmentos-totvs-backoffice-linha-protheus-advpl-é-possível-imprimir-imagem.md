---
article_id: 29629876125847
category: ADVPL - Relatório
content_hash: 0d2e6566efb77b5f083ceede6fb329f0f93526944cc44343b707a6286da7543e
fetched_at: '2026-06-28T22:40:22.980338+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - É possível imprimir
  imagem pela função SetPrint?
type: support-article
updated_at: '2025-03-06T11:15:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29629876125847-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-imprimir-imagem-pela-fun%C3%A7%C3%A3o-SetPrint
---

Tempo aproximado para leitura: 00:02:00 min

**Dúvida**  
É possível imprimir imagem pela função SetPrint?

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.2310

**Solução**  
Informamos que a função **SetPrint** não realiza a impressão de imagens no relatório, para isso temos a função **FWMSPrinter** com o método **SayBitmap** para imprimir a imagem desejada.  
  
Exemplo:

```
#Include "PROTHEUS.CH"  
#Include "RPTDEF.CH"  
#INCLUDE "TBICONN.CH"  
#INCLUDE "FWPrintSetup.ch"  
  
User Function tstimplc()  
Local oPrinter  
Local cPath := "c:\teste\" //local do .rel  
//Local cPath := "l:/home/evandro/tmp/" -> Linux  
Local nSize  
   
RpcSetEnv('99','01','','')   
  
//oPrinter := FWMSPrinter():New('teste.pdf',IMP_SPOOL,.F.,cPath,.F.,,,"PDFCreator",.T.,.F.,,.F.)  
oPrinter := FWMSPrinter():New('teste.pdf',IMP_PDF,.F.,cPath,.T.,,,,.T.,.F.,,.T.)  
oFont1 := TFont():New('Courier new',,-18,.T.)  
oPrinter:SetParm( "-RFS")  
//oPrinter:setDevice(IMP_PDF)  
oPrinter:cPathPDF := cPath //diretorio na rede do pdf  
//oPrinter:SetPortrait() //retrato  
//oPrinter:SetLandscape() //paisagem   
oPrinter:SetPaperSize(0, 300, 400) //Tamanho da folha  
//oPrinter:Setup()  
  
cTxt := " €€€€ ££££ Lorem ipsum dolor sit amet. Qui laudantium obcaecati a dolores fugit quo dolor iure aut blanditiis facere."  
cTxt2 :="Rem odio nulla et perspiciatis explicabo et nisi facere cum dolor repudiandae nam incidunt dolorem et galisum distinctio qui soluta incidunt."  
  
nSize := oPrinter:GetTextWidth(cTxt, oFont1,2)  
  
oPrinter:SayAlign( 02/*linha*/,10/*coluna*/,cTxt/*texto*/,oFont1/*fonte*/,550/*Largura*/,;  
200/*Altura*/, CLR_HRED/*Cor*/, 3/*AlinhamentoH*/, 2/*AlinhamentoV*/ )  
  
oPrinter:SayAlign( 80/*linha*/,10/*coluna*/,cTxt2/*texto*/,oFont1/*fonte*/,550/*Largura*/,;  
200/*Altura*/, CLR_HRED/*Cor*/, 3/*AlinhamentoH*/, 2/*AlinhamentoV*/ )  
oPrinter:Line( 960, 10, 960, 900, ,"-2")  
  
oPrinter:SayBitmap( 70 , 10 , "\imp\clipng.png" , 550 , 200 )  
  
oPrinter:EndPage()  
oPrinter:Preview()  
FreeObj(oPrinter)  
oPrinter := Nil  
  
Return
```

**Saiba mais**

**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe FWMSPrinter](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024253612-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FWMSPrinter)  
[FWMsPrinter](https://tdn.totvs.com/display/public/framework/FWMsPrinter)**
