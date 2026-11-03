---
content_hash: 18f8f2708a33ee436bba8e5508bdc6b607c046c87fc4a0a3139cee00cb14828f
fetched_at: '2026-06-29T00:06:07.060220+00:00'
page_id: '201734774'
product: rm
source: tdn-rm
title: DT_Bloqueio_de_recursos_em_conflito_na_Agenda_de_Cirurgia
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Bloqueio_de_recursos_em_conflito_na_Agenda_de_Cirurgia
version: 12
---

# **Bloqueio de recursos em conflito na agenda de cirurgia/Aviso de sala bloqueada no mapa da agenda de cirurgia**

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Agenda de cirurgia |
| **Rotina:** | Agenda de cirurgia |
| **Cadastros Iniciais:** | Atendimento / Agendamento / Bloqueio de sala do bloco cirúrgico |
| **Requisito (ISSUE):** | [PCREQ-6795](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6795 "PCREQ-6795") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

O objetivo desta implementação é:

* Exibir uma mensagem ao escolher os recursos a serem usados na cirurgia que indicará se aquele recurso escolhido está sendo utilizado em outra sala durante o horário escolhido e possibilitar a escolha de agendar mesmo assim, cancelar ou escolher outro recurso ou horário diferente para a cirurgia.
* Exibir um agendamento em vermelho no mapa da agenda de cirurgia para identificar o bloqueio da sala.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da release 12.1.7

1. Aplique o pacote da release 12.1.7 e execute o agendamento de exames pela assistente.

## Procedimento para Utilização

Bloqueio de recursos:

1. Acesse a **Agenda de Cirurgias**.
2. Crie um novo agendamento e preencha os dados da tela principal.
3. Acesse a aba **Recursos** e insira um novo recurso. Selecione o recurso e a quantidade.
4. Clique em **OK**, o sistema realizará a validação se existe conflito de recursos x horários e exibe uma mensagem/pergunta.
5. Caso clique em **Sim** o sistema agendará mesmo com conflito.
6. Caso clique em Não, o sistema permanece na tela para escolha de outro recurso ou quantidade.

**Bloqueio de sala:**

1. Acesse **Agendamento / Bloqueio de sala do bloco cirúrgico**.
2. Cadastre um novo bloqueio para uma sala.
3. Acesse a agenda de cirurgia e em seguida acesse o **Mapa da Agenda**.
4. No **Mapa**, será exibido um agendamento "falso" em vermelho indicando o bloqueio da sala.
