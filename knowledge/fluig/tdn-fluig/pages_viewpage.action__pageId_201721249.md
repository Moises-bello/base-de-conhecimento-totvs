---
content_hash: f91bd5333f34f806495d5075b0b72db11362eb0009db54094623837ad6783942
fetched_at: '2026-06-28T21:35:19.278079+00:00'
page_id: '201721249'
product: fluig
source: tdn-fluig
title: FORM 006 - Por que o evento beforeMovementOptions não está executando?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201721249
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** Todas

# Ocorrência

Evento beforeMovementOptions não está executando.

# Causa

O evento beforeMovementOptions **não**executa se a atividade **não abrir o modal de seleção de usuários.** Caso a atividade já selecione o usuário, ou seja uma automática que já tenha o usuário selecionado por padrão na atividade destino, dentre outros casos onde não há seleção de usuários, o evento não é executado.

# Solução

Utilizar beforeSendValidate, outro evento de pré-envio de solicitação para formulários executado pelo fluig, verificar documentação a seguir:
