---
article_id: 1500001965222
category: Faturamento - Cenários de Venda
content_hash: 4b63a642dcb015012a4c8874445aa32e1420b85025209ab3db468d69471ee38b
fetched_at: '2026-06-28T22:38:33.943843+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help OMSTABPRC2
type: support-article
updated_at: '2024-01-29T20:42:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001965222-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-OMSTABPRC2
---

**Ocorrência**Ao incluir pedido de venda, sistema apresenta o help **OMSTABPRC2**, como resolver?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**Esta mensagem indica que foi cadastrada uma condição de pagamento na **Tabela de Preços (OMSA010)**, através do campo Cond. Pagto. (**DA0\_CONDPG**), e ao informar esta tabela de preços no Pedido de Vendas **(MATA410)**, o usuário esta tentando informar uma condição de pagamento diferente.

**Solução**Para solucionar esta ocorrência, verifique os pontos abaixo:

1. Avalie se a Tabela de Preços (**OMSA010**) possui o campo "Cond. Pagto." (**DA0\_CONDPG**) preenchido;

2. Caso possua, é necessário informar esta mesma condição no campo "Cond. Pagto." (**C5\_CONDPAG**), do Pedido de Vendas (**MATA410**), sempre que esta tabela de preços for informada;

3. Lembrando que a Condição de Pagamento preenchida no campo "Cond. Pagto." (**C5\_CONDPAG**), do Pedido de Vendas (**MATA410**), pode ser carregada do Cadastro do Cliente (**MATA030**) pelo campo **A1\_TABELA**;
