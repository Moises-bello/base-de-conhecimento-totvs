---
content_hash: c07b48ee9d53acd6fa7f3b8ce9fced0c354dc14769fde00fc31d142a7e722860
fetched_at: '2026-06-29T00:08:29.456069+00:00'
page_id: '272145588'
product: rm
source: tdn-rm
title: 208553 MCP-1878 ER Cadastro Redução Z
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272145588
version: 101
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Redução Z |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado/Ticket** | 208553 | | |
| **País** | Brasil | | |

   

## Objetivo

Implementação para alterar a nomenclatura dos campos 'Cupom Inicial' e 'Cupom Final' da Redução Z para 'COO Inicial' e 'COO Final'. 

Esse procedimento não afeta o processo do cliente já que a alteração foi apenas na nomenclatura dos campos, visto que o conteúdo dos mesmos já era automaticamente preenchido (e posteriormente escriturado para o TOTVS Gestão Fiscal) com os dados do COO inicial e final da Redução.

## Definição da Regra de Negócio

Em ***"Cadastros | Fiscais | Mais | Redução Z | Valores Financeiros"***, ao criar uma nova Redução Z ou ao editar uma já existente, o usuário poderá verificar a modificação no nome dos campos.

Veja abaixo:

 

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Redução | Alteração | Cadastros | Fiscais | Mais | Redução Z | Valores Financeiros | Conforme descrito nesse documento |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
