---
content_hash: fafcc9d10028a7f530ef0fff6089a6b2a052f0fa53b7b037e149ab2d3ea3cb36
fetched_at: '2026-06-29T00:11:42.685861+00:00'
page_id: '795090587'
product: rm
source: tdn-rm
title: FISCAL01-20943 - DT - Alterar a geração do R-4010
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795090587
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD-REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-20892 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a geração do Evento R-4010 para reconhecer o campo criado no cadastro da Natureza de Rendimento (Rendimento Isento/Não tributável)

## **03. SOLUÇÃO**

Alteração no evento R-4010 para que as tags VlrIR e VlrRendTrb fossem geradas com zero quando a natureza de rendimento fosse isenta/não tributável, e para que a tag VlrRendBruto fosse gerada com o valor da base de cálculo para este mesmo cenário.

Disponível a partir da biblioteca 12.1.2302
