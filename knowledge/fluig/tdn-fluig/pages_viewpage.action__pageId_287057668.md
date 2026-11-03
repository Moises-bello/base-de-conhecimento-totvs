---
content_hash: abfc024e6189d2becaa5c12b91b9542d553b07e04f0ede1ed71441afd7ba4e5e
fetched_at: '2026-06-28T21:35:25.703560+00:00'
page_id: '287057668'
product: fluig
source: tdn-fluig
title: ARQ - Por que ao tentar subir a plataforma acontece o erro ORA-04063?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287057668
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Banco de Dados:**  Oracle

# Ocorrência

Por que ao tentar subir a plataforma acontece o erro ORA-04063: view "FLUIG.ALL\_SEQUENCES" has?

# Causa

Isso acontece por que na versão 12.2 do Oracle foi modificado a tabela ALL\_SEQUENCES. Uma coluna desta tabela foi retirada sendo que a plataforma utiliza ela para views, conforme a documentação de configuração do Oracle.

# Solução

Dropar as views existentes e recriar as mesmas. O código está na documentação de .
