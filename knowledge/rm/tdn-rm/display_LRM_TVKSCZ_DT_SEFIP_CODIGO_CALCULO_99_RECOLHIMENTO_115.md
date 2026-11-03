---
content_hash: ec708dbfc47704071540478018f818f702ce9fe3067601c3d51f51626b496b29
fetched_at: '2026-06-29T00:08:14.970947+00:00'
page_id: '244723022'
product: rm
source: tdn-rm
title: TVKSCZ_DT_SEFIP_CODIGO_CALCULO_99_RECOLHIMENTO_115
type: documentation
url: https://tdn.totvs.com/display/LRM/TVKSCZ_DT_SEFIP_CODIGO_CALCULO_99_RECOLHIMENTO_115
version: 115
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *Construção e Projetos.* |
| **Segmento:** | *RM.* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *Calculo do campo Remuneração sem 13º do registro 30.* |
| **Situação/Requisito:** | No SEFIP código de recolhimento 115, o valor dos eventos de código de cálculo "99 - Dif. Aviso Prévio" estava abatendo do campo Remuneração sem 13o do registro 30 mesmo sem ter incidência de FGTS e INSS. |
| **Solução/Implementação:** | O valor do código de cálculo "99 - Dif. Aviso Prévio" quando incide FGTS e INSS é somado ao valor do evento de código de cálculo "69 - BASE DE FGTS DE DIF SALARIAL", Somente neste caso deve ser abatido do campo Remuneração sem 13o do registro 30. Uma vez que esta verba não deve ser tratada no SEFIP  e sim na GRRF. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TVKSCZ* |
| **Requisito (ISSUE):** |  |

divs
