---
content_hash: d8a845ad3dea02f4e9d663b4b5a843449dcb45016ba2f652cc1d9bfa7d296394
fetched_at: '2026-06-29T00:08:36.856865+00:00'
page_id: '284478777'
product: rm
source: tdn-rm
title: ER SAUHRM02-1193 Bloqueio de Sado de Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+SAUHRM02-1193+Bloqueio+de+Sado+de+Estoque
version: 99
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar - RM | **Módulo** | Prescrição Médica, Movimentação de Estoque, Elaboração de Contas |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_HRM1617 | **IRM/EPIC1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAU\_BACKLOG-1329 |
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1126 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1193 |
| **Chamado/Ticket2** | [Ticket #892201](https://totvssuporte.zendesk.com/agent/tickets/892201 "Open ticket in Zendesk Support") | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Este documento tem como objetivo especificar o requisito de filtrar itens que possuem saldo zerado no estoque. 

Dessa forma, o usuário, ao pesquisar um item, serão mostrados os itens que possuem saldo no estoque. Caso nenhum item seja retornado na pesquisa, uma mensagem será mostrada para o usuário.

## Definição da Regra de Negócio

**RN001 - Parametrização**

Será criado um parâmetro chamado "*Não exibe produtos sem saldo no estoque",*para que itens com saldo zerado no estoque não sejam mostrados nas pesquisas.

**RN002 - Utilização do Filtro**

Na Elaboração de Contas, na Prescrição Médica (realizada pelo Prontuário Eletrônico) e na Movimentação de Estoque, ao buscar materiais ou medicamentos, não serão retornados os itens que possuem saldo menor ou igual a zero.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parametrização | [Envolvida] | Opções -> Parâmetros / Parâmetros Gerais - aba Estoques | **RN001** |
| Utilização do Filtro | [Alteração] | Prontuário -> aba Prescrição Médica  Estoques -> Movimentação de Estoque  Faturamento -> Particular e Convênios / Lançamentos na Conta do Paciente -> aba MatMed | **RN002** |

**Exemplo de Aplicação:**

* Acesse **Opções / Parâmetros / Parâmetros Gerais,**aba Estoques e marque o parâmetro *"Não exibe produtos sem saldo no* estoque"
* Ao realizar uma prescrição médica, elaborar uma conta ou movimentação de estoque, ao pesquisar produtos, somente será possível encontrar os itens que estão **com saldo no estoque**.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
