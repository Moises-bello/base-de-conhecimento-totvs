---
content_hash: 082156915596f1d8a2cbcbc1b0c341ea63e5883a927c6f5e3c3327abec3f850f
fetched_at: '2026-06-29T00:11:27.380110+00:00'
page_id: '722655487'
product: rm
source: tdn-rm
title: FISCAL01-18525 - DT - Sped fiscal Bloco H- operações com ressarcimento dentro
  do período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=722655487
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED FISCAL |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18551 |

## **02. SITUAÇÃO/REQUISITO**

Para a situação em que o Produto Entrou (Compra) e Saiu (Venda) dentro do próprio período do arquivo do Sped Fiscal, vamos gerar o H005 com a Data de Inventário de 1 dia anterior ao da Data da rotina, H010 e o H030 ambos zerados.

## **03. SOLUÇÃO**

Realizado ajuste para que seja gerado o H030 para movimentações dentro do período de geração da rotina, nesse cenário o registro será gerado com valores zerados.

Disponível a partir da biblioteca 12.1.34
