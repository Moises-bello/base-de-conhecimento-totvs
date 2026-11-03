---
content_hash: 1a79294934b6151ef1d523de8d853dfc70bb291748a61a28a47a493f15813ca6
fetched_at: '2026-06-29T00:08:42.927447+00:00'
page_id: '301173595'
product: rm
source: tdn-rm
title: ER SAUHRM03-1008 Migração Registro de Atendimento - Motivo de Pendência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301173595
version: 93
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar - RM | **Módulo** | Registro de Atendimento |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_HRM\_MIGRACAO | **IRM/EPIC1** | <http://jiraproducao.totvs.com.br/browse/SAUHRM03-18> |
| **Requisito/Story/Issue1** | <http://jiraproducao.totvs.com.br/browse/SAUHRM03-950> | **Subtarefa1** | <http://jiraproducao.totvs.com.br/browse/SAUHRM03-1008> |
| **Chamado/Ticket2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Este documento tem como objetivo especificar o requisito de validar o motivo de pendência quando houver documentos incompletos do paciente.

## Definição da Regra de Negócio

 **RN001 - Motivo de Pendência Obrigatório**

Sistema deve obrigar o preenchimento do Motivo de Pendência quando o campo "Documentos Completos" estiver desmarcado, caracterizando que algum documento não foi entregue.

**RN002 - Motivo de Pendência Não Obrigatório**

Sistema deve desabilitar o campo de Motivo de Pendência quando o campo "Documentos Completos" estiver marcado, caracterizando que todos os documentos foram entregues.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Motivo de Pendência | Alteração | Central de Atendimentos / Dados do Atendimento, campo Motivo de Pendência | **RN001** |
| Motivo de Pendência | Alteração | Central de Atendimentos / Dados do Atendimento, campo Documentos Completos | **RN002** |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
