---
article_id: 27992270791831
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: e43a9a0571cd5e7e151c21c604a284a97d35f64f4d46b23d72503be83f7085ef
fetched_at: '2026-06-28T22:38:39.983065+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Pontos de entrada no endereçamento
  de produtos no faturamento
type: support-article
updated_at: '2024-11-22T17:54:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27992270791831-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pontos-de-entrada-no-endere%C3%A7amento-de-produtos-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27992270740631) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais os pontos de entrada no endereçamento de produtos no faturamento?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

A ordem que aparece na consulta de endereçamento no campo do pedido de venda, não depende da validade de lote (FEFO) e nem o campo BE\_PRIOR.

O FEFO (primeira a vencer, primeiro a sair) ocorre no faturamento, ao faturar sem o C6\_LOCALIZ informado. Ai sim ele por si decidi o lote/endereço mais perto do vencimento para usar (caso seja configurado para).

Para administrar esse processo, há dois pontos de entrada:

* [MTF4LOC](https://tdn.totvs.com/x/mOR)
* [MTVLDLOC](https://tdn.totvs.com/x/zKln)

Dúvidas na tela do lote no pedido de venda ou nos pontos de entrada acima, contate a Equipe Protheus Estoque.

**Saiba mais:**

[**Cross Segmentos - TOTVS Backoffice (Linha Protheus) – SIGAFAT – Todos os Pontos de Entrada no Faturamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028794472-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Todos-os-Pontos-de-Entrada-no-Faturamento?source=search)
