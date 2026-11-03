---
content_hash: ab3d3427f3427b17c82ca024ee154664352a243305682f9ff0797bf278716234
fetched_at: '2026-06-29T00:10:15.335623+00:00'
page_id: '464947863'
product: rm
source: tdn-rm
title: 4911620 EDUCACIONAL01-8113 DT Transferencia de Exemplar Manter Numero Tombo
type: documentation
url: https://tdn.totvs.com/display/LRM/4911620+EDUCACIONAL01-8113+DT+Transferencia+de+Exemplar+Manter+Numero+Tombo
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Bibliotecária |
| Função: | Transferência de exemplares |
| Ticket: | 4911620 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Transferência de exemplares |

## **02. SITUAÇÃO/REQUISITO**

No TOTVS Gestão Bibliotecária foi identificado que ao transferir um exemplar para outra filial/unidade o sistema alertava que o tombo já existe na filial/unidade de destino.

## **03. SOLUÇÃO**

Foi identificado que ao utilizar o mesmo tombo o sistema deveria apagar o tombo do exemplar de origem, como não estava apagando, considerava como existente pois o parâmetro para número do tombo global estava marcado. Foi feito o ajuste.
