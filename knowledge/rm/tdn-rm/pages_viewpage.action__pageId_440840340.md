---
content_hash: 356dc4ccb7b949e03f7995909abfb6b88faa2aa8b9105bded6513e77e810af6b
fetched_at: '2026-06-29T00:09:53.515721+00:00'
page_id: '440840340'
product: rm
source: tdn-rm
title: DSAUGHCOM-1772 DT Histórico de Mudança de Leitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440840340
version: 2
---

# Histórico de Mudança de Leitos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Transferência de Leito | SauProcBedTransferAction. | |
| **Cadastros Iniciais:** | É necessário ter um Registro de Atendimento Interno (em aberto), e Leitos cadastrados no sistema. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZMUDANCALEITO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Este requisito tem como objetivo mostrar ao usuário todo o **Histórico de Mudança(s) de Leito(s)** realizado(s) por um paciente em um determinado atendimento.

1. Ao executar o processo de **Mudança de Leitos**, após selecionar o Paciente/Atendimento, o usuário terá acesso a todo o histórico de movimentação entre os leitos realizado pelo paciente (durante aquele atendimento).
