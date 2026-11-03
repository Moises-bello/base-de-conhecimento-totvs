---
article_id: 360019090451
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: e4063be50299da65199b2be4aadbf78802eded30dd7b2eb02dfe02f865ebd229
fetched_at: '2026-06-28T22:38:41.054359+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Qual o procedimento de Venda para Entrega Futura
type: support-article
updated_at: '2021-12-13T17:28:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019090451-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Qual-o-procedimento-de-Venda-para-Entrega-Futura
---

**Duvida**

Qual o procedimento de Venda para Entrega Futura?

**Ambiente**

Cross Segmentos- TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT)–  A partir da versão 11.80.

**Solução**

Para o processo de entrega futura pode ser utilizado o contrato de parceria (**A**) ou Pedido de Venda (**B**).

Recomendamos a utilização da rotina Contrato de parceria para estabelecer relacionamento entre os movimentos e assim, maior controle, diferente de Pedidos de Venda, individuais.

**A** **- CONTRATO DE PARCERIA: FATA400**

Esta rotina gerencia o controle de parcerias para o processo de venda.

Para utilização, Inclua um contrato de venda utilizando uma Tes para cobrança e uma Tes para remessa do produto.

Após a aprovação o sistema irá gera um pedido de vendas apenas para a cobrança do contrato.

Após a aprovação, o contrato ficará apto para efetuar a remessa do produto, que poderá ser efetuado por partes ou de forma integral.

**B** **- PEDIDO DE VENDA: MATA410**

A venda futura constitui-se na geração de duas notas fiscais:

         1. Nota Fiscal de Venda;

         2. Nota Fiscal de Simples Remessa.

Essas notas não tem vínculo entre elas, são pedidos que serão gerados de forma separada para o cliente, onde um apenas será gerado para gerar a cobrança e o outro gerado para tratar a remessa dos produtos.

Por isso, que indicamos o uso do contrato de parceria, visto que o  vínculo entre os pedidos será o número do contrato.

**Saiba mais detalhes e outras informações pertinentes ao processo de Venda Para Entrega Futura**:

**[FAQ de auxilio Venda para Entrega Futura](https://tdn.totvs.com/pages/releaseview.action?pageId=225264561)**
