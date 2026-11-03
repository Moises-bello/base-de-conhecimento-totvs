---
content_hash: c11436846ac4e4c9243eca6ae3d3651c014a64733793f52de445005ae3f76bdc
fetched_at: '2026-06-29T00:11:05.498259+00:00'
page_id: '631618725'
product: rm
source: tdn-rm
title: FISCAL01-16215 NT 2020.005 - tpViaTransp - Lançamento Fiscal e NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=631618725
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio NF-e |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16215 |

## **02. SITUAÇÃO/REQUISITO**

Na tag Indicador de presença **“tpViaTransp”** (id: I23a) foram incluídas as opções:

12=Em mãos – Alterar a Descrição do Campo (Handcarry. (NT 2013/005 v 1.10)

13=Por reboque – Novo

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação |
| 122.01 | I23a | tpViaTransp | Via de transporte internacional informada na Declaração de Importação (DI) ou na Declaração Única de Importação (DUImp) | E | I18 | N | 1-1 | 2 | 8=Conduto/Rede Transmissão 9=Meios Próprios 10=Entrada/Saída Ficta  11=Courier  12=Em mãos  13=Por reboque |

## **03. SOLUÇÃO**

For criado um campo enumerado Por Reboque e Alterado "Handcarry" por "Handcarry (Em Mãos)".
