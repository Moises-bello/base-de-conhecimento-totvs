---
content_hash: 5dd29288a7427e618a248decddc60f4e8869ff86d1891db20705fe29631ccfbb
fetched_at: '2026-06-29T00:10:21.702071+00:00'
page_id: '492707099'
product: rm
source: tdn-rm
title: FISCAL01-7774 DT EFD Contribuições - Considerar conta contábil do Item do Lançamento
  Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=492707099
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Rotina Federal EFD Contribuições |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000385 |

## **02. SITUAÇÃO/REQUISITO**

A Rotina da EFD Contribuições e da integração com o TAF devem ser alteradas para passar a gerar no campo COD\_CTA a informação do campo novo que foi criado no Item do Lançamento Fiscal.

Essa alteração deve ser feita apenas nos registros referentes à documento fiscal. Os demais registros continuam com o comportamento atual.

## **03. SOLUÇÃO**

Nas rotinas TAF\EFD Contribuições foi implementado a geração da conta contábil dos registros referentes a item do lançamento fiscal com a conta contábil informada diretamente no item do lançamento fiscal.

Quando não informado conta contábil no Item a rotina continua no fluxo conforme documentação: <http://tdn.totvs.com/x/1YgvGQ>
