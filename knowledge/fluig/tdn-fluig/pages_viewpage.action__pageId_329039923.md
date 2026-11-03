---
content_hash: c3db09fdd0ed15795393f9ae4baa23b4a075d899574c86a0f20d2a99a32a1fd6
fetched_at: '2026-06-28T21:35:26.015581+00:00'
page_id: '329039923'
product: fluig
source: tdn-fluig
title: IDE - É possível definir qual será a matrícula do usuário na plataforma quando
  é feito o provisionamento pelo Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329039923
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma integrado ao TOTVS Identity

# Ocorrência

Quando um usuário é provisionado na plataforma Fluig pelo Identity, a matrícula é definida automaticamente. Existe uma forma de definir qual será o valor da matrícula?

# Solução

Pelo provisionamento a partir do Identity, **não**: a matrícula na plataforma sempre será definida com base no ID do usuário no Identity.

Caso queira escolher a matrícula, o administrador deve incluir o usuário manualmente na plataforma. Ao salvar o novo usuário, ele será provisionado no contexto da empresa no Identity.
