---
content_hash: 24e7a21a426fba08bb115a092253bf77f3b95939a7ad26a8fd068ef5138c24c6
fetched_at: '2026-06-29T00:10:36.165873+00:00'
page_id: '531030322'
product: rm
source: tdn-rm
title: Reprocessamento de Repasse
type: documentation
url: https://tdn.totvs.com/display/LRM/Reprocessamento+de+Repasse
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Utilização**

SumárioVisão Geral

## **01. VISÃO GERAL**

Esta função é utilizada para reprocessar todos os itens de débitos já repassados aos Prestadores quando o valor de repasse nos Critérios de Repasses é alterado.

Utilização

## **02. UTILIZAÇÃO**

Para chegar até está tela, devemos ir em **Faturamento > Gestão de Repasse > Outros > Reprocessamento de Repasse.**  
Nesta tela, diversos campos estão disponíveis para que sejam aplicados filtros no reprocessamento, como o período em que os repasses foram realizados e a Unidade de Faturamento onde ocorreram.

1. Caso um Convênio seja selecionado, os itens serão pesquisados nas Tabelas definidas nas Condições Contratuais com os Convênios.
2. Informe o nome do Prestador ou selecione "Todos os Prestadores" para incluir todos os destinatários dos repasses.
3. Indique a remessa para a qual deseja reprocessar os repasses já efetuados.

Por fim, selecione uma das opções abaixo para definir o comportamento do reprocessamento.

* + **Reprocessar apenas itens de débitos JÁ repassados**: Reprocessa itens que já foram repassados a um determinado Prestador e cujo Critério de Repasse foi alterado.
  + **Processar apenas itens de débitos NÃO repassados**: Processa itens lançados para um determinado Prestador, mas que não possuíam Critérios de Repasse definidos.
  + **Reprocessar TODOS os itens de débitos (incluindo os que já foram repassados)**: Combina as duas opções anteriores, reprocessando tanto itens já repassados quanto os não repassados anteriormente.
