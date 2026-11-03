---
content_hash: c6e384a2ff0ad1af8c30cc20a72b6788b82db16746cab62745a1d6083e0f71ac
fetched_at: '2026-06-29T00:08:51.106661+00:00'
page_id: '336405679'
product: rm
source: tdn-rm
title: DT - Cobrança de Coparticipação em atendimento de retorno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=336405679
version: 2
---

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Saúde* |
| **Módulo:** | **Gestão Hospitalar** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Atendimento Externo (solicita autorização TISS).* | *GeraSolicitacaoGuia* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | |  |  | |  |  | |
| **Cadastros Iniciais:** | Condições contratuais com convênios |
| **Tickets relacionados** | *1021878* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *RMSAU-1691* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | ***SQL SERVER® e ORACLE®*** |
| **Sistema(s) Operacional(is):** | ***Windows®*** |

Cobrança de coparticipação em atendimentos de retorno  

## Descrição

  Ao solicitar uma guia de autorização de uma consulta (tiis) com valor de coparticipação o sistema lança o valor nos gastos particulares da conta, para atendimentos em retorno o valor de coparticipação não deve ser lançado.

ATENDIMENTO.

Incluir uma guia de solicitação de SP/SPADT com item de consulta consulta e clicar no botão indicado

RETORNO DA TISS com valor de coparticipação (#TOTALCOBRADO) para a consulta solicitada

 CONTA DO PACIENTE

  Na aba gastos particulares não deve lançar qualquer valor de coparticipação referente a consulta
