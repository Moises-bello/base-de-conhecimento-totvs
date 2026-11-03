---
content_hash: 62d37fdad829520b451cd125d2aa12ee5fc0ae3efb2ca3e10a7f375ba64cf956
fetched_at: '2026-06-29T00:05:50.874644+00:00'
page_id: '1043719780'
product: rm
source: tdn-rm
title: 'DT - Nota Orientativa FGTS Digital: Rescisão com adiantamento de 13º maior
  que o 13º proporcional'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1043719780
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculos - FGTS |
| País: | Brasil |
| Ticket: | [#21376164](https://totvssuporte.zendesk.com/agent/tickets/21376164 "View ticket on the Zendesk portal") |
| Issue: | [DRHCALCRM-7222](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7222) |

## **02.****VERSÕES**

A partir dos patches:

* + 12.1.2502.289
  + 12.1.2506.258
  + 12.1.2510.178
  + 12.1.2602.102
  + 12.1.2606 e superiores

## **03. SITUAÇÃO/REQUISITO**

No momento da rescisão do contrato de trabalho, caso o valor de FGTS incidente sobre o adiantamento de 13º salário já recolhido seja superior ao valor proporcional efetivamente devido ao empregado, o sistema deverá permitir que o valor excedente da base de FGTS seja compensado na base de FGTS de outras verbas rescisórias (FGTS mensal).

## **04. SOLUÇÃO**

O sistema identificará automaticamente o valor do FGTS calculado e recolhido sobre o adiantamento de 13º salário e na rescisão recalculará a diferença entre o 13º salário proporcional e o valor pago antecipadamente determinando a base correta de FGTS devido.  
   
Se o valor do FGTS já recolhido sobre o adiantamento for maior que o valor calculado na rescisão, o excedente deverá ser acumulado no código de cálculo 492 - Base Excedente FGTS 13º a Compensar no FGTS Folha.  
   
O valor excedente acumulado será utilizado para compensar a base de FGTS de outras verbas rescisórias, conforme a legislação trabalhista vigente.

## **05. ASSUNTOS RELACIONADOS**

+ [Código De Cálculo 492 - Base Excedente FGTS 13º a Compensar no FGTS Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1043712337)
+ [FGTS Digital - Compensação do valor pago a título de 13º Maior do que a rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=877870673)
+ [Nota Orientativa nº 11/2025 - Leiaute S-1.3 - FGTS DIGITAL](https://tdn.totvs.com/pages/releaseview.action?pageId=1024335823)
