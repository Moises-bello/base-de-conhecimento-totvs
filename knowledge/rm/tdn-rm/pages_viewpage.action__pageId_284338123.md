---
content_hash: aa29ea59d6a34cab7e89f37662f429cf9883b8d381566484b04da7b473008786
fetched_at: '2026-06-29T00:08:36.078466+00:00'
page_id: '284338123'
product: rm
source: tdn-rm
title: ER SAUHRM02-1117 Tela de Posto de Enfermagem Painel de eletivos não abrir a
  tela do prontuário ao chamar paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284338123
version: 103
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Gestão Hospitalar - RM | **Módulo** | Painel de Eletivos |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_HRM1617 | **IRM/EPIC1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAU\_BACKLOG-1329 |
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1117 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1118 |
| **Chamado/Ticket2** | [Ticket #820955](https://totvssuporte.zendesk.com/agent/tickets/820955 "Open ticket in Zendesk Support") | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Permitir que o usuário apenas inicie o atendimento no Posto de Enfermagem do Painel de Eletivos, sem que seja necessário abrir o Prontuário do Paciente.

### Definição da Regra de Negócio

* *RN001: Ao realizar um duplo clique  no registro do Posto de Enfermagem do Painel de Eletivos, adicionar no popup o botão Confirmar e Abrir o Prontuário, que confirmará e iniciará o Atendimento e automaticamente abrirá o Prontuário do Paciente. (Protótipo 1)*
* *RN002: *Ao realizar um duplo clique  no registro do Posto de Enfermagem do Painel de Eletivos, adicionar no popup o botão Confirmar, que confirmará e iniciará o Atendimento. *(Protótipo 1)***

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Painel de Atendimentos Eletivos | Painel de Atendimentos Eletivos [Alteração] | Atendimento / Pronto Atendimento/Ambulatório / Painel de Atendimentos Eletivos | RN001 |
| Painel de Atendimentos Eletivos | Painel de Atendimentos Eletivos [Alteração] | Atendimento / Pronto Atendimento/Ambulatório / Painel de Atendimentos Eletivos | RN002 |

***Exemplo de Aplicação:***

* Permitir que o usuário apenas inicie o atendimento no Posto de Enfermagem do Painel de Eletivos, sem que seja necessário abrir o Prontuário do Paciente.

## Protótipo de Tela

**Protótipo 01**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
