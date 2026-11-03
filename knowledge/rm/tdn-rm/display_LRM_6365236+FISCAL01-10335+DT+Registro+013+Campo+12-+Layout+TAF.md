---
content_hash: c4b54a8c4c795778fec96f2465c5cc7e7d0175b9a9544af15c75051243454bf4
fetched_at: '2026-06-29T00:10:32.073378+00:00'
page_id: '525797195'
product: rm
source: tdn-rm
title: 6365236 FISCAL01-10335 DT Registro 013 Campo 12- Layout TAF
type: documentation
url: https://tdn.totvs.com/display/LRM/6365236+FISCAL01-10335+DT+Registro+013+Campo+12-+Layout+TAF
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Layout TAF |
| Ticket: | 6365236 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10335 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar os registros de Integração TAF o sistema considera o campo valor contábil do lançamento: valorcont no campo 12 do registro T013. Esse campo é escriturado para o RM Liber considerando o valor líquido do movimento. Cliente solicita a alteração da geração dos registros TAF para que seja considerado o valor bruto da nota conforme solicitação do layout REINF: R-2010: 21 vlrTotalBruto idePrestServ Preencher com o valor bruto da(s) nota(s) fiscal(is) Validação: Deve corresponder a soma do campo {vlrBruto} dos registros vinculados.  
No lançamento do cliente o valor bruto difere do valor líquido, onde é considerado a dedução dos impostos.

## **03. SOLUÇÃO**

Alteração no Layout do TAF Registro T013, campo 12, alterada a ligação de VALORCONT para VALORMERC
