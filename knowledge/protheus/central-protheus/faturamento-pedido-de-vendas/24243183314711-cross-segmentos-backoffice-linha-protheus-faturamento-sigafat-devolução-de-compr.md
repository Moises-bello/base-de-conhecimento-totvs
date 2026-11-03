---
article_id: 24243183314711
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0522147c0f2a7382deb2c22c08543d15e7bdaaa4988411fdeddf3f78196b1754
fetched_at: '2026-06-28T22:38:38.687715+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Devolução
  de Compras emitida pelo fornecedor
type: support-article
updated_at: '2025-10-20T18:26:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24243183314711-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Devolu%C3%A7%C3%A3o-de-Compras-emitida-pelo-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24243215092887) Tempo aproximado para leitura: **03:00:00 min****Dúvida**Como incluir nota de devolução emitida pelo fornecedor, visto que não irei emitir a devolução com formulário próprio?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**

Para inserir a nota fiscal de devolução do fornecedor no sistema, é necessário verificar se a nota precisa apenas ser registrada sem movimentar estoque, financeiro e contábil, dependendo da necessidade há duas formas de inclusão:

**1. Quando a empresa precisa inserir a nota e atualizar os saldos de estoque, contábil e financeiro:**

É necessário gerar o pedido na **MATA410 (Pedido de Vendas)** referenciando a nota de origem a partir do processo padrão do faturamento, o documento apenas não será transmitido. Não há um processo para que a nota de devolução emitida pelo fornecedor seja vinculada na nota de compra de origem.

**2. Quando não necessita atualizar Estoque, Contábil e Financeiro:** Realize o processo na **MATA920 - Nota Fiscal Manual de Saída.**

**Saiba mais:**

[**Cross Segmentos - Backoffice Protheus - SIGAFAT - Como fazer uma devolução de compras**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022341592-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-fazer-uma-devolu%C3%A7%C3%A3o-de-compras)

[**MP - SIGAEST - MATA910 - Nota Fiscal Manual de Entrada e MATA920 - Nota Fiscal Manual de Saída**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022341592-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-fazer-uma-devolu%C3%A7%C3%A3o-de-compras)
