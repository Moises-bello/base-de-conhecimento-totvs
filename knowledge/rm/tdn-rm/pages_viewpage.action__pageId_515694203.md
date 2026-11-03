---
content_hash: fe0b93d1f4b7553812ffe883f629107dadef40e3a338722fe3cb0673de63361c
fetched_at: '2026-06-29T00:10:27.018171+00:00'
page_id: '515694203'
product: rm
source: tdn-rm
title: DT Ajuste de transação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515694203
version: 4
---

# Ajuste de transação para pagamentos com cartão

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *BackOffice* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRAkey,summary,type,created,updated,due,assignee,reporter,priority,status,resolution0c783de1-186e-383b-975c-a1acd7d76cb5DEDUCONNECT-108 |
| **País(es):** | *BRA* |
| **Banco(s) de Dados:** | *SQL e ORACLE* |
| **Tabelas Utilizadas:** | *FINTEGRACAOCARTAO, FINTEGRACAOHISTORICO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Implementada melhoria no sistema para que o "Ajuste de transações" consiga realizar a comunicação com todos módulo de pagamento e realizar as atualizações necessárias no Financeiro.

## Procedimento para Configuração

1. Acesse **Serviços Globais | Segurança | Perfis,**edite o perfil do usuário logado e localize a permissão **[03.05.02] Ajuste de transações,** em seguida de permissão ao usuário.

## Procedimento para Utilização

1. Acesse o Menu Movimentações Bancárias | Cartão de Crédito/Débito, clique na opção **'Ajuste de transações'.**

**2.** Na tela de Histórico de Transações, também pode ser executado o processo para ajustar a transação selecionando a transação que deseja efetuar o ajuste.

**Importante:** Este processo é permitido agendamento.
