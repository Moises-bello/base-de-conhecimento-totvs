---
article_id: 25287190760727
category: Financeiro - Liquidação a Receber
content_hash: c10a0e1fbfb0b84cc80a590f95b267716d0a3ad6fb832e4b8cc728373451eb0b
fetched_at: '2026-06-28T22:37:42.266228+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA460 - Não gera comissão
  nos título liquidados.
type: support-article
updated_at: '2025-07-30T20:47:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25287190760727-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA460-N%C3%A3o-gera-comiss%C3%A3o-nos-t%C3%ADtulo-liquidados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25287183002775) Tempo aproximado para leitura: **00:00:20 min****Dúvida**Ao realizar a liquidação de títulos com vendedor associado, as informações **não são registradas** nos títulos liquidados.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA460 - Todas as versões.

**Solução**A gravação dos campos referentes à base de cálculo e valor a ser pago de comissão para o vendedor na tabela **Contas a Receber** (**SE1**) não terão seus valores gravados quando a origem dos títulos for da rotina **Liquidação** (**FINA460**). Para o correto cálculo da comissão, bem como a base de comissão, a rotina irá buscar os valores no título "**Pai**" e realizar os devidos cálculos.

**Saiba mais**

[FINA460 - Liquidação a receber - P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=545236275)
