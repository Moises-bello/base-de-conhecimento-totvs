---
content_hash: ea7bdf68d007155274f60b49281003552125c68b51bf4042403d8e162f3bdfb9
fetched_at: '2026-06-29T00:05:51.536079+00:00'
page_id: '1050882970'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência INSS Patronal - Tratar alíquota FAP diferente
  de tomador obra própria 13° Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1050882970
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Relatório de Conferência INSS Patronal - Tratar alíquota FAP diferente de tomador obra própria 13° Salário |
| País: | Brasil |
| Issue: | [DRHROTRM-16521](https://jiraproducao.totvs.com.br/browse/DRHROTRM-16521 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2506.276
* 12.1.2510.195
* 12.1.2602.117 e superiores

## **03. SITUAÇÃO/REQUISITO**

Na geração do Relatório de Conferência INSS Patronal, o sistema não esta considerando o valor do FAP da obra própria.

## **04. SOLUÇÃO**

Realizada a tratativa nos processos de geração do **Relatório de Conferência INSS Patronal** e do **Lançamento Financeiro do tipo "26 – Total Guia INSS DCTFWeb 13º Salário"**, para que o sistema passe a considerar a alíquota de RAT ajustada (alíquota RAT × FAP) da obra própria, sempre que o parâmetro “Considera Dados da Filial” estiver desmarcado.

Nessa condição, o cálculo passa a:

* considerar a **base do tomador (CEI)**; e
* aplicar a **alíquota de FAP do CEI**, conforme informada no **anexo do eSocial do respectivo CEI**.

## **05.****DOCUMENTAÇÃO**
