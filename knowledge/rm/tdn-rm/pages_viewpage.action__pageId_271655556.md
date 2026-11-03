---
content_hash: a29753f4e4785cc4bd602cff8cbb35b68fc8cb1e9674cf585086b3ecbc437525
fetched_at: '2026-06-29T00:08:28.033847+00:00'
page_id: '271655556'
product: rm
source: tdn-rm
title: 95869 MCP-399 ER NF-e - Resolução Nº 1644/06 ANTT - Regulamento do Transporte
  Terrestre de Produtos Perigosos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271655556
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Cadastros | Produtos | Características |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado** | 95869 | | |
| **País** | Brasil | | |

## 

## Objetivo

Esta melhoria tem como objetivo atender à Resolução de Nº 1644/06 da Agência Nacional de Transportes Terrestres (ANTT) que em seu item 5.4.1.2 determina:

"Se um documento fiscal listar tanto produtos perigosos quanto não perigosos, os produtos perigosos devem ser relacionados primeiro, ou ser enfatizados de outra maneira."

## Definição da Regra de Negócio

Para atendimento ao item  5.4.1.2 da Resolução de Nº 1644/06 da ANTT, que determina que no documento fiscal os produtos perigosos sejam relacionados em primeiro lugar, ou enfatizados de outra maneira, será criado no cadastro de Produtos em (***Cadastros | Produto***), na aba ***Detalhes | Características***, dentro do group box ***Gerais***, o campo:

* Produto Perigoso - Resolução ANTT 1644/06 (TPRODUTO.PERIGOSO).

Assim, os itens que tiverem sido definidos em seu cadastro como Produto Perigoso serão enfatizados **em negrito e sublinhado** no relatório da DANFE, já os demais itens serão emitidos normalmente, ou seja, sem nenhum destaque.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Produto | Alteração | Cadastros | Produto | Conforme definições constantes deste documento |

## Tabelas Utilizadas:

* TPRODUTO - Definições dos Produtos.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
