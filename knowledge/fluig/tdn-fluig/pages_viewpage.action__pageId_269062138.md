---
content_hash: 67a1254d4803578d8715ee1742d4c5d0c0cf5cb46ce7f262e0b3a6bf90791e70
fetched_at: '2026-06-28T21:35:24.063811+00:00'
page_id: '269062138'
product: fluig
source: tdn-fluig
title: ARQ - Por que retorna erro do Apache ao consultar um webservice?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269062138
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Por que ao consultar um determinado método do *Web Service* funciona normalmente em alguns casos, porém ao tentar efetuar uma nova consulta o erro abaixo é disparado?

xmlEclipse1024Arquivo de logtrue

# Causa

O nome do host HTTPS URL não corresponde ao *Common Name* (CN) no certificado do servidor.

A resposta do Apache na causa está retornando uma mensagem *Exception* referente ao certificado HTTPS:

# Solução

É necessário corrigir o nome do host HTTPS URL no certificado do servidor. Pois quando acessado o *Web Service* na barra de endereços do navegador, consta um X em HTTPS indicando que ele está incorreto.
