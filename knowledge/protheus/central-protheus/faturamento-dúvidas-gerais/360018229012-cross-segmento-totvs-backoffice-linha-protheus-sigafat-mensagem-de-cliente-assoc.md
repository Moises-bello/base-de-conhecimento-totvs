---
article_id: 360018229012
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d012785df2534768a0ac1e6444f85403207d176f449830660b8067807bc3a07b
fetched_at: '2026-06-28T22:38:28.593414+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Mensagem de
  cliente associado ao tentar excluir o cadastro
type: support-article
updated_at: '2023-07-05T12:58:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018229012-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Mensagem-de-cliente-associado-ao-tentar-excluir-o-cadastro
---

**Dúvida**

Ao excluir o cliente, surge a mensagem: "Este cliente está associado a uma estrutura de clientes e não poderá ser excluído".

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

No Cadastro de Cliente, clique em alterar, vá na aba de vendas, campo **A1\_GRPVEN** (GRP.Vendas),  e limpe o código gravado neste campo, somente desta forma, o cadastro poderá ser excluído e a mensagem em questão deixará de ocorrer.

Valide se este cadastro já não foi utilizado em alguma operação do sistema, por que aí, também será permitida sua exclusão a fim de manter integridade sistêmica.
