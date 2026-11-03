---
content_hash: df437bd20c9e83495bcbe9028245e3f5f3a1966f55ec82f8c2dd93d711cc3a3c
fetched_at: '2026-06-29T00:11:10.155679+00:00'
page_id: '641675857'
product: rm
source: tdn-rm
title: DT 12173473 FISCAL01-16605 - Ressarcimento MG - Registros 1250 e 1255
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+12173473+FISCAL01-16605+-+Ressarcimento+MG+-+Registros+1250+e+1255
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED - EFD |
| País: | Brasil |
| Ticket: | 12173473 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16605 |

## **02. SITUAÇÃO/REQUISITO**

INTERPRETAÇÃO DE DEMANDA  
Cliente informa que ao gerar o Sped Fiscal, os registros 1250 e 1255 estão trazendo valores incorretos para os campos 03 e 04, devido a inconsistências de valores nos campos 12 e 15 do registro C185.

O valor que o sistema está gerando nos campos marcados em vermelho e em verde estão incorretos. É por isso que o registro está sendo gerado com valores muito maiores, segue

Referente ao campo 12 do registro C185:

De acordo com o cliente os campos deveriam gerar com a média do ICMS TOTAL da compra dos produtos e o mesmo está gerando duplicando o valor para o campo 12, segue:

1ª Compra:   
Quantidade: 102  
ICMS TOTAL: R$ 35.678,85  
MÉDIA: R$ 349,79265

2ª Compra:   
Quantidade: 112  
ICMS TOTAL: R$ 39.176,76  
MÉDIA: R$ 349,79250

TOTAL:  
Quantidade TOTAL: 214  
ICMS TOTAL: R$ 74.855,61000  
Média TOTAL: R$ 349,79257

O Sistema está duplicando as informações do campo com as informações da média TOTAL, exemplo: R$ 349,79257 \* 2 = R$ 699,58514. Dessa maneira ao gerar valores para os registros 1250 e 1255 consequentemente as informações estão sendo levadas incoerentes também.

Referente ao Campo 15 do registro C185 o valor que está sendo levado no campo é R$ 874,406547, devido ao sistema estar calculando as informações de acordo com a expressão abaixo informada, como o valor do campo 12 está incorreto o cálculo realizado se torna incoerente também.

Segue Cálculo realizado no arquivo do cliente:  
Campo 12 + Campo 13 - Campo 10 = Campo 15  
699,585147 + 174,8214 - 0 = 874,406547

## **03. SOLUÇÃO.**

Na geração do registro C185, no VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV (campo 12), alem dos campos 13(VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV) e 14(VL\_UNIT\_FCP\_ICMS\_ST\_ESTOQUE\_CONV), o valor preenchido  será a média do valor da referencia dos itens (produto).
