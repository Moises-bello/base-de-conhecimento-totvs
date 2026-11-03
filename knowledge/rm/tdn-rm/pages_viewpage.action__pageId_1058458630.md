---
content_hash: ebbe2d1f01dbd6e4116f3c0ed12e656d773bf62504d400da84983d802a22dfa4
fetched_at: '2026-06-29T00:05:52.656602+00:00'
page_id: '1058458630'
product: rm
source: tdn-rm
title: DT - CNPJ agora possui estrutura alfanumérica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058458630
version: 14
---

## **01. DADOS GERAIS**

| Produto: | TOTVS Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | CNPJ agora possui estrutura alfanumérica |
| País: | Brasil |
| Issues: | * [DRHROTRM-14494](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14494) * [DRHCALCRM-11373](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-11373) |

## **02. RELEASES**

* 12.1.2502.306
* 12.1.2506.296
* 12.1.2510.221
* 12.1.2602.139 e superiores

## **03. SITUAÇÃO/REQUISITO**

A **Receita Federal,** por meio da **Instrução Normativa nº 2.229/2024,** anunciou que o CNPJ passará a ter formato alfanumérico a partir de **julho de 2026**. A medida visa atender ao esgotamento das combinações numéricas atuais e à necessidade de novos registros de pessoas jurídicas, considerando o contexto da Reforma Tributária.

Diante desse cenário, torna-se necessário adequar o produto TOTVS Folha de Pagamento para garantir conformidade com a nova regulamentação.

## **04. SOLUÇÃO**

O produto TOTVS Folha de Pagamento foi adequado para suportar o novo formato do CNPJ alfanumérico, que passará a conter 14 posições, sendo:

* 8 posições iniciais para a raiz (alfanuméricas)
* 4 posições seguintes para a ordem do estabelecimento (alfanuméricas)
* 2 posições finais numéricas para os dígitos verificadores

Adicionalmente, foram realizadas adequações nas regras de validação do CNPJ, tanto nas telas quanto na geração de arquivos, para contemplar o novo padrão alfanumérico.
