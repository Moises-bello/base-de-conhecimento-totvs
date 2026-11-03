---
content_hash: 2189627dc42fbd3b9b54e1f925c45387188b9e6c22a7bec03aec46fa5002958a
fetched_at: '2026-06-29T00:09:14.816083+00:00'
page_id: '421385265'
product: rm
source: tdn-rm
title: Excluir Composições não Utilizadas no Projeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385265
version: 2
---

São consideradas composições não utilizadas no projeto, as composições que não estão associadas a nenhum serviço e as composições que estão associadas a outras composições e não estão associadas a nenhum serviço.

**Observação:**  
Serão excluídas composições auxiliares que não estão sendo utilizadas no projeto, ou seja, estão cadastradas como auxiliares em composições que também não estão sendo utilizadas no projeto.

**Exemplos:**  
A composição 000001 não é auxiliar de nenhuma composição e não esta associada a nenhum serviço, portanto ao executar esse processo ela será excluída.  
A composição 000001 não está associada a nenhum serviço e tem como composição auxiliar a composição 000002 que também não está associada a nenhum serviço. Ao executar esse processo, as composições 000001 e 000002 serão excluídas.
