---
article_id: 360016376212
category: ADVPL - Classe e Função
content_hash: 6c5847bd49d5015028ee78576766ded794d27f49fb1884985d1702a171dfdd48
fetched_at: '2026-06-28T22:40:16.986010+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Método INT25
type: support-article
updated_at: '2025-05-13T19:26:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016376212-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-M%C3%A9todo-INT25
---

**Ocorrências**1- A **FWMSPRINTER** tem os formato ITF14 ou DUN14 ?

2- Ao utilizar a classe **FWMsBar**(INT25), o **Protheus** não esta respeitando nenhuma configuração nessa classe, a largura do código de barras, ele fica grande demais para passar em uma leitura de banco  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL –  A partir da versão 12.1.17  
  
**Causa** o **FWMSBar** possui algumas limitações neste aspecto.

**Solução**

1- O DUN14 tem as mesmas características do método INT25 já existente na **FWMsPrinter**.

2 - Os métodos específicos permitem melhor dimensionamento dos objetos gráficos no relatório enquanto

Imprime código de barra no padrão Int25  
  
@param nRow Posição relativa ao topo  
@param nCol Posição relativa à esquerda  
@param cCodeBar Texto a ser codificado  
@param nWidth Largura da Barra  
@param nHeight Altura da Barra  
@param lSay Indica se deve colocar say com o conteúdo em baixo do código de barras  
@param lCheck Indica se deve calcular o digito verificador  
  
//--------------------------------------------------------------  
Method Int25(nRow,nCol,cCodeBar,nWidth,nHeight,lSay,lCheck,oFont) Class FWMSPrinter

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Exemplo de customização

```
#Include "PROTHEUS.CH  
#Include "RPTDEF.CH"  
#INCLUDE "TBICONN.CH"  
  
User Function Int25()  
  
Local oFont := TFont():New('Courier new',,-16,.T.)  
local cLineDig := ""  
Local lAdjustToLegacy := .T.  
Local lDisableSetup := .T.  
Local cNUM:="0001" //É O NOME DO BOLETO NO MEU CASO O CODIGO DA NOTA  
Local CodBarras := "23793047089000000042384022562100266430000100000" //CODIGO DE BARRAS A SE DECODIFICADO  
Private oPrn  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"  
  
oPrn := FWMSPrinter():New(cNUM,IMP_PDF,lAdjustToLegacy,,lDisableSetup,,,,,.F.)//instaciando a classe  
oPrn:SetResolution(72)  
oPrn:SetPortrait()  
oPrn:SetPaperSize(DMPAPER_A4)  
oPrn:StartPage()  
oPrn:cPathPDF := "c:\Temp\"  
oPrn:Int25(000800,300,CodBarras,0.73,40,.F.,.F., oFont)  
oPrn:EndPage()  
oPrn:Preview()  
FreeObj(oPrn)  
  
RESET ENVIRONMENT  
  
Return
```
