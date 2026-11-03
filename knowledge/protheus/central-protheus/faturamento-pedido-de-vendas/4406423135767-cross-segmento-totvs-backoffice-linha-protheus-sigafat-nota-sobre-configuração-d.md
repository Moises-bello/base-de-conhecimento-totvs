---
article_id: 4406423135767
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 4f9792b1ad6024e1b9b0351841b39912effe5dfd15891d26e9d30b1460bbcf17
fetched_at: '2026-06-28T22:38:38.578639+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota sobre configuração
  de faturamento para sugerir quantidade de lote mínimo
type: support-article
updated_at: '2021-08-18T11:25:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406423135767-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-configura%C3%A7%C3%A3o-de-faturamento-para-sugerir-quantidade-de-lote-m%C3%ADnimo
---

**Dúvida**

Nota sobre configuração de faturamento para sugerir quantidade de lote mínimo.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**

O módulo de faturamento não possui configuração para sugestão  de quantidade mínima de lote, por padrão, sempre buscará o lote que ***primeiro que expira*** para sugestão na liberação do pedido (**FEFO** - **primeiro que expira, primeiro que sai**).

Se tiver um lote que atenda a necessidade da venda, pode sugerir diretamente no campo do pedido de vendas (**MATA410**), **c6\_lotectl** (lote).

No pedido é possível sugerir a quantidade mínima de venda, desde que informe essa quantidade no campo **b1\_lotven** .

**Saiba mais:**

**[FAT00296 - Lote\_e\_Serie](https://tdn.totvs.com/x/DpNvI)**

**[MP-FAT-Help-FTQTDMIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052520313-MP-FAT-Help-FTQTDMIN)**
