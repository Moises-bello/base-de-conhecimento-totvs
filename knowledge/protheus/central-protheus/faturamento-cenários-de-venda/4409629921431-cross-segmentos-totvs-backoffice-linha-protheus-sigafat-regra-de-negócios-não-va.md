---
article_id: 4409629921431
category: Faturamento - Cenários de Venda
content_hash: 807e02a6dd5f447f107bf05f55f4c4cc9a118a7c36b54e761eb5475814bf5e9a
fetched_at: '2026-06-28T22:38:34.131840+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Regra de Negócios
  não valida os Campos "Indenização" (C5_DESCONT) e "%Indenização" (C5_PDESCAB)
type: support-article
updated_at: '2021-09-29T10:56:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409629921431-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Regra-de-Neg%C3%B3cios-n%C3%A3o-valida-os-Campos-Indeniza%C3%A7%C3%A3o-C5-DESCONT-e-Indeniza%C3%A7%C3%A3o-C5-PDESCAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**A Regra de Negócios não valida os descontos lançados nos campos "Indenização" (C5\_DESCONT) e "%Indenização" (C5\_PDESCAB).  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Causa**

A validação realizada pelo sistema, quando cadastrada uma regra na aba de Desconto, é:

O sistema verifica o conteúdo dos campos "Prc Unitário" (C6\_PRCVEN) e "Prc Lista" (C6\_PRUNIT), e considera desconto, aplicável à Regra de Negócios, a diferença entre os valores desses dois campos. Caso o campo "Prc Lista" (C6\_PRUNIT) não esteja preenchido, mesmo que destacado um desconto, o sistema não considera como válida a aplicação de bloqueio pela regra de negócios.

Caso o desconto seja aplicado nos campos "Indenização" (C5\_DESCONT) e "%Indenização" (C5\_PDESCAB), o sistema não irá considerar como aplicável o bloqueio por Regra de Negócio, pois esses campos possuem a característica de aplicação de desconto no total do pedido, ou seja, não trabalham os valores dos itens. A Regra de Negócios trabalha o desconto nos itens, sendo necessário que a aplicação seja na linha do item para que a Regra seja validada.

**Solução**Caso necessite utilizar a Regra de Negócios para bloqueio de percentuais de desconto acima do previsto, utilize os campos de desconto na linha dos itens ou os campos do cabeçalho que afetam os itens, para mais informações sobre os campos de desconto acesse: **[Descontos no Pedido de Vendas](https://tdn.totvs.com/x/KE1tDQ)**
