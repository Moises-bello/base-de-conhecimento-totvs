---
content_hash: 1fa7fcdc8e9e627ef818af24af06e90f252b88b3cf579b27df074951cb96f037
fetched_at: '2026-06-29T00:08:23.037265+00:00'
page_id: '269442853'
product: rm
source: tdn-rm
title: ER_SAUHRM02-328_Bloqueio_de_agendamentos_simultaneo
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM02-328_Bloqueio_de_agendamentos_simultaneo
version: 118
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | GESTÃO HOSPITALAR - RM | **Módulo** | Atendimento / Agenda de Atendimentos |
| **Segmento Executor** |  | | |
| **Projeto1** | SAUHRM02 | **IRM1** | [SAUHRM02-346](http://jiraproducao.totvs.com.br/browse/SAUHRM02-346) - Melhorias do Hospital Oswaldo Cruz BANCO DE IDEIAS |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-328 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-407 |
| **Chamado2** |  | | |
| **País** | ( **X** ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Esta especificação tem como objetivo detalhar a melhoria à ser implementada na funcionalidade de Agenda de Atendimentos do produto TOTVS Gestão Hospitalar. A melhoria consiste-se em bloquear os horários de agendamento no início do processo de agendamento de atendimento. O objetivo é impedir a tentativa de agendamentos em horários simultaneamente e consequentemente a ocorrência da perda das informações preenchidas durante o processo de agendamento, com isso agregando uma melhoria operacional ao produto, principalmente para equipes onde há grande fluxo de utilização simultânea da Agenda de Atendimentos do TOTVS Gestão Hospitalar.

## **Definição da Regra de Negócio**

**RN001**- Na inclusão/alteração de um novo agendamento, verificar se o horário selecionado não encontra-se ocupado na tabela de controle de agendamentos simultâneo, em caso de selecionar um horário ocupado, exibir mensagem de agendamento em andamento.

**RN002**- Na inclusão/alteração de um novo agendamento, inserir um registro na tabela de controle de agendamentos simultâneo. Não permitindo o agendamento no mesmo horário, exibindo uma mensagem de que já existe agendamento em andamento. Após a efetivação do agendamento, excluir o registro da tabela de controles de agendamentos simultâneo.

**RN003**- No caso do cancelamento do processo de agendamento de atendimento [RN001], excluir o registro da tabela de tabela de controle de agendamentos simultâneo, para liberação do horário de agendamento.

**RN004**- No processo de cópia de agendamento, ao colar o agendamento previamente copiado, executar RN001 e posteriormente RN002 e RN003.

**RN005**- No processo de Agendamento seriado realizar as validações da seguintes RNs: RN001, RN002, RN003.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Agenda de Atendimentos | [Alteração] | Atendimento / Agendamento / Agenda de Atendimentos | RN001, RN002 |
| Cancelamento do Agendamento | [Alteração] | Atendimento / Agendamento / Agenda de Atendimentos / Horário de Agendamento\* / Cancelar | RN003 |
| Copia de Agendamento | [Alteração] | Atendimento / Agendamento / Agenda de Atendimentos / Registro de Agendamento\* / Copiar-Colar Agendamento | RN004 |
| Agendamento Seriado | [Alteração] | Atendimento / Agendamento / Agenda de Atendimentos / Registro de Agendamento\* / Agendamentos seriados | RN005 |

*\*Selecionar um Registro*

***Exemplo de Aplicação:***

* *Evitar a perda das informações do paciente quando o registro for salvo e o horário já estiver ocupado.*

***Tabelas Utilizadas***

* SZAGENDAMENTO - Agendamento de atendimentos
* SZAGENDAMENTOSIMULT- Controle de agendamentos simultâneo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
