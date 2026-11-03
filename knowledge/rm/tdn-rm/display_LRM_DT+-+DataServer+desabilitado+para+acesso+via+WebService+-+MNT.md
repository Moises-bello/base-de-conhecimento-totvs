---
content_hash: 3b1ba3768b87da251008e5431a6a893ee923c934a954f3f5358a3d48dbe776be
fetched_at: '2026-06-29T00:10:38.882100+00:00'
page_id: '545258733'
product: rm
source: tdn-rm
title: DT - DataServer desabilitado para acesso via WebService - MNT
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+DataServer+desabilitado+para+acesso+via+WebService+-+MNT
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Manutenção |
| Função: |  |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-7725 |

## **02. SITUAÇÃO/REQUISITO**

Alguns DataServers não fazem sentido estar exposto por conter regras intermediários e só fazer sentido para uso interno, nesses casos o acesso WebService deve ser desabilitado.

## **SOLUÇÃO**

* Desabilitado DataServer de ser acessado via WebService quando esse não faz sentido estar exposto conforme regra de negocio.
* Lista dos DataServers desabilidados:
* + MntOrdemServicoData
