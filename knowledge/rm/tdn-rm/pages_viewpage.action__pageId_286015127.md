---
content_hash: c019d1fa589348c6afbea61c102f919dbae98f11a837c7bf88ff9671f04b36c1
fetched_at: '2026-06-29T00:08:39.254728+00:00'
page_id: '286015127'
product: rm
source: tdn-rm
title: ER SAUHRM02-1307 Migração Registro de atendimentos - Adequação da tela principal
  apenas para Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286015127
version: 102
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar - RM | **Módulo** | Registro de Atendimento |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_HRM1617 | **IRM/EPIC1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-349 |
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1262 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1307 |
| **Chamado/Ticket2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Este documento tem como objetivo especificar o desenvolvimento da tela que englobará as diferentes seções do Registro de Atendimento que serão migradas, focando apenas na seção do paciente inicialmente.

## Definição da Regra de Negócio

**RN001 - Tela Principal (SauCentralAtendimentosAction)**

Desenvolver uma tela que centralize todas as seções a serem migradas do Registro de Atendimento, tanto externo quanto interno.

**RN002 - Seção Paciente**

Permitir localizar, incluir e editar o paciente a partir da tela principal.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Tela Principal | [Criação] | (pesquisar via Action na nova MDI) | **RN001** |
| Seção Paciente | [Envolvida] | Central de Atendimentos (tela principal) -> Aba Paciente | **RN002** |

**Exemplo de Aplicação:**

* Acessea **Central de Atendimentos.**
* Inclua um **novo paciente** e salve.
* Um novo paciente deverá ser **incluído com sucesso.**
* **Localize** um paciente já existente.
* Altere alguma informação e salve.
* A **alteração** deverá ser **salva com sucesso.**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
