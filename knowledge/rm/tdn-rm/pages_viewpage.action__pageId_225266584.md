---
content_hash: c89cf895903a4c73a11bc8f7c92bc161fd389f4b5de2c965162789cc03687e9c
fetched_at: '2026-06-29T00:06:26.460081+00:00'
page_id: '225266584'
product: rm
source: tdn-rm
title: ER_PCREQ-9952_Restrições_por_Exame_Dia_Horário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=225266584
version: 122
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Saúde |
| **Projeto1** | [PDR\_SAU\_V12](http://jira.totvs.com.br/browse/SAU_DEV) | **IRM1** | [PCREQ-9841](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9841 "PCREQ-9841") |
| **Requisito1** | [PCREQ-9952](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9952 "PCREQ-9952") | **Subtarefa1** | SAU\_DEV-4138 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 Restringir o agendamento de exames por dia e horário

### (Obrigatório)

## Definição da Regra de Negócio

Criar uma aba nova no cadastro de exames para que seja possível informar dias da semana e horários para que o exame possa ser agendado. Quando cadastramos pelo menos um registro, no dia escolhido o sistema permitirá o agendamento apenas na faixa horária definida. Fora dessa faixa não será permitido agendar o exame no dia da semana escolhido e o sistema exibirá uma mensagem no caso de uma tentativa de agendamemto. Nos outros dias da semana, o sistema permitirá o agendamento em qualquer horário e caso seja necessário restringir horários, será preciso efetuar o devido cadastro para este dia.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
