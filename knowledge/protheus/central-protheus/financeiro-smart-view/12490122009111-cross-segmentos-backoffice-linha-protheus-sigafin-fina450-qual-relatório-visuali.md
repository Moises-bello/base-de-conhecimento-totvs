---
article_id: 12490122009111
category: Financeiro - Smart View
content_hash: 0eef9025768809d3d61d71483e8154e3a06a1df4f233cabc39e1de2d7dcd3010
fetched_at: '2026-06-28T22:37:44.700581+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  FINA450 - Qual relatório
  visualiza títulos compensados
type: support-article
updated_at: '2026-03-04T16:55:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12490122009111-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA450-Qual-relat%C3%B3rio-visualiza-t%C3%ADtulos-compensados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25199352479127) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Qual relatório posso emitir para verificar quais títulos foram compensados pela FINA450?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
O relatório **FINR520 utilizado para visualização de títulos compensados, foi descontinuado a partir de outubro de 2024, evoluído para Smartview através do objeto de negócio FINSV033**, compensação entre carteiras.

Para consulta de cada título, existe a **FINC040 a Receber ou FINC050 a Pagar**; a tabela é a **SE5**, e o campo **E5\_TIPODOC**, tem o tipo de movimentação.

O objeto de negócio possibilita a exibição dos ID da compensação, e demonstra os títulos envolvidos. Como mostra o print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37701450097047)

**Saiba Mais**

[Compensação entre carteiras - FINA450](https://tdn.totvs.com/pages/releaseview.action?pageId=516194467)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINSV033 - Visualização de titulos envolvidos na compensação entre carteiras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37698711779735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINSV033-Visualiza%C3%A7%C3%A3o-de-titulos-envolvidos-na-compensa%C3%A7%C3%A3o-entre-carteiras)
