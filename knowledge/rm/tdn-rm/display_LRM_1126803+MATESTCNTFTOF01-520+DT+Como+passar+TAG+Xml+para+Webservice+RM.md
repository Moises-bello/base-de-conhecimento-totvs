---
content_hash: 630d523b0ef78053cc659104837ce823d6655b985f7a525875e5a51f44da0962
fetched_at: '2026-06-29T00:08:40.777989+00:00'
page_id: '286504565'
product: rm
source: tdn-rm
title: 1126803 MATESTCNTFTOF01-520 DT Como passar TAG Xml para Webservice RM
type: documentation
url: https://tdn.totvs.com/display/LRM/1126803+MATESTCNTFTOF01-520+DT+Como+passar+TAG+Xml+para+Webservice+RM
version: 104
---

# INCLUIR/ALTERAR PRODUTO VIA WEBSERVICE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Incluir Produto via WebService. |
| **Situação/Requisito:** | Ao utilizar a inclusão de Produto via WebService, não está sendo aplicado a regra referente ao parâmetro de Produto: **Complementa o último nível do código do produto**. |
| **Solução/Implementação:** | Quando for realizada a inclusão/alteração de Produto via WebService serão aplicadas as mesmas regras de quando utilizado a tela do sistema. São elas:   * Respeitar a regra referente ao parâmetro de Produto **Complementa o último nível do código do produto**; * Quando o **Código do Produto** estiver preenchido e o **Número do Produto no Fabricante** não foi informado, será copiado a informação do Código do Produto para o campo Número do Produto no Fabricante; * O campo **Código Reduzido** será alterado somente quando o parâmetro de Produto **Usa Código Reduzido** for igual a **Não Sequencial**. |
| **Conversores e Parâmetros:** | Desnecessário. |
| **Tickets relacionados:** | 1126803. |
| **Requisito:** | Cadastro de Produtos/Serviços (EstPrdAction) |

divs
