---
article_id: 22568139785751
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 187cb99aee171334535b65f84e5077d8dad9c5f44ce72bcd1d032d1e31c4bb1f
fetched_at: '2026-06-28T22:38:39.803163+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help "A410REF"
type: support-article
updated_at: '2024-04-05T11:40:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22568139785751-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410REF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22568130773783) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como resolver o Help "A410REF"?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22568130776471)  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Esse erro ocorre quando o sistema não localiza a referência do item.

**Esse erro só acontecerá se:**

* (1) For utilizado curva de características tabela (SAS - Curva de Características)
* (2) O produto informado existir na tabela (SB4 - Referências de Produto) porém com com a referência vazia
* (3) O produto referência existir na tabela (SB1 - Cadastro de Produtos) e seu campo B1\_GRADE não for "S".

**Para resolver:**

* 1 - Cadastre uma referência do produto do pedido de venda na tabela (SB4 - Referências de Produto)
* 2 - Informe o campo "Utiliza Grade? (B1\_GRADE)" = 'S - Sim' no produto informado no pedido de venda
* 3 - Informe uma outra referência do produto do pedido de venda na tabela (SB4 - Referências de Produto)
