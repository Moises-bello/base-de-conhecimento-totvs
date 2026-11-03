---
article_id: 360025815874
category: Faturamento - Orçamentos
content_hash: e6a1c71949caee07f7af4df2179e8b7780b3c0cc119ca8834d998c2654c636ca
fetched_at: '2026-06-28T22:38:24.951249+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - CJ_STATUS - Orçamento de
  Vendas
type: support-article
updated_at: '2025-10-20T20:07:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025815874-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-CJ-STATUS-Or%C3%A7amento-de-Vendas
---

**Dúvida**

O que é e como tratar cada status do orçamento de vendas do Faturamento?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12

**Solução**

Tratativas para cada status do orçamento:

* **CJ\_STATUS == A** - **Orçamento em aberto** - É quando se efetua o orçamento normalmente, preenchendo cliente, condição de pagamento, produto, preço e TES, ao confirmar, fica em aberto, cor verde.
* **CJ\_STATUS == B** - **Orçamento Baixado** - É quando se efetiva este orçamento em pedido de venda, neste caso, o usuário sairá da rotina **MATA415**, irá para aprovação de orçamento, **MATA416**, e clicará na opção **"Efetivar"**, ao finalizar o processo, o sistema retornará ao browser do orçamento, com o mesmo na cor vermelha, indicando a baixa do orçamento.
* **CJ\_STATUS == C** - **Orçamento Cancelado**- É quando se pega um orçamento em aberto, seleciona o orçamento, e vai em ações relacionadas, opção cancelar, ao confirmar a tela de orçamento, o sistema volta ao browser do mesmo com na cor preta, indicando o cancelamento.
* **CJ\_STATUS == D - Orçamento não Orçado** - Este caso é parecido com o orçamento aberto, o que irá diferenciar é se não informar a quantidade do produto ou o preço, o sistema salvará o orçamento, mas ficará com o status em amarelo, onde o cliente poderá complementar posteriormente estas informações.
* **CJ\_STATUS == F** - **Orçamento Bloqueado** - Este caso é quando se possui uma **regra de negócios** e ao efetuar o orçamento, o mesmo atende aos requisitos da regra, exemplo:

Cenário de vendas - Regra de negócios - incluir uma regra - aba comercialização - produto 000001

Tipo de regra: Exceção

Esta regra informa que toda vez que eu utilizar este produto, o orçamento ou o pedido de venda ficará bloqueado.

No orçamento de vendas, gerado um orçamento em aberto, conforme explicado anteriormente, utilizando o produto em questão, ao confirmar o orçamento, o sistema deixará o mesmo bloqueado, cor marrom.

Para saber o o motivo do bloqueio - basta clicar em ações relacionadas **Blq.regra**.

O sistema exibirá que o orçamento foi bloqueado, o tipo de bloqueio, e no botão regra, poderá ver a regra de negócios que bloqueou.

Para liberar, é preciso ou desativar a regra em questão ou utilizar um outro produto que não entre na regra gerada. O orçamento não possui desbloqueio de regras.

Mais informações sobre o bloqueio por regra, acesse: **[Orçamento de Venda (MATA415) Bloqueado por Regra](https://tdn.totvs.com/x/OekpE)**
