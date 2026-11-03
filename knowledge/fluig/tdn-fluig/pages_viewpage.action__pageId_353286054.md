---
content_hash: 18fceaf58b9c99be141045a015430ad5dabe590ec94d2f97da5ae55ddf4b88b9
fetched_at: '2026-06-28T21:35:26.309439+00:00'
page_id: '353286054'
product: fluig
source: tdn-fluig
title: Identity | Como obter o objectGUID de um usuário no Active Directory?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353286054
version: 6
---

**Dúvida**

Como obter o objectGUID de um usuário no Active Directory?

**Solução**

Para localizar o valor do atributo objectGUID de um usuário, siga o procedimento abaixo:

**01.** No servidor do Active Directory, acessar o **Active Directory *Users and Computers***.

**02.** No diretório ***Users*** (Usuários), localizar o cadastro do usuário desejado.

**03.** Clicar duas vezes sobre o nome do usuário para exibir a janela de ***Properties*** (Propriedades).

**04.** Selecionar a aba ***Attribute Editor*** (Editor de Atributos).

**05.** Localizar na lista o atributo **objectGUID**. O valor será exibido ao lado do nome do atributo.

O exemplo acima foi criado a partir de um servidor Windows Server 2012 R2 com Active Directory 6.3.9600.16384. Versões diferentes do sistema operacional e/ou do AD podem divergir dos procedimentos descritos nesta página.
