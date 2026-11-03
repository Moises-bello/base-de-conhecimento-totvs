---
article_id: 360025973732
category: Materiais - Compras (SIGACOM)
content_hash: 9123ba80b4d9dababdcf1ea2a50b0a46e653cd81d09bf6a9d19dc25e8f7c4f8f
fetched_at: '2026-06-28T22:41:07.533937+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como alterar a condição
  de pagamento do CT-e quando importado pelo Totvs Colaboração ?
type: support-article
updated_at: '2022-05-16T22:15:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025973732-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-alterar-a-condi%C3%A7%C3%A3o-de-pagamento-do-CT-e-quando-importado-pelo-Totvs-Colabora%C3%A7%C3%A3o
---

**Dúvida**Como alterar a condição de pagamento do CT-e quando importado pelo Totvs Colaboração ?

**Ambiente**Protheus – SIGACOM – A partir da versão 12.1.17

**Solução**

O sistema possui o parâmetro **MV\_XMLCPCT** que através dele informamos qual será condição de pagamento para documento CT-e, porém quando cada fornecedor tem uma condição de pagamento.

Exemplo:

Para o fornecedor 01 é utilizada a condição 020(a vista)

Para o fornecedor 02 é utilizada a condição 030(parcelamento)

Como o parâmetro permite apenas uma condição de pagamento para alteração da Condição de Pagamento deve-se utilizar o ponto de entrada **A116TECT**.

***Saiba Mais:***

[A116TECT - Altera TES e Condição de pagamento para CTe](http://tdn.totvs.com/pages/releaseview.action?pageId=51250511)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
