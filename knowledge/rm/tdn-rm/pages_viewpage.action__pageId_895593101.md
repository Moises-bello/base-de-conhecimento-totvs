---
content_hash: 3125dff05890d1b191679a6d6d5ddb0b34ecffa5392e22969411965b0e0de087
fetched_at: '2026-06-29T00:12:01.436915+00:00'
page_id: '895593101'
product: rm
source: tdn-rm
title: DT - S-1200 - Reintegração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=895593101
version: 4
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1200 - Reintegração |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10248](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10248) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.255
* 12.1.2406.199
* 12.1.2410.130 e superiores

## **03. SITUAÇÃO/REQUISITO**

Tratar a geração do XML do evento S-1200 de complemento no mês da reintegração do funcionário, atualmente o sistema está levando os valores já enviados de rescisão.

## **04. SOLUÇÃO**

Foi ajustada a geração do evento S-1200 para considerar somente o lançamento do complemento no mês da reintegração. A rotina agora valida o mês da reintegração e desconsidera os envelopes lançados com data de pagamento até dez dias após a data de desligamento cadastrada no cadastro do funcionário.

## **05. DEMAIS INFORMAÇÕES**
