---
content_hash: 5a4034c8b3dfd8824733b736293f7f9ef145e545d2f420f9c2db448d1fdb5ef2
fetched_at: '2026-06-29T00:11:56.756601+00:00'
page_id: '870407931'
product: rm
source: tdn-rm
title: DT - Folha Analítica - Tratativa no Total Geral quando rateia por centro de
  custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=870407931
version: 5
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Folha Analítica - Tratativa no Total Geral quando rateia por centro de custo |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11127](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11127 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.256
* 12.1.2402.226
* 12.1.2406.154 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Adaptar a Folha Analítica para que, ao ratear por centro de custo, o valor do campo "FGTS eSocial" no Total Geral seja a soma de todos os centros de custos.

## **04. SOLUÇÃO**

Implementamos uma tratativa para que, o sistema trunque o valor do campo "FGTS eSocial" no Total Geral da Folha Analítica, evitando diferenças de centavos devido ao arredondamento.

## **5. DEMAIS INFORMAÇÕES**

[Folha Analítica](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719339)
