---
content_hash: f748778a694989614208f90767727eb0a3385c92c99001649e47ef241bf71d36
fetched_at: '2026-06-29T00:12:10.130639+00:00'
page_id: '952380438'
product: rm
source: tdn-rm
title: DT - S-1200 - Autônomo com tipo de documento igual "Gera IRRF"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=952380438
version: 12
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1200 - Autônomo com tipo de documento igual "Gera IRRF" |
| País: | Brasil |
| Issue: | [DRHROTRM-13910](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13910 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410.247
* 12.1.2502.154
* 12.1.2506.100 e superiores

## **03. SITUAÇÃO/REQUISITO**

Gerar o XML do evento S-1200 para autônomos cujo lançamento financeiro utiliza um tipo de documento configurado apenas como "Gera IRRF", nos casos em que não há retenção de IRRF por insuficiência de base para o desconto.

## **04. SOLUÇÃO**

Foi realizada uma tratativa no produto para que a geração do evento S-1200 ocorra corretamente nos casos de documentos configurados apenas como "Gera IRRF", mesmo quando não houver retenção do imposto devido à base insuficiente para o desconto.

O campo "Tipo de Documento" esta disponível no produto TOTVS Gestão Financeira, menu BackOffice | Gestão Financeira | Cadastros | Clientes Fornecedores | Anexos | Lançamentos, conforme demonstrado abaixo:

## **05. DEMAIS INFORMAÇÕES**

[S-1200 – Remuneração do Trabalhador vinculado ao RGPS](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719412)
