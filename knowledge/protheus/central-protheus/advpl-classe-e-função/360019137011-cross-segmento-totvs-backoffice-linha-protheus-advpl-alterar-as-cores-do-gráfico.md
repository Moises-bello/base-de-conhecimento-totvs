---
article_id: 360019137011
category: ADVPL - Classe e Função
content_hash: 73b035f45c2a19d5d49ba25d60adc11f101f775165bfed0c6b80273a1d2e02b3
fetched_at: '2026-06-28T22:40:14.362805+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alterar as cores
  do gráfico (Fwchart)
type: support-article
updated_at: '2022-01-03T20:38:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019137011-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Alterar-as-cores-do-gr%C3%A1fico-Fwchart
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**É possível trocar a cor dos componentes do gráfico criado pelas classes de geração de gráfico?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Utilize a propriedade oFwChartColor (presente nos objetos instanciados pelas classes de geração de gráfico) em conjunto com o método SetColor().  
  
**Observação**  
Não é possível fazer a atribuição de cores por cada elemento exibido e só há as opções *BLUE* (tons de azul) ou *RANDOM* (cores aleatórias).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014848792/mceclip3.png)  
  
**EXEMPLO**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "PRCONST.ch"  
  
// FUNÇÃO DE GERAÇÃO DE GRÁFICO  
User Function T131CHART()  
    Local oDlg   := NIL // CAIXA DE DIÁLOGO QUE SERÁ EXIBIDO O GRÁFICO  
    Local oChart := NIL // OBJETO DO GRÁFICO  
  
    // DECLARAÇÃO DE DOS ATRIBUTOS DA CAIXA DE DIÁLOGO  
    DEFINE MSDIALOG oDlg PIXEL FROM 10,0 TO 400,400  
        oChart := FwChartPie():New() // INSTANCIAÇÃO DO OBJETO  
          
        // INICIALIZAÇÃO E VINCULAÇÃO COM A CAIXA DE DIÁLOGO  
        oChart:Init(oDlg, .T.)  
          
        // ADIÇÃO DOS DADOS QUE SERÃO EXIBIDOS  
        oChart:AddSerie("Jair Bolsonaro - PSL", 46.03)  
        oChart:AddSerie("Fernando Haddad PT", 29.28)  
        oChart:AddSerie("Ciro Gomes - PDT", 12.47)  
        oChart:AddSerie("Geraldo Alckmin - PSDB", 04.76)  
        oChart:AddSerie("João Amoêdo - NOVO", 02.50)  
        oChart:AddSerie("Cabo Daciolo - PATRIOTA", 01.26)  
        oChart:AddSerie("Outros - SPD", 03.70)  
  
        // INFORMA A LOCALIZAÇÃO DA LEGENDA  
        // EM RELAÇÃO A CAIXA DE DIÁLOGO  
        oChart:SetLegend(CONTROL_ALIGN_LEFT)  
  
        // ALTERA A COR PADRÃO DO GRÁFICO  
        oChart:oFwChartColor:SetColor("RANDOM")  
        
        // MONTA O GRÁFICO  
        oChart:Build()  
    ACTIVATE MSDIALOG oDlg // EXIBE A CAIXA DE DIÁLOGO  
Return (NIL)
```

**Saiba mais**[Classe FwChartPie](http://tdn.totvs.com/pages/releaseview.action?pageId=6815502)
