---
content_hash: 53591c38092bf067e8c7ad1573e891e0b84048d6bd95336f91bd2ae0c4fa07ae
fetched_at: '2026-06-28T21:35:23.073073+00:00'
page_id: '243651260'
product: fluig
source: tdn-fluig
title: BPM 050 - Como solucionar o erro que ocorre ao Salvar/Completar uma tarefa?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243651260
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

**Versão:** 1.5.9

# Ocorrência

Ao tentar movimentar uma solicitação para a atividade automática, está ocorrendo o erro:

# Solução

O problema acima ocorre quando o fluig não consegue localizar usuários comuns para o mecanismo de atribuição definido na **condição da atividade automática** e na **atividade destino**.

Por exemplo, se na atividade automática for definido que o mecanismo é por papel e na atividade destino for definido que a atribuição é por grupo, o fluig enviará a solicitação para o usuário que estiver no grupo e no papel.

Para solucionar o problema, será necessário revisar o fluxo *workflow* para garantir que os mecanismos sejam atendidos.
