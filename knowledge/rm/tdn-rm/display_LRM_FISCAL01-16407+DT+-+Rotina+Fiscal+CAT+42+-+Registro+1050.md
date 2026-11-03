---
content_hash: 7577e6a378df12e9b9a892cd5fb5126dc1a3aac36e6875fe59944e8bba33ee79
fetched_at: '2026-06-29T00:11:10.210384+00:00'
page_id: '642619887'
product: rm
source: tdn-rm
title: FISCAL01-16407 DT - Rotina Fiscal CAT 42 - Registro 1050
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16407+DT+-+Rotina+Fiscal+CAT+42+-+Registro+1050
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | CAT 42 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16407 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a CAT 42, o registro 1050 - Saldos em Estoque de um produto com Saldo zerado no final do período, não foi gerado. O produto teve a entrada e saída no mesmo mês.  
Ao validar o arquivo sem o registro 1050 é apresentada a inconsistência abaixo.

## **03. SOLUÇÃO**

Registro 1050 deve conter todos os itens movimentados independente do saldo.

Quando a mesma quantidade de um produto entra e sai no mesmo período, o saldo fica zerado, mesmo nessas situações o produto deve aparecer no registro 1050.
