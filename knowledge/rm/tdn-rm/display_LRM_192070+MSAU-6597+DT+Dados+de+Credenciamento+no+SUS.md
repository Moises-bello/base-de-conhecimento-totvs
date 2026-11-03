---
content_hash: 38f488a15bcfcb2e3b6c2bbfc4a5af5ac46130b9e969e9f5f8b23e101d465072
fetched_at: '2026-06-29T00:08:31.714392+00:00'
page_id: '273306769'
product: rm
source: tdn-rm
title: 192070 MSAU-6597 DT Dados de Credenciamento no SUS
type: documentation
url: https://tdn.totvs.com/display/LRM/192070+MSAU-6597+DT+Dados+de+Credenciamento+no+SUS
version: 110
---

# Dados de credenciamento no SUS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento SUS | Elaboração de AIH | |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Realizado ajuste na elaboração de AIH para que o sistema já carregue os dados de credenciamento do médico executante, quando ele for credenciado direto no convênio SUS.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.16.103

## Procedimento para Utilização

       1.            Acesse o menu Faturamento > Faturamento SUS > Elaboração de AIH.

       2.            Selecione um AIH em elaboração.

       3.            Na aba de procedimentos, inclua um novo procedimento para o atendimento.

       4.            Ao preencher os dados do médico executante, os sistema deve copiar os dados do credenciamento do médico para os campos "Doc Recebedor" e "Recebedor".

divs
