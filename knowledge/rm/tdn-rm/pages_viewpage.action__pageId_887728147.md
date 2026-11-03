---
content_hash: e657f048ac0dafdf64814fc8bfee6e29e73d6a32a255aa8039496ea26dfffe14
fetched_at: '2026-06-29T00:12:00.717339+00:00'
page_id: '887728147'
product: rm
source: tdn-rm
title: DT - S-1010 - Gerar a tag <codIncCP> conforme Instrução Normativa nº2185/2024
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=887728147
version: 13
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1010 - Gerar a tag <codIncCP> conforme Instrução Normativa nº2185/2024 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10566](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10566) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.245
* 12.1.2406.185
* 12.1.2410.120 e superiores

## **03. SITUAÇÃO/REQUISITO**

Implementar ajustes na geração do evento "S-1010 - Tabelas de Rubricas" para garantir que a tag**`<codIncCP>`** seja gerada em conformidade com a [Instrução Normativa nº 2185/2024](https://www.totvs.com/blog/fiscal-clientes/esocial-alteracoes-nas-contribuicoes-sociais-previdenciarias/).

## **04. SOLUÇÃO**

O sistema foi ajustado para que, na geração do XML do evento com código de cálculo "**352-Salário Maternidade Complementar"**, a tag `<codIncCP>` seja preenchida da seguinte forma:

* Valor **15**, quando a incidência de INSS for exclusiva do segurado.
* Valor **21**, quando o evento possuir apenas incidência de INSS.

**Exemplo:**

  Geração do XML do evento S-1010:

  Comparativo de Incidências de Rubricas

Maiores informações sobre o processo Comparativo de Incidências de Rubricas acessar o link abaixo:

## **05. DEMAIS INFORMAÇÕES**

[Salario Maternidade Complementar](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719063)
