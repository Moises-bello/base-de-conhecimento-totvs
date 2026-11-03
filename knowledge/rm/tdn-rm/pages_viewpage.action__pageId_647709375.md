---
content_hash: 3ac288a18e0c484ce56acd808b9fca1ac13dbc750fe26cae097ab646152179ab
fetched_at: '2026-06-29T00:11:11.519114+00:00'
page_id: '647709375'
product: rm
source: tdn-rm
title: Cópia de Grupos de Patrimônio entre coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=647709375
version: 2
---

A cópia de grupos de patrimônio é uma entidade disponível na cópia de dados entre coligadas no módulo Serviços Globais.

Regras para cópia:

-Nenhuma das entidades vinculadas aos grupos é obrigatória (por exemplo, cenários de cálculo, título e etc). Caso não exista na coligada de destino, este dado será copiado nulo e a cópia será feita normalmente.

-Nos eventos contábeis, serão copiadas apenas as contas contábeis que existam na coligada de destino

Durante a cópia caso ocorra algum erro ou aviso, será detalhado no log do processo.
