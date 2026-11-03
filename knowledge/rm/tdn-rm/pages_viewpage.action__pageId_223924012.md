---
content_hash: 39c3bdd1f8aa974b3f567cbdf9a1f08802bf38da39d510f824037421fdb70f1f
fetched_at: '2026-06-29T00:06:22.616883+00:00'
page_id: '223924012'
product: rm
source: tdn-rm
title: TTVTMK_DT_Alteração_Hora_Agendamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223924012
version: 4
---

# Alteração na Hora do Agendamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Agenda | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Sql Server e Oracle |
| **Tabelas Utilizadas:** | SZAGENDAMENTO |
| **Sistema(s) Operacional(is):** | Windows® |
| **Versões/Release:** | 12.1.9 |

## Descrição

Ajuste no sistema para que ao agendar um paciente o campo **Hora** esteja em branco e não permitir que o campo **Hora Chegada** seja preenchido, obrigando preenchimento do campo **Hora** antes de gravar e não permitir alterar o campo **Hora Chegada**.

## Procedimento para Utilização

1. Acesse **Atendimento / Agendamento / Agenda de Atendimentos**.
2. Selecione uma agenda.
3. Clique em "**Encaixe**".
4. O campo "**Hora**" na tela de agendamento deverá estar em branco.
5. O campo **"Hora Chegada"** não pode ser alterado.
6. Como é um campo obrigatório, se o usuário não preenchê-lo, o sistema irá emitir um aviso e não permitirá salvar o agendamento.
