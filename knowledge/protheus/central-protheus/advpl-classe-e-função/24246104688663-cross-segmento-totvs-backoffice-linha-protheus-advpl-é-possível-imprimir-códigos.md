---
article_id: 24246104688663
category: ADVPL - Classe e Função
content_hash: 6962877cf90d1fb4b1112cc1fc5e9806225af090d79bedc9f3ae75f594ae7c95
fetched_at: '2026-06-28T22:40:21.537870+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- É possível imprimir
  códigos de barras na classe TReport?
type: support-article
updated_at: '2024-06-18T19:22:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24246104688663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-imprimir-c%C3%B3digos-de-barras-na-classe-TReport
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24246104672279) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**É possível imprimir códigos de barras na classe TReport?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

A classe *TReport* não possui método específico para impressão de código de barras, entretanto pode ser usado a função *MsBar4*.

![gif1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24246149857175)

**Exemplo**

```
#Include 'Protheus.ch'  
  
User Function TesteBAR()  
Local oReport := ReportDef()  
  
oReport:PrintDialog()  
  
Return NIL  
  
Static Function ReportDef()  
Local oReport := NIL  
Local oSection1 := NIL  
Local cTitle := "Exemplo de uso MSBAR4"  
  
oReport:= TReport():New("CODBAR",cTitle,NIL, {|oReport| ReportPrint(oReport)})  
oReport:SetPortrait() // Define a orientacao de pagina do relatorio como retrato.  
oReport:HideParamPage() // Desabilita a impressao da pagina de parametros.  
oReport:nFontBody := 9 // Define o tamanho da fonte.  
oReport:nLineHeight := 50 // Define a altura da linha.  
  
oSection1 := TRSection():New(oReport,"Exemplo",{"SB1"},NIL) // "Ordens de Produção"  
oSection1:SetLineStyle() //Define a impressao da secao em linha  
oSection1:SetReadOnly()  
  
TRCell():New(oSection1,'BARTYPE' ,'SB1',"Tipo Barra",NIL,30,/*lPixel*/,/*{|| code-block de impressao }*/)  
  
Return(oReport)  
  
Static Function ReportPrint(oReport)  
Local oSection1 := oReport:Section(1)  
Local nX := 1  
  
oReport:SetMeter(3)  
oSection1:Init()  
  
oSection1:Cell('BARTYPE'):SetValue('Codigo 128 subset A')  
oSection1:PrintLine()  
MSBAR4("CODE128",2.6,0.2,"12345678901",@oReport:oPrint,NIL,NIL,NIL,8,NIL,.T.,NIL,"A",.F.)  
oReport:IncMeter()  
  
nLoops := 300/oReport:nLineHeight  
If nLoops - Int(nLoops) > 0  
nLoops := Int(nLoops+1)  
EndIf  
For nX := 1 to nLoops  
oReport:SkipLine()  
Next nX  
  
oSection1:Cell('BARTYPE'):SetValue('Codigo 128 subset B')  
oSection1:PrintLine()  
MSBAR4("CODE128",6.0,0.2,"123456789011010",@oReport:oPrint,NIL,NIL,NIL,8,NIL,.T.,NIL,"B",.F.)  
oReport:IncMeter()  
  
nLoops := 300/oReport:nLineHeight  
If nLoops - Int(nLoops) > 0  
nLoops := Int(nLoops+1)  
EndIf  
For nX := 1 to nLoops  
oReport:SkipLine()  
Next nX  
  
oSection1:Cell('BARTYPE'):SetValue('EAN13')  
oSection1:PrintLine()  
MSBAR4("EAN13",9.6,0.2,"123456789012",@oReport:oPrint,.T.,NIL,NIL,6,NIL,.T.,NIL,NIL,.F.)  
oReport:IncMeter()  
  
oSection1:Finish()  
  
Return
```

**Saiba Mais**

[TReport](https://tdn.totvs.com/display/public/framework/TReport)

[Msbar4](https://tdn.totvs.com/pages/releaseview.action?pageId=358452230)
