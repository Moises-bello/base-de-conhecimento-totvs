---
content_hash: 88a1f0fdf20aa637bc4ca083f03aa7fcfaf3478ba1bc239bec63dcdce42cec3d
fetched_at: '2026-06-29T00:11:21.280819+00:00'
page_id: '691455320'
product: rm
source: tdn-rm
title: FISCAL01-18124 - DT Data do Rateio por Centro de Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18124+-+DT+Data+do+Rateio+por+Centro+de+Custo
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Geração Automática de Guias DARF |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18124 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a Guia DARF do IRRFPJ está sendo considerado os lançamentos fiscais de acordo com a data base definida nos parâmetros da apuração do tributo (no caso pela data de emissão), mas o rateio desta guia está considerando a data de entrada dos lançamentos. Com isso o valor da guia refere-se ao acumulado das notas do emitidas no período e o rateio refere-se às notas que entraram no período.

## **03. SOLUÇÃO**

Alteração feita na consulta utilizada pela rotina de geração das guias para obtenção dos rateios para passar a considerar as datas de emissão e entrada.

Disponível a partir da biblioteca 12.1.33
