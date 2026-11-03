---
article_id: 4403550628247
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b8975cac577303cbf647e46bca99e54926dcbd17a86eadddd02f4529c75e3901
fetched_at: '2026-06-28T22:38:29.918118+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Ordem de Preço de venda (C6_PRUNIT) no Pedido de Venda.
type: support-article
updated_at: '2021-07-01T13:47:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403550628247-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Ordem-de-Pre%C3%A7o-de-venda-C6-PRUNIT-no-Pedido-de-Venda
---

**Dúvida**Ordem de Preço de venda (C6\_PRUNIT) no Pedido de Venda.

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - A partir da versão 11.80.

**Solução.**

Segue abaixo a ordem de preço do produto para faturamento no Pedido de Venda:

1. **Contrato de Parceria(**FATA400) - **ADB\_PRCVEN**.
2. **Preço de Venda** POR **PRODUTO** (**MATA010**): **B1\_PRV1** - Preço Venda  
   *(OBS: Campos de Preço da SB5 - Complemento de Produtos não são utilizados no módulo Faturamento).*
3. **Preço de Venda** POR **TABELA de Preço** (**OMSA010**): **DA1\_PRCVEN** - Preço Venda (Necessário que a Tabela esteja Ativa e a Vigência no Item seja anterior ou igual à data base)
4. **Preço de Venda** POR **CLIENTE**: Registrar no Cadastro de Cliente a Tabela de Preço padrão para esse Cliente - **A1\_TABELA** - Tabela Preço
5. **Preço de Venda** POR **LOTE (MATA805**): **B8\_PRCLOT** (Necessário que a data base seja inferior ou igual à **B8\_DTVALID**).

**Saiba mais:**

**<https://tdn.totvs.com/pages/viewpage.action?pageId=393364250>**
