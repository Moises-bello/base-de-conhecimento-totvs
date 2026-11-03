---
content_hash: 519505d349dcd10c86e304c143df009150fbb35eb0bfd52eb15c1f3375ff9b6a
fetched_at: '2026-06-29T00:08:42.286872+00:00'
page_id: '287068296'
product: rm
source: tdn-rm
title: ER SAUHRM03-967 Migração Registro de atendimentos - Informações de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287068296
version: 101
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar - RM | **Módulo** | Registro de Atendimento |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_HRM\_MIGRACAO | **IRM/EPIC1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM03-18 |
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM03-892 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM03-967 |
| **Chamado/Ticket2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Este documento tem como objetivo especificar o requisito de consultar as informações de contrato do plano e/ou sub-plano do convênio.

## Definição da Regra de Negócio

**RN001 - Aba Informações de Contrato** 

Criar aba no Registro de Atendimento com as informações de contrato do plano e/ou sub-plano do convênio.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Aba Informações de Contrato | [Criação] | Central de Atendimento (tela principal - pesquisar via Action na nova MDI) / Aba Dados do Atendimento - Sub-aba Informações de Contrato | **RN001** |

**Exemplo de Aplicação:**

* Acessea **Central de Atendimentos.**
* Localize um paciente.
* Acesse a aba **Dados do Atendimento** selecionando um **atendimento existente.**
* Acesse a sub-aba **Informações de Contrato.**
* Visualize as informações (se existir).

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
