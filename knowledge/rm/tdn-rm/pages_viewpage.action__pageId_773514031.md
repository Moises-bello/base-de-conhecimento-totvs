---
content_hash: 71f77a7afbca676fbf58c29a593fb11387d29b73fa2c2ec1e168184d10b3dc92
fetched_at: '2026-06-29T00:11:36.743753+00:00'
page_id: '773514031'
product: rm
source: tdn-rm
title: 'DT - S-2206: Considerar a função de confiança e a função normal'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773514031
version: 10
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-2206: Considerar a função de confiança e a função normal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6560](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6560) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2209.242
* 12.1.2302.167
* 12.1.2306.110

## **03. SITUAÇÃO/REQUISITO**

No cadastro do funcionário, foi informado a função de confiança. Entretanto, ao gerar o XML do evento S-2206, apenas a função normal é considerada, não sendo incluída a informação referente a função de confiança do funcionário.

## **04. SOLUÇÃO**

Realizamos uma atualização no produto para incorporar as duas funções (Normal e Confiança), a fim de atender ao exemplo mencionado no MOS S-1.1, item 8.2.

"Se o declarante contrata um trabalhador para o cargo de escriturário e, temporariamente exercer a função de gerente, deve preencher o campo {nmCargo} com [Escriturário] e o campo {nmFuncao} com [Gerente]."
