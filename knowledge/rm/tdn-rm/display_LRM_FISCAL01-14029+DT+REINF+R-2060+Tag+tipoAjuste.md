---
content_hash: 63a688e397cdebb310b0d2477f545e36ed47f03018a8b6b7a6e33b64ba471fc6
fetched_at: '2026-06-29T00:10:52.159496+00:00'
page_id: '570370414'
product: rm
source: tdn-rm
title: FISCAL01-14029 DT REINF R-2060 Tag tipoAjuste
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-14029+DT+REINF+R-2060+Tag+tipoAjuste
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração dos Eventos REINF R-2060 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14029 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a Reinf o lançamento de ajuste será gerado no Grupo tipoAjuste  e ser totalizado no campo vlrExcRecBruta quando for redução ou no campo vlrAdicRecBruta quando for adição.

## **03. SOLUÇÃO**

No registro R-2060 da REINF foi implementado a tag tipoAjuste baseado nos lançamentos de Outros débitos e créditos do tributo CPRB.

Mapeamento dos campos do registro R-2060 : .

Observação: O valor dos lançamento de outros débitos e créditos considerado é para Exclusão ou Adição da base de cálculo da CPRB.
