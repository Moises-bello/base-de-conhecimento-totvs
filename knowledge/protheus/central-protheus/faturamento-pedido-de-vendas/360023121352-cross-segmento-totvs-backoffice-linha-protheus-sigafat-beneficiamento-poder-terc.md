---
article_id: 360023121352
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3171f1252ba3755e7415eca380eac29a5176b0b7ffd5b022b7666067cdc5dbb9
fetched_at: '2026-06-28T22:38:38.449729+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Beneficiamento
  Poder Terceiro Utiliza Fornecedor
type: support-article
updated_at: '2022-08-24T18:24:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023121352-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Beneficiamento-Poder-Terceiro-Utiliza-Fornecedor
---

**Dúvida**

Como utilizar beneficiamento no modulo de Faturamento (controle Poder Terceiro)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O Controle de beneficiamento pode e deve ser utilizado quando:

- Houver um beneficiamento de material

- Houver uma simples remessa onde o retorno do material eh obrigatório.

Para a correta utilização do controle de poder de terceiros/em terceiros temos:

**A) Poder de Terceiros:** Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Controle de Poder de Terceiros

**B) Poder em Terceiro :** Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como efetuar o controle de poder em terceiros

**Observações:**

1) Item que controla Poder em terceiro não trata Financeiro, gerando um contas a Receber/Pagar (mesmo com TES configurada com o campo "Gera duplicata = SIM"); bem como,

Não utiliza Preço de Venda (A partir do Preço de Venda / Preço de Lista - Tabela de Preço), pois Beneficiamento não se trata de uma Venda.

Saiba mais: <https://tdn.totvs.com/x/wq48E>

2) Quando for informado o numero da OP na entrada do material e o mesmo movimentar estoque este será requisitado diretamente para o custo da OP.

3) A movimentação do estoque é opcional no controle de poder de terceiros, mas se efetuada será considerada no calculo do MRP.

4) Caso seja movimento estoque na entrada ou na saída do material obrigatoriamente deve-se efetuar o mesmo na devolução do material.

5) Caso seja efetuada uma operação triangular deve-se configurar os parâmetros das rotinas para contempla-la. ( F12 ou F10 no browse da rotina).
