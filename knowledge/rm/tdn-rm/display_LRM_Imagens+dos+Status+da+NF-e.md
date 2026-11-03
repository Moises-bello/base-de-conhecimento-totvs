---
content_hash: ad542b248c9e9a7394978836714017c0a61640f9fa49062d1ae4dad9d163ed22
fetched_at: '2026-06-29T00:05:57.840118+00:00'
page_id: '184780791'
product: rm
source: tdn-rm
title: Imagens dos Status da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Imagens+dos+Status+da+NF-e
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.20* |
| **Processo** | **:** | Envio da NF-e |
| **Subprocesso** | **:** | Envio da NF-e |
| **Data da publicação** | **:** | 03/02/2015 |

Os registros criados nos processos da NF-e podem assumir os seguintes status:

Logo após ser enviada se não ocorreu nenhum problema de validação o registro da NF-e assumirá o status Pendente: 

Se no momento do envio for detectada alguma inconsistência no movimento que irá gerar a NF-e o registro assumirá o status Inconsistente: 

Quando a NF-e for consultada e a mesma for autorizada pela SEFAZ ela assumirá o status Autorizada: 

Caso a nota consultada não tenha sido autorizada pela SEFAZ o registro assumirá o status Rejeitada:  Neste caso o movimento poderá ser corrigido e reenviado.

Existem casos nos quais o destinatário da NF-e possui alguma pendência com o Fisco e nestas situações a SEFAZ denega a nota emitida para ele. Assim sendo o registro assume o status Denegada: . Notas denegadas não podem ser reenviadas.

Uma nota cancelada inicialmente assume o status Cancelamento Pendente até que seja retornada pela SEFAZ: 

Quando o cancelamento é consultado se for autorizado o registro assume o status de Cancelado: . Se o cancelamento não for autorizado pela SEFAZ o registro terá seu status retornado para Autorizada:
