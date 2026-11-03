---
content_hash: a109f77a958c4dab4cd36f7b84289b3d01216829a126f71400cb470c33bfd890
fetched_at: '2026-06-28T21:35:22.787467+00:00'
page_id: '240296146'
product: fluig
source: tdn-fluig
title: Identity | Preciso liberar o Identity no proxy ou firewall da empresa?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240296146
version: 14
---

**Dúvida**

Preciso liberar o Identity no proxy ou firewall da empresa?

**Solução**

Com o objetivo de eliminar pontos únicos de falha e proporcionar melhor disponibilidade e escalabilidade, desde junho de 2016 o Identity utiliza um balanceador com redundâncias que não possui um IP fixo para liberação.

1. Liberar acesso para a URL (\*.[fluigidentity.com](http://fluigidentity.com/)) e não mais para o IP (caso seja por *firewall* tipo *next generation* que permite essa funcionalidade);

2. Deixar o acesso ao Identity atrás de um *proxy* interno (tanto os ADs para comunicação via SmartSync, quanto o acesso dos usuários à interface *web*), assim o cliente apenas libera o acesso para o *proxy* e todos são beneficiados com isso;
