---
content_hash: e7d750ec073cc90de7ba7bd640ebe4e1d8dab0858ac9ab4246324264e59d13d4
fetched_at: '2026-06-29T00:12:09.324492+00:00'
page_id: '945392617'
product: rm
source: tdn-rm
title: FISCAL01-25760 - Evento Tributário para Filial SCP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=945392617
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Evento Tributário - Apuração Lucro Exploração |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25760 |

## **02. SITUAÇÃO/REQUISITO**

Necessidade de realizar a parametrização para apuração dos tributos IRPJ e CSLL através do evento tributário para uma filial SCP de Lucro de Exploração. A apuração deve ser realizada de forma separada da filial Sócio ostensiva.

## **03. SOLUÇÃO**

No cadastro do evento tributário o campo Apurar para Filial SCP passa a ficar habilitado quando marcado checkbox Lucro de Exploração, tornando possível a apuração do Lucro de Exploração através da filial SCP e de forma separada da filial Sócio ostensiva.

Disponível a partir da biblioteca 12.1.2406
