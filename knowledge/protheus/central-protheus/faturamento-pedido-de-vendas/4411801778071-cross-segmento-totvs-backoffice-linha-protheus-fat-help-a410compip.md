---
article_id: 4411801778071
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 254a7bb858881b454e4bfaf4892bc795c3eccca199589195946360998278a8d3
fetched_at: '2026-06-28T22:38:38.371327+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - HELP A410COMPIP
type: support-article
updated_at: '2022-05-11T17:16:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411801778071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-HELP-A410COMPIP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao incluir uma nota de complemento de ipi, apresenta o help A410COMPIP, como resolver?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Faturamento - Todas as versões  
  
**Causa**Não foi informado a nota de origem no complemento.  
  
**Solução**Ocorre que na validação do sistema quando não há nota de origem informada na inclusão de pedido de venda do tipo complemento de preço/quantidade e esta informação não há como salvar o pedido de complemento, por isso ocorre o help **A410COMPIP**.  
Isto é conceito pois é necessário informar qual nota você esta complementando.

Sendo assim, localize a **NF** **original** por meio do campo **"N.F. Original (C6\_NFORI)"**, no campo tecle **<ENTER>** e depois **[F4]** para localizar a nota e incluir no complemento.

**Saiba Mais**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Inclusão de Pedido de Vendas do Tipo Complemento de Preço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017608012-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Inclus%C3%A3o-de-Pedido-de-Vendas-do-Tipo-Complemento-de-Pre%C3%A7o?source=search)
