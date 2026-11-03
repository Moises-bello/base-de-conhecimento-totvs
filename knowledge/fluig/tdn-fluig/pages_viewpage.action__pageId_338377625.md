---
content_hash: 0b9aa8c01e06c48f37b4d79517ae963f4d34d088a10a1e3d674585a10731587b
fetched_at: '2026-06-28T21:35:26.112884+00:00'
page_id: '338377625'
product: fluig
source: tdn-fluig
title: Identity | Mensagem "O serviço do AD de sua empresa está fora" para alguns
  usuários ao acessar o Identity
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338377625
version: 8
---

---

**Ocorrência**

Alguns usuários não estão conseguindo acessar o contexto da empresa no Identity utilizando o endereço de e-mail e a senha do Active Directory. É apresentado o seguinte alerta:

**Causa**

Na aba Conta do cadastro destes usuários no Active Directory, o campo Domínio está preenchido incorretamente apenas com uma "@" ao invés do domínio completo de e-mail, por exemplo, "@empresa.com.br".

**Solução**

Corrigir o campo Domínio nos cadastros dos usuários no Active Directory com o domínio completo.

Dica

Você pode consultar o status dos diretórios Active Directory através da página .
