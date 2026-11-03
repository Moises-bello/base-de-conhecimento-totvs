---
content_hash: dc47e87c6d2b408443b979cecc24e9daf0f38ee9a1b014a0b75bd4440f04e5f5
fetched_at: '2026-06-29T00:12:03.613118+00:00'
page_id: '911867322'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro - Tipo "25 -Total Guia INSS DCTFWeb" - Tratar alíquota
  FAP diferente de tomador obra própria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911867322
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Lançamento Financeiro - Tipo "25 - Total Guia INSS DCTFWeb" |
| País: | Brasil |
| Issue: | [DRHROTRM-11789](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11789) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2402.273
* 12.1.2406.233
* 12.1.2410.166
* 12.1.2502.101 e superiores

## **03. SITUAÇÃO/REQUISITO**

Quando é feito o lançamento financeiro 25 - Total Guia INSS DCTFWeb o cálculo não estava considerando o valor do FAP da obra própria.

## **04. SOLUÇÃO**

Tratado o processo de geração do relatório de conferência INSS Patronal e lançamento financeiro 25 - Total Guia INSS DCTFWeb, para considerar a alíquota RAT ajustado (aliq. RAT X FAP) da obra própria sempre que o parâmetro "Considera Dados da Filial" esteja desmarcado. O cálculo passa a considerar a base do tomador (CEI) e aplicar a alíquota FAP do CEI especificada no anexo eSocial do CEI.

## **05.****DOCUMENTAÇÃO**
