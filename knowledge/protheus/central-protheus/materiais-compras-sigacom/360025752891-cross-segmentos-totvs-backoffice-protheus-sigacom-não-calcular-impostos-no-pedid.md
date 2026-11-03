---
article_id: 360025752891
category: Materiais - Compras (SIGACOM)
content_hash: d2c1599a0cd778fd8f087069c015b39fe55395d59875b5ca462ea064aa1ec158
fetched_at: '2026-06-28T22:41:20.256627+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não calcular Impostos
  no Pedido de Compras
type: support-article
updated_at: '2023-12-14T19:38:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025752891-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-calcular-Impostos-no-Pedido-de-Compras
---

**Dúvida**Impostos no Pedido de Compras

**Ambiente**Microsiga Protheus – Compras – A partir da versão 11.80

**Solução**

1. Como não calcular impostos no Pedido de Compras ?

Na inclusão do pedido de compras para não calcular os impostos automaticamente (ICMS e IPI), deverá configurar o parâmetro MV\_INITES = .T. (*True*).

Exemplo:

.T. = Indica que até informar o código do TES, os campos que indicam se haverá cálculo do ICMS, cálculo do IPI, geração do livro ICMS, geração do livro IPI, assumirá o valor N (não serão calculados/gerados).

.F. = continuará a proceder da forma atual, ou seja, os campos que indicam se haverá cálculo do ICMS, cálculo do IPI, gerações do livro ICMS, geração do livro IPI, assumem o valor S.

      2. O Sistema calcula Impostos quando incluído um Pedido com moeda diferente de Real ? Qual o impacto no Relatório de Pedido de Compras (MATR110) ?

Ao incluir um Pedido de Compras, utilizando uma moeda diferente de Real, mesmo que haja alíquota de ICMS e IPI informados no cadastro do Produto, as informações referentes as alíquotas não serão apresentadas no relatório de Pedido de Compras (MATR110), as alíquotas são apresentadas somente após a inclusão do Documento de Entrada referenciando esse Pedido.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
