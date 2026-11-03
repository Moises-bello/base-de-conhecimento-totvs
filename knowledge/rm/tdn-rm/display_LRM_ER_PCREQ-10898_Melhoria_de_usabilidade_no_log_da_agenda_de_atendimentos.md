---
content_hash: 325fec86bc8276e83abcad748c42e58c7e0e4e17e87ee1479c8fd5237a70a279
fetched_at: '2026-06-29T00:08:07.759932+00:00'
page_id: '237388457'
product: rm
source: tdn-rm
title: ER_PCREQ-10898_Melhoria_de_usabilidade_no_log_da_agenda_de_atendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10898_Melhoria_de_usabilidade_no_log_da_agenda_de_atendimentos
version: 113
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM SAÚDE |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10841](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10841 "PCREQ-10841") |
| **Requisito** | * [PCREQ-10898](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10898 "PCREQ-10898") | **Subtarefa** | * [SAU\_DEV-4772](http://jira.totvs.com.br/browse/SAU_DEV-4772) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

    O Objetivo deste documento é a especificação do requisito de modificação da tela de log da agenda de atendimentos para que a mesma passe a utilizar a grid padrão dos produtos RM, com todos os controles e funcionalidades disponíveis.

## Definição da Regra de Negócio

**R****N001**

* No log da agenda de atendimentos, alterar a tela existente, removendo a grid atual e adicionando a grid padrão dos produtos RM.
* Os dados apresentados na tela devem permanecer os mesmos, para minimizar o impacto para os clientes que já utilizam esta tela.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Log da Agenda de Atendimentos | Alteração | Atendimento > Agendamento > Agenda de Atendimentos > Log da Agenda de Atendimentos | **RN001** |

**Exemplo de Aplicação:**

* Acesse o menu "**Atendimento > Agenda > Agenda de Atendimentos**";
* Selecione uma agenda qualquer e clique em uma data onde existam registros de atendimentos;
* Clique no botão , posicionado no centro da tela;
* Verifique se a tela está com a grid padrão dos produtos da linha RM, com todas as funcionalidades.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
