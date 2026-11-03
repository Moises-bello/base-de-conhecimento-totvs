---
article_id: 20713955329047
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 661e58e875e131971262512c12d3961136a1beada9cf5e538e863f2b278216ec
fetched_at: '2026-06-28T22:38:39.590425+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Help A410ADTMOED
  no Faturamento
type: support-article
updated_at: '2024-02-01T21:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20713955329047-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Help-A410ADTMOED-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20713955296023) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como resolver o Help A410ADTMOED no Faturamento?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Deixe a moeda do pedido de venda como moeda forte, ou seja deixe o campo "Moeda (C5\_MOEDA)" = 1 (real). Esse Help só ocorre quando MV\_PAISLOC = 'BRA'.

O Relacionamento de Títulos de Adiantamento com Pedidos de Venda deve ocorrer somente se tanto o Pedido quanto o Título utilizarem a Moeda Corrente (Moeda 1). Para efetuar a compensação em outras moedas, utilize a rotina de Compensação de Títulos a Receber do módulo Financeiro.

Caso o pedido de venda tenha vindo do módulo de exportação, deve-se realizar a exclusão do pedido de venda e feito novamente e, colocado uma condição de pagamento no exportação, campo "Cond. de Pagamento SIGA (Y6\_SIGSE4)" que não tenha o campo "Adiantamento (E4\_CTRADT)" = '2 - Não'.

Isso ocorre pois o processo de RA (Recebimento Adiantado) em um pedido do módulo de exportação é realizado nas próprias rotinas do módulo de exportação.

Dúvidas nesse processo, contate a Equipe Protheus Trade.

**Saiba mais:**

[FAT0149 - Recebimento Antecipado (RA/Adiantamento) no Pedido de Venda (MATA410)](https://tdn.totvs.com/x/GkD2Dw)
