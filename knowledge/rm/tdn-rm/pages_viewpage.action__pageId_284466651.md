---
content_hash: e8d347370dd317f28d79df3607eeeafc52ed5662c7fcb1888e49b2ef92aad2f4
fetched_at: '2026-06-29T00:08:36.181563+00:00'
page_id: '284466651'
product: rm
source: tdn-rm
title: ER SAUHRM02_1162 Disponibilizar a opção de Vincular Unidade de Atendimento
  - Cadastro de Produtos/Informações do TOTVS Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284466651
version: 105
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
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1125 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1162 |
| **Chamado/Ticket2** | [Ticket #866546](https://totvssuporte.zendesk.com/agent/tickets/866546 "Open ticket in Zendesk Support") | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Este documento tem como objetivo especificar o requisito de vínculo das unidades de atendimento com produto. 

Este requisito permitirá informar as unidades de atendimento, no cadastro do produto, que irão utilizá-lo. Dessa forma, ao realizar uma prescrição, elaborar uma conta e movimentar estoque, só será possível visualizar os produtos que terão vínculo com a unidade de atendimento em questão. 

A utilização destes filtros dependem de parâmetro ativado.

### (Obrigatório)

## Definição da Regra de Negócio

**RN001 - Parametrização**

Será criado uma parâmetro chamado *"Filtra Produtos por Unidade de Atendimento"*para que se ative o filtro por unidades de atendimento.

**RN002 - Vínculo das Unidades de Atendimento**

Será disponibilizada uma nova aba no cadastro do produto, visível somente se parametrização ativada, para que se selecione quais unidades de atendimento poderão utilizar o produto em questão.

**RN003 - Utilização do Filtro**

Na Elaboração de Contas, na Prescrição Médica (realizada pelo Prontuário Eletrônico) e na Movimentação de Estoque, ao buscar materiais ou medicamentos será possível selecionar itens permitidos para a unidade de atendimento selecionada.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parametrização | [Envolvida] | Opções -> Parâmetros / Parâmetros Gerais - aba Estoques | **RN001** |
| Vínculo das Unidades de Atendimento | [Alteração] | Cadastros -> Estoques / Produto / Anexo: Produto - Informações RM Saúde | **RN002** |
| Utilização do Filtro | [Alteração] | Prontuário -> aba Prescrição Médica  Estoques -> Movimentação de Estoque  Faturamento -> Particular e Convênios / Lançamentos na Conta do Paciente | **RN003** |

**Exemplo de Aplicação:**

* Acesse **Opções / Parâmetros / Parâmetros Gerais,**aba Estoques e marque o parâmetro *"Filtra Produtos por Unidade de Atendimento" .*
* Acesse Cadastros / Estoques / Produto.
* Selecione um produto.
* Acesse Anexos / Produto - Informações RM Saúde
* Na aba *"Unidades de Atendimento vinculadas ao Produto"*, será possível selecionar quais unidades de atendimento poderão utilizar o produto que se está configurando.
* Ao realizar uma prescrição médica, elaborar uma conta ou movimentação de estoque, ao pesquisar produtos, somente será possível encontrar os itens que estão permitidos para a unidade de atendimento em questão.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
