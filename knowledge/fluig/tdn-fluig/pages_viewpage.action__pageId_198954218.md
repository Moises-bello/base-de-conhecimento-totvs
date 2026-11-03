---
content_hash: c7d55feede2d152729aee5d040af5b0ea01567249dc988d639688f0e7200a2ed
fetched_at: '2026-06-28T21:35:19.214199+00:00'
page_id: '198954218'
product: fluig
source: tdn-fluig
title: BPM 101 - Por que algumas movimentações de processos realizados no fluig estão
  sendo bloqueados?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198954218
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Por que ao realizar movimentações em processos no fluig, tanto pela web como por dispositivo móveis através de rede externa da empresa, as chamadas estão sendo bloqueadas?

# Causa

Ao realizar movimentações em processos no fluig, tanto pela web como por dispositivo móveis através de rede externa da empresa, dependendo das configurações do firewall, as chamadas podem ser bloqueadas.

O Firewall de aplicação, pode identificar erroneamente a chamada REST feita como um possível ataque de SQL injection.

# Solução

Será necessário que adicionar no firewall exceções para as URLs do fluig, especialmente para as URLs que contenham “/api/rest”.
