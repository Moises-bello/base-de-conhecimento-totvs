---
content_hash: a93f91c4546e17b21a762eb26dc1376a600001078b4377607f1c5156450a53c2
fetched_at: '2026-06-29T00:05:47.350580+00:00'
page_id: '1010813118'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Margem consignado considerar IRRF conforme mês
  caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1010813118
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Cálculos |
| País: | Brasil |
| Ticket: | [24134648](https://totvssuporte.zendesk.com/agent/tickets/24134648 "View ticket on the Zendesk portal") |
| Issue: | [DRHCALCRM-9656](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9656) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2410.317
  + 12.1.2502.227
  + 12.1.2506.177
  + 12.1.2510.110
  + 12.1.2602 e superiores

## **03. SITUAÇÃO/REQUISITO**

Atualmente, o sistema está considerando indevidamente o valor de IRRF retido no adiantamento salarial como parte da base de cálculo da provisão do Crédito do Trabalhador durante o processamento da folha mensal.

No entanto, de acordo com o entendimento baseado no regime de caixa do IRRF, o imposto retido no adiantamento deve ser considerado apenas para fins do próprio adiantamento, e não deve compor novamente a base de cálculo da provisão do Crédito do Trabalhador na folha mensal.

## **04. SOLUÇÃO**

O valor de IRRF retido no adiantamento salarial não deve ser incluído na base de cálculo da provisão do Crédito do Trabalhador na folha mensal.

*Consultoria: Diante do exposto, considerando que o fato gerador do IRRF ocorre na data do pagamento (regime de caixa) e não na competência da folha, concluímos que o imposto retido no adiantamento deve ser considerado apenas para a base de cálculo do próprio adiantamento, não compondo novamente a base da folha de pagamento.*

## **05. ASSUNTOS RELACIONADOS**

* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
