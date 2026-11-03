---
content_hash: 8ee655b5e893c4d09d5c7463d3020fe255533c62c4d8d2040d0d233eab744486
fetched_at: '2026-06-29T00:12:06.898134+00:00'
page_id: '917132275'
product: rm
source: tdn-rm
title: DT - Códigos de Cálculo 21/314/419 - Melhoria do Log de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=917132275
version: 9
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Melhoria no log de cálculo |
| País: | Brasil |
| Ticket: | [22746498](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2222746498%22 "22746498") |
| Story: | [DRHCALCRM-7925](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7925) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.240
* 12.1.2410.177
* 12.1.2502.105
* 12.1.2506 e superiores

## **03. SITUAÇÃO/REQUISITO**

O log de cálculo com os eventos dos códigos de cálculo 21, 314 ou 419 apresentavam informações padrão sobre os CC's, como cálculo do evento (contendo código e descrição do evento), código de cálculo e a prioridade

## **04. SOLUÇÃO**

Com a ocorrência de algum dos eventos com os códigos de cálculo 21, 314 ou 419 no envelope de pagamento, ao acessar o Log de Cálculo, é possível verificar que após a informação do evento a ser calculado, código de cálculo e a prioridade abrem-se outras duas linhas, contendo o valor do arredondamento lançado no período anterior, a competência considerada, o período, seguidas do valor do evento (existente antes da melhoria).                                                                                                                                                                   

*Exemplo da melhoria no Código de Cálculo 21*                                                       

*Exemplo da melhoria no Código de Cálculo 314*

*Exemplo da melhoria no Código de Cálculo 419*

## **05. ASSUNTOS RELACIONADOS**

[Código de Cálculo 21 - Arredondamento (Desconto)](https://tdn.totvs.com/pages/viewpage.action?pageId=452719805)

[Código de Cálculo 314 - Arredondamento de Desconto (Base)](https://tdn.totvs.com/pages/viewpage.action?pageId=452719430)

[Código de cálculo 419 - Desconto do Arredondamento de Líquido Insuficiente (Desconto)](https://tdn.totvs.com/pages/viewpage.action?pageId=517137486)
