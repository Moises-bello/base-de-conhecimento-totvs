---
content_hash: 1864197b169358fb3b639c14b9c5b5e3c90669f99d604d2efc3d464700ed13d1
fetched_at: '2026-06-29T00:12:03.419553+00:00'
page_id: '908348047'
product: rm
source: tdn-rm
title: DT - Atualização do FGTS - Mensagem de alerta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=908348047
version: 8
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Atualização do FGTS - Mensagem de alerta |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-12779](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12779) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.270
* 12.1.2406.228
* 12.1.2410.159 e superiores

## **03. SITUAÇÃO/REQUISITO**

No processo "**Atualização do FGTS**", ao selecionar o parâmetro "Incluir a competência atual", é exibida uma mensagem de alerta orientando sobre os cuidados necessários antes de prosseguir. No entanto, caso o usuário opte por marcar "Não exibir novamente", a mensagem deixa de ser apresentada, o que pode levar a divergências entre os campos "Saldo do FGTS para Fins Rescisórios" e "Saldo FGTS na CEF", caso as validações necessárias não sejam realizadas previamente.

04. **SOLUÇÃO**

O processo de "**Atualização do FGTS**" foi ajustado para garantir que a mensagem de alerta com as orientações necessárias seja sempre exibida quando o parâmetro "Incluir competência atual" estiver marcado. Dessa forma, o cliente deverá seguir as instruções apresentadas na mensagem para evitar possíveis divergências no processo.

## **05. DEMAIS INFORMAÇÕES**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719557>
