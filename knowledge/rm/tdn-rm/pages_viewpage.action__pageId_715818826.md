---
content_hash: a3e4a8fe4e06389d2231959c736bea5c89fc8db49fc08fab0bb15cedff45d211
fetched_at: '2026-06-29T00:11:26.133513+00:00'
page_id: '715818826'
product: rm
source: tdn-rm
title: DT - RRA - Adequação Layout S-1.1 - Diferença Salarial / Diferença de Férias
  / Diferença 13º Salário  / Rescisão Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715818826
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Diferença Salarial / Diferença 13º salário / Diferença Férias |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-2991](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2991)  [DRHCALCRM-3244](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3244)  [DRHCALCRM-2992](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2992)  [DRHCALCRM-2994](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2994)  [DRHCALCRM-2998](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2998) |

## **02. SITUAÇÃO/REQUISITO**

Com o novo leiaute o RRA não é mais identificado pela tag <codIncIRRF> passou a ser identificado pela tag <**IndRRA**> no evento S-1200, S-1202, S-1207, S-2299 e S-2399.

Calcular os eventos de RRA separados em proventos e descontos e os mesmos devem ser lançados em períodos separados do cálculo da Folha/13º.

## **03. SOLUÇÃO**

1. Criar códigos de cálculo para separar os valores de RRA.
2. Deverá existir um envelope de pagamento separado para pagamento do RRA, não poderá estar no mesmo envelope de pagamento da folha.
   1. Definir período para lançamento no parametrizador (usuário irá informar, devendo ser acima de 99, igual foi feito para retificação);
   2. Esse período deve ser bloqueado pelo usuário para qualquer lançamento;
   3. A diferença de Férias e Folha podem ser inseridos no mesmo período;
   4. Décimo terceiro deve ser inserido em período diferente.
   5. Para rescisão complementar entendemos que seria o período completo como RRA não precisando separar
3. Continuará existindo os eventos de base para não ter impactos na DIRF – referentes ao período anterior a essa implementação
   1. Continuar preenchendo o histórico de RRA de acordo com o mescomp, anocomp e período
   2. O histórico de RRA deverá ser separado Folha e 13o. Salário (preencher os campos já existentes).

## **04.** **ASSUNTOS RELACIONADOS**

* [Parametrizador – Geral 2/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=715817366)
* [Código de cálculo 459 - DIFERENÇA SALARIAL RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=715818471)
* [Código de cálculo 460 - INSS DE DIFERENÇA SALARIAL RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=715818516)
* [Código de cálculo 461 - DIFERENÇA DE FÉRIAS RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=725725439)
* [Código de cálculo 462 - INSS DE DIFERENÇA DE FÉRIAS RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=725725460)
* [Código de Cálculo 463 - DIFERENÇA DE 13º SALÁRIO RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=721007397)
* [Código de Cálculo 464 - INSS DE DIFERENÇA DE 13º SALÁRIO RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=721007638)
* [Rendimentos Recebidos Acumuladamente (RRA)](https://tdn.totvs.com/pages/viewpage.action?pageId=715818269)
