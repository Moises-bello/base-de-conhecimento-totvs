---
content_hash: 9a5b42f664e3dad9774faa7c058ff4e0976cd1afc860a028d04efcaeea411166
fetched_at: '2026-06-29T00:10:59.163677+00:00'
page_id: '611640461'
product: rm
source: tdn-rm
title: FISCAL01-14949 DT Gerar o Evento R-2099 com R-2055 autorizado no período pelo
  Backoffice RM - Reinf
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611640461
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Eventos Periódicos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14949 |

## **02. SITUAÇÃO/REQUISITO**

* Autorizar um Evento do Tipo R-2099 com um R-2055 no período Preenchendo o campo evtAquis
* Conferir a geração dos campo 52 “CRAquis”, 53 “vlrCRAquis” e 54 “vlrCRAquisSusp” do Grupo “RAquis” no retorno do R-2099
* Implementar no mercado a partir da versão 12.1.28

## **03. SOLUÇÃO**

* Implementado a tag evtAquis na transmissão do R-2099 na versão 1.05
* Tratado o retorno para exibir nos Totalizadores caso exista 2055 no período

Ao autorizar o R-2099 na versão 1.05 da REINF que exista R-2055 autorizado no período o sistema irá exibir os totalizadores de Aquisições de Produtor Rural.
