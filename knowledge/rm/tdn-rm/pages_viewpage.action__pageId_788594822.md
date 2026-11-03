---
content_hash: f124359ea92d934d6910d9dbe7f050a69a21176c6bd34359d0a62196cd24d360
fetched_at: '2026-06-29T00:11:39.129687+00:00'
page_id: '788594822'
product: rm
source: tdn-rm
title: FISCAL01-20244 - DT - Lançamento Fiscal - Cálculo Alíquota Ad Rem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=788594822
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-20244 |

## **02. SITUAÇÃO/REQUISITO**

Alterar o Cálculo do Lançamento Fiscal para considerar a Alíquota Ad Rem para o ICMS e ICMS ST. Também verificar a necessidade de ajustar os avisos de diferença de valor existentes no Lançamento

## **03. SOLUÇÃO**

Esse tipo de cálculo é necessário fazer de forma manual, apenas inserindo os dados nos campos Alíquota Ad Rem e Valor de ICMS.

Foi adicionado uma regra no campo “Base Tributada ICMS” para não recalcular o Valor de ICMS, caso o campo Alíquota AD Rem estiver preenchido.

Disponível a partir da biblioteca 12.1.2302
