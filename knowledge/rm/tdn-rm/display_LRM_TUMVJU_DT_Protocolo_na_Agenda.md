---
content_hash: ca652525829edbe0ea19853c4154405ef5d799ce0feefc91c4948e7d2cac2af3
fetched_at: '2026-06-29T00:08:05.936394+00:00'
page_id: '236423459'
product: rm
source: tdn-rm
title: TUMVJU_DT_Protocolo_na_Agenda
type: documentation
url: https://tdn.totvs.com/display/LRM/TUMVJU_DT_Protocolo_na_Agenda
version: 116
---

# Número do protocolo no agendamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Agenda de Atendimento | |
| **Parâmetro(s):** | **Opções / Parâmetros / Parâmetros Gerais**, aba **Registro e Controle III,** parâmetro "Utiliza Protocolo no Agendamento". |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER e ORACLE |
| **Tabelas Utilizadas:** | SZAGENDAMENTO e SZLOGAGENDAMENTO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado parâmetro para que se utilize o protocolo na agenda ao marcar um atendimento, cancelar e pesquisar.

## Procedimento para Utilização

1. Acesse **Opções / Parâmetros / Parâmetros Gerais**, aba **Registro e Controle III** e marque o parâmetro "**Utiliza Protocolo no Agendamento**".
2. Acesse a Agenda de Atendimentos.
3. Selecione uma agenda disponível.
4. Ao realizar o agendamento e salvar, será exibido o número do protocolo e o mesmo ficará salvo nas observações do agendamento.
5. Ao excluir um agendamento, será exibido o protocolo e o mesmo ficará salvo nas observações do log de agendamento.
6. Ao realizar um agendamento seriado, ao final do processo será exibido o número do protocolo do primeiro agendamento.
7. Na pesquisa de atendimentos, foi implementado o campo para pesquisar pelo protocolo.

divs
