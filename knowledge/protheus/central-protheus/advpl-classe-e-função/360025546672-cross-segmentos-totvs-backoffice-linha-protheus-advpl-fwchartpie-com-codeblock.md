---
article_id: 360025546672
category: ADVPL - Classe e Função
content_hash: eef395709bf0da405f53ef5106931ef72432e4f6186c17ed5d59f9434a842d57
fetched_at: '2026-06-28T22:40:19.490080+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - FwChartPie com
  codeblock
type: support-article
updated_at: '2022-01-10T22:27:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025546672-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-FwChartPie-com-codeblock
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**É possível passar um *codeblock* ao efetuar duplo clique sobre o gráfico?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Utilize a propriedade **Bserieaction** , exemplo:

```
#INCLUDE "PROTHEUS.CH"  
  
User Function chartpie()  
Local oChart  
Local oDlg  
Local nVisual:= 1  
  
DEFINE MSDIALOG oDlg PIXEL FROM 10,0 TO 600,600  
  
oChart := FWChartPie():New()  
oChart:Init( oDlg , .T. , .T. )  
oChart:SetTitle( "STR0120" + If( nVisual == 1, "STR0115" , "STR0121" ) )  
oChart:SetColor( "RANDOM" )  
oChart:addSerie( "Votos PT", 50 )  
oChart:addSerie( "Votos PMDB", 30 )  
oChart:addSerie( "Votos PV", 20 )  
oChart:setLegend( CONTROL_ALIGN_LEFT )  
  
oChart:bSerieAction := {||Alert("TESTE")}  
oChart:Build()  
ochart:saveToPng(1,1,300,340,"c:/01/uimagem.bmp")  
Activate MsDialog oDlg Center  
  
Return
```

**Saiba Mais**[FwChartPie](http://tdn.totvs.com/display/public/PROT/FwChartPie)
