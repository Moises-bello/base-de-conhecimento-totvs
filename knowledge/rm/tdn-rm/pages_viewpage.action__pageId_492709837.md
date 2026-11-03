---
content_hash: c8aaf2fae1da00c1f00bde3bf6ae760147b864cc1672cfb8289c25ef764d4a69
fetched_at: '2026-06-29T00:10:21.718495+00:00'
page_id: '492709837'
product: rm
source: tdn-rm
title: FISCAL01-7775 DT EFD ICMS\IPI Considerar conta contábil do Item do Lançamento
  Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=492709837
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal - Geração do Arquivo |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000212 |

## **02. SITUAÇÃO/REQUISITO**

A Rotina do Sped Fiscal deve ser alterada para passar a gerar no campo COD\_CTA, a informação do campo novo que foi criado no Item do Lançamento Fiscal.

Essa alteração deve ser feita apenas nos registros referentes à documento fiscal. Os demais registros continuam com o comportamento atual.

## **03. SOLUÇÃO**

Nas rotina EFD ICMS\IPI foi implementado a geração da conta contábil dos registros referentes a item do lançamento fiscal com a conta contábil informada diretamente no item do lançamento fiscal.

Quando não informado conta contábil no Item a rotina continua no fluxo conforme documentação: <http://tdn.totvs.com/x/V4ovGQ>
