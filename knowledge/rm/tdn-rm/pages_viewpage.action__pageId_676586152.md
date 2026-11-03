---
content_hash: ec1885f83b6714402c37f5e8cb0d5a5ffb1303052186f37b63bee05132461e18
fetched_at: '2026-06-29T00:11:17.082012+00:00'
page_id: '676586152'
product: rm
source: tdn-rm
title: FISCAL01-17700 DT - Liberar edição dos campos Identificador do Código da Receita
  e Tipo Recolhimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=676586152
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| País: | Brasil |
| Ticket: | [Ticket #13810580](https://totvssuporte.zendesk.com/agent/tickets/13810580 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17700 |

## **02. SITUAÇÃO/REQUISITO**

O campo **Identificador do Código da Receita** do formulário de “Outros Tributos” é habilitado somente para os tributos CSLLRF, PISRF, COFINSRF, CONTRIBSOCIALRF e INSS para lançamentos de saída e IRRF, IRPJ, PISIMPORT e COFINSIMPORT para lançamentos de entrada.

O campo **Tipo Recolhimento** só era habilitado para o tributo IRRFPJ em Lançamentos de Entrada.

Os campos deveriam ficar habilitados nos Lançamentos de Saída para possibilitar a geração das guias referentes ao código de receita 8045 para o tributo IRRFPJ.

**Caminho dos campos:**  
BO Fiscal | Obrigações Principais | Lançamentos | Situação tributária | Outros Tributos | Identificador do Código da Receita

BO Fiscal | Obrigações Principais | Lançamentos | Situação tributária | Outros Tributos | Tipo Recolhimento

## **03. SOLUÇÃO**

Alteração na regra para que os campos **Identificador do Código da Receita** e **Tipo Recolhimento** fiquem habilitados para o tributo IRRFPJ em lançamentos fiscais de entrada ou saída.

Informações

Disponível partir da versão 12.1.34
