---
article_id: 4405226438551
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0beb3b284153af7fb11dc9fe834189238ab2b4c78f752a0bd76641ac2e789862
fetched_at: '2026-06-28T22:38:38.397322+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Nota sobre
  o uso do custo do produto como preço de venda do pedido
type: support-article
updated_at: '2021-07-29T14:37:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405226438551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-Nota-sobre-o-uso-do-custo-do-produto-como-pre%C3%A7o-de-venda-do-pedido
---

**Dúvida**  
Nota sobre o uso do custo do produto como preço de venda do pedido (**MATA410**).  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões  
  
**Solução**

O módulo de Faturamento não utiliza o custo de produto como preço de venda no pedido de venda(**MATA410**) diretamente, por padrão de sistema, faturamento não calcula custo e não tem opção para buscar no momento de inserção do produto no pedido.

Hoje, ou preço de venda terá que se efetuado por preço de lista, seja no preço de venda do produto (**MATA010**) ou preço de tabela de preço (**OMSA010**) ou será inserido manualmente.

Já no faturamento do pedido,  o sistema até calcula o custo no **d2\_custo**(1 a 5), desde que tenha o valor do campo **b2\_cm** que será multiplicado pela quantidade vendida (**d2\_quant**), mas esse cálculo não influenciará no preço de venda.  
  
Uma possibilidade  é tentar utilizar uma tabela de preço no pedido com uso de reajuste por planilha de formação de preço, onde na planilha de formação, existem vários cálculos para chegar ao melhor preço para venda e podendo trabalhar com custo do produto.

Para dúvidas sobre planilha de formação(**MATC010**), contate a equipe de Estoque para melhor orientação.

Saiba mais:

**[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Rotina Formação de Preço (MATC010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022184251-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-Forma%C3%A7%C3%A3o-de-Pre%C3%A7o-MATC010-)**

**[MP- FAT - Reajuste de Tabela de Preço por Planilha de Formação de Preço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333411-MP-FAT-Reajuste-de-Tabela-de-Pre%C3%A7o-por-Planilha-de-Forma%C3%A7%C3%A3o-de-Pre%C3%A7o)**

**[MP-FAT-Como-o-sistema-alimenta-o-campo-D2-CUSTO1-no-faturamento-da-nota-MATA461-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044967593-MP-FAT-Como-o-sistema-alimenta-o-campo-D2-CUSTO1-no-faturamento-da-nota-MATA461-)**

**[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito de utilização da rotina MATA320 - Custo Standard/Custo de Reposição - B1\_CUSTD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-da-rotina-MATA320-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o-B1-CUSTD)**
