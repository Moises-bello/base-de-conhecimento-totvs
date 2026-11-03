---
content_hash: a77bdf5616ef74f3437dfe1b62bd18912d0dab0573f666ea12edb6c8ed3f9787
fetched_at: '2026-06-29T00:11:39.150939+00:00'
page_id: '788602316'
product: rm
source: tdn-rm
title: FISCAL01-20545 - DT - Reinf-4020 - Não gerar isenImun para 2.1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=788602316
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Escrituração |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-20545 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o evento Reinf R-4020 com a versão da Reinf configurada como 2.1.2 ou superior. O campo isenImun é gerado com o valor fixo 1.

## **03. SOLUÇÃO**

Para atender a versão 2.1.2 do layout da REINF o campo não será gerado.

Se o parâmetro de versão da REINF estiver com uma versão inferior, o comportamento anterior se mantêm inalterado.

Disponível a partir da biblioteca 12.1.2209
