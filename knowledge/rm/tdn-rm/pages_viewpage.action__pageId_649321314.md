---
content_hash: b07aaea9ea6e2ed055cd84b76db9e133adcb1bf1815ea2402f55c6799d52cb76
fetched_at: '2026-06-29T00:11:11.769646+00:00'
page_id: '649321314'
product: rm
source: tdn-rm
title: FISCAL01 - 16276 DT - Alterar o serviço de seleção de CFOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=649321314
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | RSN - Considerar procedência |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16276 |

**02. SITUAÇÃO/REQUISITO**

      Alterar o serviço de seleção de CFOP para considerar a Procedência do item do Movimento

      Criar uma métrica adicional para indicar a utilização da regra avançada de CFOP e uma métrica para o novo recurso

**idmetrica:** gestao-fiscal-rm\_regras-de-selecao-de-natureza-utilizadas\_info

**Subtorina:** Filtro do Procedência

## **03. SOLUÇÃO**

Quando há procedência no serviço de seleção da natureza, ela é aplicada na query. Caso nenhuma natureza possua a procedência informada, todas as naturezas aplicáveis são retornadas por padrão.
