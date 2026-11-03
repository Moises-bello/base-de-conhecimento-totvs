---
content_hash: f54accb14cba29bc5bc08f6f8088fc78a9be027526811e0a926beb4d224ec2e7
fetched_at: '2026-06-29T00:10:15.054299+00:00'
page_id: '463802831'
product: rm
source: tdn-rm
title: DT Base de cálculo dos tributos na baixa de lançamentos a pagar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463802831
version: 3
---

# BAIXA DE LANÇAMENTOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Backoffice* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Baixa de Lançamento a Pagar* | *Baixa de Lançamento a Pagar* | |  |  | |
| **Requisito (ISSUE):** | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-6538 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |

## Descrição

Criado um parâmetro para permitir o usuário informar a base de cálculo dos tributos na baixa manual para lançamentos a pagar.

## Procedimento para Utilização

No parametrizador do TOTVS Gestão Financeira, na etapa [*Financeiro >> Contas a Pagar >> Baixa >> Manutenção de Baixas*], deve ser marcado o parâmetro "" para permitir o usuário informar a base de cálculo dos tributos na baixa manual para os lançamentos a pagar.

Com esse parâmetro marcado, na baixa manual, na etapa de Edição do Lançamento será apresentado o campo "Base de cálculo dos tributos" onde o usuário poderá informar a base de cálculo. Caso não seja informado nenhum valor nesse campo o sistema fará o cálculo já existente.

Obs: A base de cálculo informada no momento da baixa, somente será aplicada no caso de baixas parciais. Sendo que ao quitar o lançamento que possui baixa parcial, a base de cálculo restante será aplicada mesmo que seja informado uma base de cálculo diferente no momento da baixa.
