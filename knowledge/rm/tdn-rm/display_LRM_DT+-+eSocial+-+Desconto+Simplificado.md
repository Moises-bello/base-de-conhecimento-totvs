---
content_hash: 2d14fadc5d102d5a4ca35d8adb50545a97dd96af682e52dc0aed338229b5e9b0
fetched_at: '2026-06-29T00:12:01.369697+00:00'
page_id: '894370561'
product: rm
source: tdn-rm
title: DT - eSocial - Desconto Simplificado
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+eSocial+-+Desconto+Simplificado
version: 12
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | eSocial - Desconto Simplificado |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-6824](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6824) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.255
* 12.1.2406.200
* 12.1.2410.130
* 12.1.2502 e superiores

## **03. SITUAÇÃO/REQUISITO**

Possibilitar o envio da verba com a Natureza de Rubrica "68-Desconto simplificado mensal" no eSocial.

## **04. SOLUÇÃO**

1) Disponibilizamos os seguintes códigos de cálculo para possibilitar o lançamento do valor do desconto simplificado de IRRF no envelope do funcionário, conforme regras estabelecidas:

* + [477- Valor a Deduzir de IRRF Simplificado Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139184)
  + [478- Valor a Deduzir de IRRF Simplificado Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139208)
  + [479- Valor a Deduzir de IRRF Simplificado 13 salário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139220)

2) Será necessário que o usuário crie os eventos/verbas associados aos códigos de cálculo mencionados. Dessa forma, o sistema poderá lançar os eventos/verbas com os valores correspondentes ao desconto simplificado, quando aplicável.

3) Caso a empresa opte por não enviar a verba com o valor do desconto simplificado para o eSocial, será necessário informar os respectivos eventos/verbas na configuração de **"Eventos a Desconsiderar"** do eSocial, disponível em: Configurações | Parametrizador | eSocial | Registros Inativos | Eventos a Desconsiderar.

## **05. DEMAIS INFORMAÇÕES**

####
