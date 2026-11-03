---
content_hash: 889775517e6739f8c7457bb9a84975414c4a8fa55da971b8f177c3cc6bbe4ee2
fetched_at: '2026-06-29T00:11:06.410237+00:00'
page_id: '634487798'
product: rm
source: tdn-rm
title: FISCAL01-16213 - DT NF-e - NT 2020.005 - Alterações do código de barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=634487798
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Transmissão de NF-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16213 |

## **02. SITUAÇÃO/REQUISITO**

* **Grupo I. Produtos e Serviços da NF-e**

Incluídos os Campos:

**Código de barras** (Código de barras diferente do padrão GTIN do Grupo I (id:I03a)).

**Código de Barra da Unidade Tributável** (Código de Barras da unidade tributável que seja diferente do padrão GTIN do Grupo I (id:I12a)).

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação |
| 102.01 | I03a | cBarra | Código de barras diferente do padrão GTIN | E | I01 | C | 0-1 | 3-30 | Preencher com o Código de Barras próprio ou de terceiros que seja diferente do padrão GTIN |
| 111.01 | I12a | cBarraTrib | Código de Barras da unidade tributável que seja diferente do padrão GTIN | E | I01 | C | 0-1 | 3-30 | Preencher com o Código de Barras próprio ou de terceiros, que seja diferente do padrão GTIN, correspondente àquele da menor unidade comercializável identificado por Código de Barras. |

## **03. SOLUÇÃO**

Geração das tags cBarra e cBarraTrib no processo de NF-e.

Ambiente de Homologação → Disponível

Ambiente de Produção → A partir do dia 01-09-2021
