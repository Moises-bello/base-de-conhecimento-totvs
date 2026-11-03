---
content_hash: 911530134dc0811e7c25eb5a18077fca75265ee63578cb951d0856e7a3ef60e2
fetched_at: '2026-06-29T00:06:05.581956+00:00'
page_id: '201724735'
product: rm
source: tdn-rm
title: DT_Conflitos_de_Horários_em_Agendamento_de_Exames_Através_do_Assistente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201724735
version: 8
---

# Agendamento de Exames Através do Assistente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | Agendamento de exames com Assistente |
| **Cadastros Iniciais:** | Cadastro de Agendas, Cadastro de Exames |
| **Requisito (ISSUE):** | [PCREQ-6795](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6795 "PCREQ-6795") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | SZAGENDAMENTO |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

Esta implementação consiste em minimizar os conflitos de horários gerados por consultas concorrentes no assistente de agendamentos de exames.

Após o sistema exibir os horários disponíveis para os exames selecionados, o sistema passa a verificar a disponibilidade do horário selecionado. Para finalizar o agendamento é necessário finalizar o processo. Quando ocorrer conflito as reservas deverão ser canceladas.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da release 12.1.7

1. Aplique o pacote da release 12.1.7 e execute o agendamento de exames pela assistente.

## Procedimento para Utilização

1. Acesse a agenda de atendimentos.
2. Selecione o ícone Agenda Exames.
3. Informe os dados do agendamento.
4. Selecione os exames a serem agendados.
5. Selecione os dias da semana que preferir.
6. Diante dos horários exibidos, marque os de sua preferência.
7. Selecione um horário que já tenha sido utilizado por outro usuário.
8. Feche o assistente e verifique a mensagem de que o processo será cancelado.
