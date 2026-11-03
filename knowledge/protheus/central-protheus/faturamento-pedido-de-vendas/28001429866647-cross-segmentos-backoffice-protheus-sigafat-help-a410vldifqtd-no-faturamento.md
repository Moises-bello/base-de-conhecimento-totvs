---
article_id: 28001429866647
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6084e23471772e8106bc83ea2d4693fb869a008259c32a475cd148b927d61caf
fetched_at: '2026-06-28T22:38:39.830237+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A410VLDIFQTD no Faturamento
type: support-article
updated_at: '2024-11-28T15:06:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28001429866647-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410VLDIFQTD-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28001446614167) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como resolver o help A410VLDIFQTD no Faturamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**O erro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28133485091223)

Ocorre por conta da tentativa de devolução de entrada "Prc Unitario (C6\_PRCVEN)" está diferente do campo da nota fiscal de entrada "Valor Unitario (D1\_VUNIT)".

Ajuste o campo "Prc Unitario (C6\_PRCVEN)" para ficar com o exato valor (inclusive decimais) do campo "Valor Unitario (D1\_VUNIT)".

Para que o Help ocorra isso tudo precisa estarem todos acontecendo um após o outro:

* 1 | O tipo do pedido de venda tem de ser 'D - Devolução'
* 2 | O campo C6\_NFORI não deve estar vazio
* 3 | O campo da entrada D1\_VALDESC deve estar vazio
* 4 | O C6\_PRCVEN da devolução não estar igual ao D1\_VUNIT da entrada

Qualquer item acima diferente, fará o Help não ocorrer (solucionar).

**Saiba mais:**

**[FAT0068 Aumento de Casas Decimais no ambiente Faturamento (SIGAFAT)](https://tdn.totvs.com/x/twEmDg)**
