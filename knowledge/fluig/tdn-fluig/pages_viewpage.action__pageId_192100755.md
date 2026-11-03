---
content_hash: af30aa139f9ca5cf5a728372bab2d8f0912a9b7b9e3906bcf71385fb8404612b
fetched_at: '2026-06-28T21:35:19.136075+00:00'
page_id: '192100755'
product: fluig
source: tdn-fluig
title: Identity | É possível alterar o timeout da sessão no Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=192100755
version: 13
---

**Dúvida**

É possível alterar o timeout da sessão no Identity?

**Solução**

**Não**. Por padrão, as sessões do Identity em **inatividade** duram em torno de **4 dias**, podendo se estender por mais tempo quando estiver em plena utilização.

O Identity é executado em várias máquinas, simultaneamente. No entanto, o usuário realiza login em apenas uma máquina. Nesse período, caso o usuário seja direcionado para outra máquina, o Identity também solicitará novo login.

Saiba mais em .
