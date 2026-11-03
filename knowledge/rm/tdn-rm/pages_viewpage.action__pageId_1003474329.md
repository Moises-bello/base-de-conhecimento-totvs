---
content_hash: 5b2df01a82c2e9e44105351bcb03a45d04f0f297fd6a932d8ef2740b577e45e7
fetched_at: '2026-06-29T00:05:45.084928+00:00'
page_id: '1003474329'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Rescisão descontando empréstimo de inicio de
  desconto para competencia seguinte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1003474329
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Cálculos |
| País: | Brasil |
| Issue: | [DRHCALCRM-9603](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9603)  [DRHCALCRM-9804](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9804) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410.307
* 12.1.2502.215
* 12.1.2506.118
* 12.1.2510.100
* e superiores

## **03. SITUAÇÃO/REQUISITO**

Conforme o MANUAL DE ORIENTAÇÃO DO EMPREGADOR, do MTE, "Se o trabalhador for desligado antes do início da competência de referência para o desconto da primeira parcela do empréstimo consignado, não deve haver escrituração do consignado no eSocial, nem de retenção de salário,\* tampouco de pagamento da parcela\* , ainda que os dados do contrato constem no Portal Emprega Brasil.",

## **04. SOLUÇÃO**

Após o ajuste realizado, se a data da demissão for anterior ao início do desconto previsto no contrato do Crédito do Trabalhador, nenhum valor referente ao empréstimo deverá ser descontado na rescisão e o evento de empréstimo não deve constar no recibo de rescisão. Do contrário, se a data da demissão for igual ou posterior ao início do desconto, o valor correspondente à(s) parcela(s) em aberto deve ser corretamente calculado e descontado na rescisão e o evento de empréstimo deve constar no recibo de rescisão com o valor devido.

## **05. ASSUNTOS RELACIONADOS**

[DT - Crédito do Trabalhador Cálculos](https://tdn.totvs.com/pages/viewpage.action?pageId=939246677)

[DT - Crédito do Trabalhador eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=925346824)

[Rescisão descontando empréstimo de início de desconto para competência seguinte](https://tdn.totvs.com/pages/viewpage.action?pageId=1003474794)
