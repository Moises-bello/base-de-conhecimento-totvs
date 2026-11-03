---
content_hash: 6873272abd27f378a2da56811781b5c18f1bf7bb0acc448fe83f432bf39c86c3
fetched_at: '2026-06-28T21:35:19.192079+00:00'
page_id: '198940049'
product: fluig
source: tdn-fluig
title: BPM 005 - Por que ocorre erro ao abrir solicitação de processo com atividade
  inicial tipo timer?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198940049
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

Ao tentar abrir uma solicitação de um processo que possui apenas uma atividade inicial do tipo timer é apresentado a mensagem: Ops! "Não é possível iniciar manualmente um processo com atividade de início do tipo timer. Se mesmo assim deseja fazer isso, é necessário que o processo também possua uma atividade de início normal configurada. Saiba mais sobre, consultando a documentação técnica."

# Causa

Uma atividade do tipo Timer sempre será executada automaticamente pelo fluig e nunca poderá ser executada manualmente pelo usuário. No caso de uma atividade inicial ser do tipo Timer, esta solicitação somente poderá ser iniciada pelo fluig e será bloqueado o início manual.

# Solução

Para permitir que um processo possa ser iniciado tanto manualmente quanto automaticamente pelo fluig será preciso modelar o processo com uma atividade inicial normal além da inicial Timer.
