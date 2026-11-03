---
content_hash: 6f4e97f90b3c41c70a5df177d16923af6ea6e0ebca9dd5eebb5ed687aaa0a632
fetched_at: '2026-06-29T00:11:54.643354+00:00'
page_id: '856457111'
product: rm
source: tdn-rm
title: DT - Ajuste na API recordClockMarkings para aceitar registro com NSR 0 quando
  for de terminal de coleta do tipo 'Refeitório'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=856457111
version: 6
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Aceitar registro com NSR 0 na API recordClockMarkings |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-6613](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6613) |

## **02. SITUAÇÃO/REQUISITO**

Aceitar registro com NSR 0 na API **recordClockMarkings** quando o registro for de refeição.

## **03. SOLUÇÃO**

Aceitar registro com NSR 0 ou duplicado na API **recordClockMarkings** quando o terminal de coleta for do tipo 'Refeitório'.

## **04. VERSÕES**

Disponível a partir dos patches:

* 12.1.2410 e superiores
* 12.1.2406.115
* 12.1.2402.182

## **05. EXEMPLO**

1- Terminal de Coleta do tipo **'Refeitório'**.

2- Chamada na API **recordClockMarkings** como **NSR 0**.

3- Registro inserido na tabela **AINTEGRACAOBATIDAS**.

## **06. ASSUNTOS RELACIONADOS**

* [Importação das Batidas de Refeição TSA](https://tdn.totvs.com/display/public/LRM/DT_Importacao_De_Batidas_De_Refeicao_A_Partir_Do_TSA)
* [DT API recordClockMarkings](https://tdn.totvs.com/pages/viewpage.action?pageId=725741835)
