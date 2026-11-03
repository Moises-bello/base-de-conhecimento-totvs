---
content_hash: 534e986ef1005e3eb71a2bcdd10790fc6874fce5335fdbb311f6ccf9b8c24e86
fetched_at: '2026-06-29T00:10:14.490328+00:00'
page_id: '461908015'
product: rm
source: tdn-rm
title: DT Página de callback - IFrame Getnet
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461908015
version: 3
---

# IFRAME GETNET

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Portal Educacional e Processo Seletivo* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Pagamento com Cartão de Crédito/Débito*.* | ***Pagamento com Cartão de Crédito/Débito**.* | |  |  | |
| **Requisito (ISSUE):** | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-10376 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *FINTEGRACAOCARTAO, FINTEGRACAOHISTORICO* |

## Descrição

Criação de uma URL HTTPS com um método GET que será consumida pela plataforma Getnet para permitir que TOTVS Gestão Financeira seja informado quando houver uma alteração no status de uma transação.

## Procedimento para Utilização

O cliente deverá configurar na plataforma da Getnet a seguinte *URL*: []/Source/Fin-Financeiro/RM.Fin.Lan/Getnet/FinLanCartaoCallback.aspx.
