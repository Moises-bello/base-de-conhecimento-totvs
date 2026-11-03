---
content_hash: 4be1906cda8e3756da20c7a6335f11f130ac829e459ae47931cc1303108cfa5c
fetched_at: '2026-06-29T00:12:09.510221+00:00'
page_id: '947301388'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência INSS - PIS/PASEP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=947301388
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Relatório de Conferência INSS - PIS/PASEP |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-13907](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13907 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2406.280
* 12.1.2410.237
* 12.1.2502.149 e posteriores

## **03.** **SITUAÇÃO/REQUISITO**

Implementar no **Relatório de Conferencia INSS** a possibilidade de comparar o valor e a base de cálculo do PIS/PASEP informada no evento S-5001 com a base de cálculo do PIS/PASEP apurada pelo sistema TOTVS Folha de Pagamento, facilitando a conferência e validação dos dados.

## **04. SOLUÇÃO**

Implementada o valor e a base de cálculo do PIS/PASEP no **Relatório de Conferência INSS.**

Após atualizações das versões, é necessário a execução do RM.Atualizador.exe para a criação dos campos referente a conferência.

| Coluna | Valor Folha | Valor RET |
| --- | --- | --- |
| Base PIS/Pasep | Retorna a soma  dos eventos/verbas com Incidência em PIS/PASEP Mensal  com os Códigos 11, menos os eventos de estorno com incidência em PIS/PASEP com os Códigos 11. Tabela (PEVENTO.INCPISPASEP). | Retorna o valor da tag <vrBcPisPasep> do S-5001 e <ind13> = 0. |
| Base PIS/Pasep 13° | Retorna a soma  dos eventos/verbas com Incidência em PIS/PASEP Mensal  com os Códigos 12, menos os eventos de estorno com incidência em PIS/PASEP com os Códigos 12. Tabela (PEVENTO.INCPISPASEP). | Retorna o valor da tag <vrBcPisPasep> do S-5001 e <ind13> = 1. |

**ATENÇÃO:** A base de cálculo do PIS/PASEP (tag `<vrBcPisPasep>` do S-5001) é retornada por filial, e não por lotação tributária. Diante disso, foi necessário criar uma aba separada no relatório especificamente para o PIS/PASEP.

## **05. DEMAIS INFORMAÇÕES**
