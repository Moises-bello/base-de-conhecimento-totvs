---
article_id: 10222950919575
category: Comércio Exterior - Easy Import Control - Relatórios
content_hash: c14b4b20e5df6964d27baa603c06633cbf281d3c3758ada773325d4b003a9d7f
fetched_at: '2026-06-28T22:39:43.409413+00:00'
product: protheus
section_id: 1500001549662
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Inserir logo na
  impressão da Purchase Order (EICPO150) via ponto de entrada
type: support-article
updated_at: '2022-11-16T13:36:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10222950919575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Inserir-logo-na-impress%C3%A3o-da-Purchase-Order-EICPO150-via-ponto-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como faço para inserir um logo na rotina de Impressão do Purchase Order (**EICPO150**)  via ponto de entrada?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*– Todas versões  
  
**Solução**

```
#Include "Average.Ch"  
  
User Function PO150LGO()  
Local nLinha := PARAMIXB[1]  
oSend(oPrn, "SayBitmap", nLinha+25, 50, "lgrl99.bmp" , 350, 150 )  
Return
```

**Parâmetros**

**![PARAMETROS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10222575827479)**

**Variáveis**

**![VARIAVEIS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10222577397143)**

Este Ponto de Entrada **NÃO** é executado quando o relatório é gerado pelo novo modelo em HTML. Para o novo modelo em HTML, deve seguir os passos disponíveis no documento [Impressão do Purchase Order - EICPO150 (modelo HTML).](https://tdn.totvs.com/pages/releaseview.action?pageId=306858818)  
  
**Saiba mais**[PE PO150LGO Adicionar um Logotipo na Impressão do Purchase Order](https://tdn.totvs.com/pages/releaseview.action?pageId=599611862)
