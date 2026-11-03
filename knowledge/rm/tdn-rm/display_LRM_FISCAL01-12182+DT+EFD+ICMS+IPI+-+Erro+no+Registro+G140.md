---
content_hash: 734cdf9d9f722677539677af889ed8353e5e9f12a0ae0276a7a5e8d40b7886af
fetched_at: '2026-06-29T00:10:37.087874+00:00'
page_id: '535855380'
product: rm
source: tdn-rm
title: FISCAL01-12182 DT EFD ICMS IPI - Erro no Registro G140
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-12182+DT+EFD+ICMS+IPI+-+Erro+no+Registro+G140
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12182 |

## **02. SITUAÇÃO/REQUISITO**

O G140 está sendo gerado com a quantidade total do item e o valor total do ICMS do item. Quando é criado um item com quantidade 2 e 2 patrimônios associados são gerados 2 registro G140 (um para cada patrimônio) e neste caso o G140 deveria ser proporcionalizado para considerar somente a proporção referente ao patrimônio (G125)

## **03. SOLUÇÃO**

Foi ajustado no sistema para que seja proporcionalizado o G140 quando se existir um item com quantidade maior que um e contendo mais que um patrimônio associado
