---
content_hash: 56060ecaa1c0af0e96442102f6d71255987b42baabc5609d260611ef4d32d211
fetched_at: '2026-06-28T21:35:23.215407+00:00'
page_id: '244430948'
product: fluig
source: tdn-fluig
title: ESB - Por que ocorre o erro "elemento inesperado" ao consumir WS do TOTVS ESB?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244430948
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS ESB

# Ocorrência

Por que ocorre o erro de "elemento inesperado" ao consumir o WS do TOTVS ESB?

# Causa

A tag "in0" não está recebendo um conteúdo de texto.

# Solução

Colocar o conteúdo da tag entre **<![CDATA[...]>**, conforme o exemplo abaixo.

xml
...]]]]>
RMReceiver
]]>
