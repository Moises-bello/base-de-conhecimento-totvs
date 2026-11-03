---
article_id: 21480048393495
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: ea29ca717863589744a06e3a73190333f220f514dc2fc134843adec561bb99f0
fetched_at: '2026-06-28T22:38:41.019872+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus – SIGAFAT – Descontos no valor total
  do pedido de venda
type: support-article
updated_at: '2024-07-11T11:30:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21480048393495-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Descontos-no-valor-total-do-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21480048372887) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**

Como dar descontos no valor total do pedido de venda?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus – Faturamento (SIGAFAT) – Todas as versões

**Solução**

É possível não dar descontos por item e sim desconto sobre o valor total cheio do pedido de venda.

Basta saber se quer dar o valor em porcentagem ou valor cheio total.

OBS 1: Os campos ficam no cabeçalho

OBS 2: O valor que será submetido ao crédito nesse caso é o valor sem o desconto desses campos.

OBS 3: Ao faturar, o valor do desconto irá para o campo F2\_PDESCAB e F2\_DESCONT respectivamente.

OBS 4: Esses descontos não vão aos campos de desconto C6\_VALDESC e C6\_DESCONT.

Campo de desconto por porcentagem: **"%Indenizacao (C5\_PDESCAB)"**

Campo de desconto por valor: **"Indenizacao (C5\_DESCONT)"**

Exemplo:

* Total do pedido de venda no momento e R$1000 já com descontos no item.
* Ao informar **"Indenizacao (C5\_DESCONT)" = 50,** o valor total novo é R$950

**Saiba mais:**

[FAT0035 - Descontos, acréscimos e arredondamentos no Faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=225266984)
