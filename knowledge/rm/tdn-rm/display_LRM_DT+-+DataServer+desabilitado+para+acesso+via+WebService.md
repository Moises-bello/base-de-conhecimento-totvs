---
content_hash: 69f86ad659aa7195f43137b034fa4875a9066c5e1367385503ae57b493048885
fetched_at: '2026-06-29T00:10:38.839647+00:00'
page_id: '545248058'
product: rm
source: tdn-rm
title: DT - DataServer desabilitado para acesso via WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+DataServer+desabilitado+para+acesso+via+WebService
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, compras e faturamento |
| Função: |  |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATFATCMPCRM01-11057 |

## **02. SITUAÇÃO/REQUISITO**

Alguns DataServers não fazem sentido estar exposto por conter regras intermediários e só fazer sentido para uso interno, nesses casos o acesso WebService deve ser desabilitado.

## **SOLUÇÃO**

* Desabilitado DataServer de ser acessado via WebService quando esse não faz sentido estar exposto conforme regra de negocio.
* Lista dos DataServers desabilidados:
* + MovCupomFiscalBaseData
  + MovMovimentoData
  + MovConsultaOrcamentoData
