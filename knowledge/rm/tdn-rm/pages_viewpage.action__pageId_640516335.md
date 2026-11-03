---
content_hash: e66b5c3a8ecbbfb59534db06532ed169fbbfcbb5bfff7cb780fdb7b5c58d50a0
fetched_at: '2026-06-29T00:11:09.580964+00:00'
page_id: '640516335'
product: rm
source: tdn-rm
title: DT- Desconto do empréstimo consignado nas férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=640516335
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Férias |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCONS-431](https://jiraproducao.totvs.com.br/browse/DRHCONS-431) |

## **02. SITUAÇÃO/REQUISITO**

Provisionar valor nas férias para o desconto da parcela de empréstimo consignado do funcionário e posteriormente lançar na folha de pagamento para evitar líquido negativo.

## **03. SOLUÇÃO**

Criação de códigos de cálculo que visam provisionar o valor de desconto do empréstimo consignado no recibo de férias e posterior lançamento no envelope de pagamento.

EMPRÉSTIMO CONSIGNADO - CONDIÇÕES PARA PROVISIONAMENTO:

Se o número de dias de férias no mês for superior a 15 dias.

* No caso de férias partidas, verifica mais de 15 dias em cada mês

Verificar existência de desconto de empréstimos na competência anterior da folha de pagamento:

* Busca na tabela PFMOVTEMPCONSIG parcela de empréstimo no mês/ano anterior a competência atual da folha.

Se ainda existem parcelas pendentes daquele empréstimo para o funcionário nas competências referentes às férias:

* NROPARCELA + número de meses entre competência atual e a data de inicio das ferias

Se NROPARCELA for menor que TOTALPARCELAS, acumula valor (pode existir mais de um empréstimo).

Se NROPARCELA ou TOTALPARCELAS estiver com valor zerado na PFMOVTEMPCONSIG, não será lançado o desconto, e irá exibir mensagem de Aviso (finaliza Amarelo).

Foram criados os seguintes códigos de cálculo:

453 - PROVISÃO EMPRÉSTIMO CONSIGNADO FÉRIAS 1o. MÊS (Desconto)

454 - PROVISÃO EMPRÉSTIMO CONSIGNADO FÉRIAS 2o. MÊS (Desconto)

455 - PROVISÃO EMPRÉSTIMO CONSIG.FÉRIAS 1o. MÊS ENVELOPE (Provento)

456 - PROVISÃO EMPRÉSTIMO CONSIG.FÉRIAS 2o. MÊS ENVELOPE (Provento)

## **04. DEMAIS INFORMAÇÕES**

[Código de cálculo 453 - PROVISÃO EMPRÉSTIMO CONSIGNADO FÉRIAS 1o. MÊS (Desconto)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=640219341)

[Código de cálculo 454 - PROVISÃO EMPRÉSTIMO CONSIGNADO FÉRIAS 2o. MÊS (Desconto)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=640220443)

[Código de cálculo 455 - PROVISÃO EMPRÉSTIMO CONSIG.FÉRIAS 1o. MÊS ENVELOPE (Provento)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=640220522)

[Código de cálculo 456 - PROVISÃO EMPRÉSTIMO CONSIG.FÉRIAS 2o. MÊS ENVELOPE (Provento)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=640220779)

## **05. ASSUNTOS RELACIONADOS**

* [Exemplo de lançamento de empréstimo consignado nas férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=640219721)
