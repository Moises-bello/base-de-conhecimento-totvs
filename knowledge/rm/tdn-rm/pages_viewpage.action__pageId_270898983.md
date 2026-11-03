---
content_hash: 5df7a35eed56f59c5691dfa6b67e54c9640f68b1155d372c08f9443974e095b6
fetched_at: '2026-06-29T00:08:24.614027+00:00'
page_id: '270898983'
product: rm
source: tdn-rm
title: ER_SAUHRM02-539_Alteração_do_campo_Atividade_da_agenda_quando_estiver_em_período_de_retorno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270898983
version: 112
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | GESTÃO HOSPITALAR RM | **Módulo** | Agendamento / Agenda de Atendimentos |
| **Projeto1** | SAUHRM02 | **IRM1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-486 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-485 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-539 |
| **País** | ( **X** ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação

## Objetivo

 Esta especificação tem como objetivo detalhar a melhoria à ser implementada na funcionalidade de Agenda de Atendimentos do produto TOTVS Gestão Hospitalar. A melhoria consiste-se em aplicar o status de Retorno nos Atendimentos automaticamente com base na parametrização do Atividades da Agenda e do tempo parametrizado nas Condições Contratuais dos Convênios.

## Definição da Regra de Negócio

**RN001**- Parametrizar a Atividade da Agenda correspondente ao status de Retorno nos Parâmetros Gerais - Registro e Controle II.

**RN002**- Parametrizar a Atividade do Registro de Atendimento correspondente ao status de Retorno nos Parâmetros Gerais - Registro e Controle II.

**RN003**- Ao acessar um registro da Agenda de Atendimentos, se o mesmo estiver dentro do período de retorno, conforme a parametrização da RN001, informar o status correspondente automaticamente.

**RN004**- Ao acessar um registro da Agenda de Atendimentos e Acessar o Registro de Atendimento pelo Agendamento, se o mesmo estiver dentro do período de retorno, conforme a parametrização da RN002, informar o status correspondente automaticamente.

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Pârametros Gerais | [Criação] | Parâmetros / Parâmetros Gerais / Registro e Controle II | RN001 / RN002 |
| Agenda de Atendimentos | [Alteração] | Atendimentos / Agendamento / Agenda de Atendimentos | RN003 |
| Registro de Atendimentos Externo | [Alteração] | Atendimentos / Pronto Atendimento / Registro de Atendimentos Externo | RN004 |

***Exemplo de Aplicação:***

* *Visualizar que o Atendimento está dentro do período de retorno automaticamente, sem a necessidade de editar o registro.*

***Tabelas Utilizadas***

* *SZAGENDAMENTO – Agenda de Atendimentos*
* **SZATENDIMENTO – Registro de Atendimentos**

divs

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
