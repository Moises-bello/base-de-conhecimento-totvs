---
content_hash: a51f9aa1cb7dd1c4c915213b9a57703f3430715e00b527b4bd9a29e83e3d733b
fetched_at: '2026-06-29T00:08:14.070782+00:00'
page_id: '244440243'
product: rm
source: tdn-rm
title: ER_SAUHRM01-397_Registro_de_Atendimento_Externo_Idade_do_Paciente
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM01-397_Registro_de_Atendimento_Externo_Idade_do_Paciente
version: 115
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAÚDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** | SAUHRM01 | **IRM** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-392 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-397 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-432 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 

Esta especificação tem como objetivo detalhar a nova melhoria à ser implementada no Registro de Atendimentos Externos e na Agenda de Atendimentos, para que o sistema informe a idade do paciente no formato que apresente a quantidade em Anos, Meses e Dias. Esta informação é motivada pela característica de pacientes pediátricos, onde o detalhamento da idade do paciente é importante.  

## Definição da Regra de Negócio

**RN001** - Apresentar a idade do paciente no Registro de Atendimentos no formato que apresente a quantidade em Anos, Meses e Dias.  
**RN002** - Apresentar a idade do paciente na Agenda de Atendimentos no formato que apresente a quantidade em Anos, Meses e Dias.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Registro de Atendimentos | [Alteração] | Atendimento / Pronto Atendimento/Ambulatório / Registro de Atendimentos Externos | RN001 |
| Agenda de Atendimentos | [Alteração] | Atendimento / Agendamento / Agenda de Atendimentos | RN002 |

***Exemplo de Aplicação:***

* Médicos podem acessar a idade precisa do pacientes pediátricos.

***Tabelas Utilizadas***

* + SZATENDIMENTO
  + SZAGENDAMENTO

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
