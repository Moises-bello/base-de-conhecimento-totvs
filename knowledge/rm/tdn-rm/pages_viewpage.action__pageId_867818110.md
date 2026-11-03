---
content_hash: 1b0cda0be047dd1eb82e92828de42657fc97a42c32b3bfcd57dff8b168f72df0
fetched_at: '2026-06-29T00:11:56.642771+00:00'
page_id: '867818110'
product: rm
source: tdn-rm
title: DT - Contabilização - Tratativa de arredondamento ao marcar o parâmetro "Gravar
  lote separado por filial"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867818110
version: 2
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Contabilização - Tratativa de arredondamento ao marcar o parâmetro "Gravar lote separado por filial" |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9987](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9987) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir da release:

* 12.1.2402.218
* 12.1.2406.146
* 12.1.2410 e superiores

## **03. SITUAÇÃO/REQUISITO**

Implementamos uma tratativa na contabilização ao utilizar o parâmetro **"Gravar lote separado por filial"**, que visa eliminar a diferença de centavos entre as contas de débito e crédito do funcionário quando há rateio por centro de custo. Essa melhoria assegura maior precisão nos lançamentos contábeis, garantindo que os valores sejam registrados de forma correta e equilibrada.

## **04. SOLUÇÃO**

O processo Encargos | Contabilização | Geração dos Lançamentos passou a verificar a diferença de centavos entre as contas débito e crédito quando o parâmetro **"Gravar lote separado por filial"** estiver marcado. Quando o sistema identificar a diferença entre as contas ele irá aplicar na última conta débito ou crédito de acordo com o rateio de cada filial.

## **05. DEMAIS INFORMAÇÕES**
