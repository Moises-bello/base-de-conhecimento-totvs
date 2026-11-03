---
content_hash: c3aa072142c07c0a9f63e5f66c78760eb6f7e09278e3fe14fdc4f04a2c9bdaf8
fetched_at: '2026-06-29T00:09:54.197898+00:00'
page_id: '442960550'
product: rm
source: tdn-rm
title: DSAUGHCOM-1773 Validação da cobertura de diárias e seleção das diárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=442960550
version: 2
---

# Validação da cobertura de diárias e seleção das diárias

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Mudança de Leito | Mudança de Leito | |
| **Cadastros Iniciais:** | Leitos e Registro de Atendimento (Interno). |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZCONDCONTRATDIARIA, SZCONDCONTRATPROIBIDO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Coberturas e restrições de diárias na transferência de leito.

## Procedimento para Utilização

No processo de Mudança de Leito, caso o leito selecionado para a transferência não seja um leito de Centro Cirúrgico e a diária deste leito seja PROIBIDA pelas condições contratuais com o convênio do paciente, o usuário será informado e impedido de realizar a transferência.

Caso a diária do leito selecionado para a transferência não seja coberta pelo convênio, o usuário deverá selecionar, dentre as diárias cobertas, a diária que será utilizada como base para o cálculo da diferença de diárias, bem como informar o responsável por esta diferença.
