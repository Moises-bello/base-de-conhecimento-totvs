---
content_hash: 22daf731276c8dd1bccf5cd2e71d8659d4793c303b866762ab26b4625962168c
fetched_at: '2026-06-29T00:11:09.998543+00:00'
page_id: '640898265'
product: rm
source: tdn-rm
title: FISCAL01-16270 - CAT 42 - Valor de Confronto
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16270+-+CAT+42+-+Valor+de+Confronto
version: 2
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16270 |

## **02. SITUAÇÃO/REQUISITO**

No período de apuração do tributo icmsst | ressarcimento/complemento de icms st |coluna valor unitário realiza o calculo  com base no campo ICMS Próprio dentro dos itens.  Porém a nota de saída com cfop iniciado com 5.xxx.xxx esta atrelado o tipo de tributação isento ou não incidência com isso impactando no calculo do valor a ressarcir.

Conforme nossa consultoria e o manual da CAT 42 o campo Confronto deve ser preenchido anexo o trecho da cat 42.

## **03. SOLUÇÃO**

Para solucionar o problema do valor unitário do Confronto estar retornando 0 nas situações em que o tipo de tributação é isento ou não incidência, e que se trata de Venda Interna, foi implementado o retorno dos valores da Base de Cálculo (Isento ICMS) e Alíquota conforme o cálculo abaixo para o valor unitário do Confronto. Com o valor unitário do Confronto é possível calcular os valores de Ressarcimento do ICMS-ST.

**O cálculo para o valor unitário do Confronto é realizado da seguinte forma: (Valor da Base de Cálculo Isento ICMS \* (Alíquota / 100)) \* Quantidade**
