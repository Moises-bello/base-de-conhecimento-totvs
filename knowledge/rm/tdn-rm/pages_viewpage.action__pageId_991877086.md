---
content_hash: ad54369e597eb1ed7d3915f72a991159962de32ae67d925f7b5b28b9cbec9e3f
fetched_at: '2026-06-29T00:12:16.525980+00:00'
page_id: '991877086'
product: rm
source: tdn-rm
title: DT - Criação dos códigos de cálculo 490 - Estorno Base FGTS RRA Folha e 491
  - Estorno Base FGTS RRA 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=991877086
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cadastro de eventos |
| País: | Brasil |
| Ticket: | [24639836](https://totvssuporte.zendesk.com/agent/tickets/24639836 "View ticket on the Zendesk portal") |
| Issue: | [DRHCALCRM-9937](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9937) |

## **02.** **VERSÕES**

Liberados nas versões:

* 12.1.2410.301
* 12.1.2502.211
* 12.1.2506.159
* 12.1.2510 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Ao gerar uma rescisão complementar por dissidio de ano anterior ao atual para o colaborador, o sistema gera as informações do período atual e de RRA conforme configurado no parametrizador e os eventos de RRA possuem incidência em FGTS conforme orientação que devem ter a mesma incidência do evento com código de cálculo 37 - Diferença Salarial.

## **04.****SOLUÇÃO**

Para não gerar base de FGTS duplicada na tabela PFPERFF pois, o período atual possui a incidência devido aos eventos com códigos de cálculo 69 - Base de FGTS de Diferença Salarial e 410 - Base de FGTS de Diferença Salarial na Rescisão e também a incidência do eventos nos períodos de RRA, foram criados os códigos de cálculo 490 - Estorno Base FGTS RRA Folha e 491 - Estorno Base FGTS RRA 13º Salário.

## **05. ASSUNTOS RELACIONADOS**

* [Código De Cálculo 490 - Estorno Base FGTS RRA Folha](https://tdn.totvs.com.br/pages/releaseview.action?pageId=991869016)
* [Código De Cálculo 491 - Estorno Base FGTS RRA 13º Salário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=991869077)
