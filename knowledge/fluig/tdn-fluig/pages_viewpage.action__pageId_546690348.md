---
content_hash: 13b9fa65176529a1838eeed67136533e431b22975268e1534f720250de09f25e
fetched_at: '2026-06-28T21:35:27.409975+00:00'
page_id: '546690348'
product: fluig
source: tdn-fluig
title: Identity | Mensagem "Acesso restrito" ao tentar acessar o Identity
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546690348
version: 3
---

---

**Ocorrência**

Ao tentar acessar o Identity é apresentada a seguinte mensagem de erro:

**Causa**

Quando o filtro de acesso por IPs estiver configurado e habilitado, usuários que tentarem realizar o acesso a partir de endereços IP não cadastrados pelo administrador da empresa no Identity serão bloqueados.

**Solução**

Para liberar o acesso do usuário, o endereço IP externo informado na mensagem deve ser incluído no filtro de IPs pelo administrador do Identity, conforme descrito na documentação [Filtrar acesso por IPs externos](https://tdn.totvs.com/x/2pNvI).
