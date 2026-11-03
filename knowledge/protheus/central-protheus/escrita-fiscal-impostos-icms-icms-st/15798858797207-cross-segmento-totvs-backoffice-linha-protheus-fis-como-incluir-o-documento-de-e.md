---
article_id: 15798858797207
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 59695051fa14463f16e966b778e73533b5761f251b8702edea45e03fef001330
fetched_at: '2026-06-28T22:39:20.327758+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como incluir o documento
  de entrada para GAS GLP CST61?
type: support-article
updated_at: '2024-05-02T14:29:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15798858797207-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-incluir-o-documento-de-entrada-para-GAS-GLP-CST61
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15798895406615) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como incluir o Documento de entrada para GAS GLP CST61?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Procedimento para lançar a nota fiscal de GAS recebida CST 61.

![](https://totvssuporte.zendesk.com/attachments/token/bCpKonpDHSh5rTkanA2OTqVIh/?name=image.png)

Nota fiscal de entradas

![](https://totvssuporte.zendesk.com/attachments/token/1L1XyegMwYKX1KfoMxTNTxSr8/?name=image.png)

Para o lançamento dessa nota fiscal precisa gerar o UPPDISTR para poder alterar o campo de alíquota do ICMS ST

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Expedição continua Protheus Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7432655235607-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Expedi%C3%A7%C3%A3o-continua-Protheus-Fiscal?source=search)

No SIGACFG // Base de dados // tabela SD1

![](https://totvssuporte.zendesk.com/attachments/token/8HiUXbsXJ9mnWW70La42BaXnb/?name=image.png)

Quantidade = 901

Valor unitário = 4,5545

Valor da mercadoria = 4.103,60

![](https://totvssuporte.zendesk.com/attachments/token/JsL9claI0kuKsDFgUQGtwxL1n/?name=image.png)

Dados recebidos do ICMS ST Monofásico recolhido anteriormente

Base de calculo  = 901

Alíquota ICMS ST = 1,2571

Valor do ICMS ST = 1.132,65

![](https://totvssuporte.zendesk.com/attachments/token/sE5T2rQiSQ6Hnd4EYvbHGW0Cp/?name=image.png)

Boletim

https://tdn.totvs.com/pages/releaseview.action?pageId=765332384
