---
article_id: 4412672358167
category: ADVPL - Classe e Função
content_hash: 6c3c538a5c321f35c55a06b7365a5e058196020d8aee55a500f8afc16ab80457
fetched_at: '2026-06-28T22:40:20.693847+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como gerar arquivo
  PDF utilizando a classe FWMSPrinter() para impressão via SPOOL
type: support-article
updated_at: '2023-05-18T19:57:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412672358167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-gerar-arquivo-PDF-utilizando-a-classe-FWMSPrinter-para-impress%C3%A3o-via-SPOOL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como gerar arquivo PDF utilizando a classe FWMSPrinter() para impressão via SPOOL, sem utilizar a tela de Setup?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**Para ser gerada corretamente o arquivo pdf sem a tela de *setup*, o parâmetro **cPrinter** da classe **FwMsPrinter()** deve conter o nome completo da impressora, exemplo: "Microsoft Printer to PDF", exemplo:

```
#INCLUDE "RPTDEF.CH"  
#INCLUDE "FWPrintSetup.ch"  
#INCLUDE "TOTVS.ch"  
  
User Function MyCod128()  
local cCodBar := "789001006189"  
Local cCodINt25 := "34190184239878442204400130920002152710000053475"  
Local cLocal := ""  
Local cPrinter := "Microsoft Print to PDF"   
Local lAdjustToLegacy := .F.  
Local lDisabeSetup := .T.  
Local lPDFAsPNG := .F.  
Local lRaw := .T.  
Local lServer := .F.  
local lTReport := .F.  
Local lViewPDF := .T.  
Local n := 0  
Local nI := 0  
Local nQtdCopy := 1  
Local oPrint  
  
rpcsetenv("99","01")  
  
  
nLinC := 10 //Linha que ser? impresso o C?digo de Barra  
nColC := 0.90 //Coluna que ser? impresso o C?digo de Barra  
nWidth := 0.0164 //Numero do Tamanho da barra. Default 0.025 limite de largura da etiqueta ? 0.0164  
nHeigth := 1.5 //Numero da Altura da barra. Default 1.5 --- limite de altura ? 0.3  
lBanner := .T. //Se imprime a linha com o c?digo embaixo da barra. Default .T.  
nPFWidth := 0.2 //N?mero do ?ndice de ajuste da largura da fonte. Default 1  
nPFHeigth := 0.2 //N?mero do ?ndice de ajuste da altura da fonte. Default 1  
lCmtr2Pix := .T. //Utiliza o m?todo Cmtr2Pix() do objeto Printer.Default .T.  
cFilePrintert := "Boleto"+ALLTRIM(STR(int(SECONDS())))+"Nota"  
cPathInServer := "\SPOOL\"//Caminho onde vai ser gerado o boleto grafico abaixo do System  
  
for n:=1 to 1  
cFilePrintert := "Boleto"+ALLTRIM(STR(int(SECONDS())))+"Nota"  
cNameArq:=cPathInServer+cFilePrintert+".PDF"  
oPrint := FWMSPrinter():New(cFilePrintert ,IMP_SPOOL/*IMP_PDF*/, lAdjustToLegacy, /*cPathInServer*/, lDisabeSetup , lTReport, /*@oPrintSetup*/, cPrinter, lServer, lPDFAsPNG, /*lRaw*/, /*lViewPDF*/, /*nQtdCopy*/ )  
oPrint:SetResolution(72)  
oPrint:SetPortrait()  
oPrint:SetPaperSize(DMPAPER_A4)  
oPrint:SetMargin(60,60,60,60) // nEsquerda, nSuperior, nDireita, nInferior  
oPrint:cPathPDF:="C:\teste\"  
oPrint:lInJob := .F.  
  
oFont8 := TFont():New("Arial",9,8,.T.,.F.,5,.T.,5,.T.,.F.)  
oFont10 := TFont():New("Arial",9,10,.T.,.T.,5,.T.,5,.T.,.F.)  
oFont20 := TFont():New("Arial",9,20,.T.,.T.,5,.T.,5,.T.,.F.)  
  
oPrint:StartPage() // Inicia uma nova p?gina  
nRow1 := 1  
oPrint:Line (nRow1+0100,500,nRow1+0070, 500)  
oPrint:Line (nRow1+100,100,nRow1+0100,710)  
oPrint:Say (nRow1+0080,100,"Itaú Unibanco",oFont10 ) // [2]Nome do Banco  
oPrint:Say (nRow1+0080,513,"341"+"-7",oFont20 ) // [1]Numero do Banco  
oPrint:Say (nRow1+0110,100,"Código digitavel",oFont8 )  
oPrint:Say (nRow1+0120,100,"remetente | remetente" ,oFont8 )  
oPrint:FWMSBAR("INT25" /*cTypeBar*/,11/*nRow*/ ,10/*nCol*/, cCodINt25/*cCode*/,oPrint/*oPrint*/,.T./*lCheck*/,/*Color*/,.T./*lHorz*/,0.02/*nWidth*/,0.8/*nHeigth*/,.T./*lBanner*/,"Arial"/*cFont*/,NIL/*cMode*/,.F./*lPrint*/,2/*nPFWidth*/,2/*nPFHeigth*/,.F./*lCmtr2Pix*/)  
oPrint:QRCode(0300,100,"QR Code gerado com sucesso", 100)  
oPrint:DataMatrix(300,300,"DataMatrix gerado com sucesso", 100)  
oPrint:EndPage() // Finaliza a pagina  
oPrint:Print() //efetua geração do rel em estado de Job  
NEXT  
  
Return
```

**Saiba mais**  
[FWMsPrinter](https://tdn.totvs.com/display/public/PROT/FWMsPrinter)
