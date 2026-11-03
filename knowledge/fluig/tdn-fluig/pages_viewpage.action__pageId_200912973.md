---
content_hash: ce034c665c34e0b80a00de83e58b77b9df86e1d998179535f55dc3b22ffb0354
fetched_at: '2026-06-28T21:35:19.265938+00:00'
page_id: '200912973'
product: fluig
source: tdn-fluig
title: Identity | Importação de grupos do Active Directory
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=200912973
version: 36
---

4.\*ndice

---

Esta documentação demonstra como efetuar a importação de grupos do Active Directory. Esses grupos, uma vez aceitos pelo administrador, passam a ser grupos do Identity e com isso podem ser associados aos aplicativos.

# Pré-requisitos

* Possuir grupos cadastrados no Active Directory.

* [SmartSync](https://tdn.totvs.com/x/VIs0DQ) instalado, configurado e em execução.

* [Active Directory configurado](http://tdn.totvs.com/pages/viewpage.action?pageId=201739046) no contexto da empresa no Identity.

# Importar grupos do Active Directory

Os grupos existentes no Active Directory são importados para o Identity através do SmartSync. Contudo, para que os grupos sejam efetivamente criados no Identity, é necessário que o administrador da empresa faça o aceite do grupo, conforme os passos da documentação [Aceitar grupos pendentes](https://tdn.totvs.com/x/OeEGEQ).

# Alterar nome de exibição dos grupos

O nome de um grupo do importado do Active Directory pode ser alterado no Identity para que, quando este grupo for aceito pelo administrador, ele seja criado com este novo nome de exibição. Os passos para realizar a alteração estão no item [Alterar o nome de exibição de um grupo](https://tdn.totvs.com/x/OeEGEQ#Aceitargrupospendentes-Alteraronomedeexibi%C3%A7%C3%A3odeumgrupo).

# Rejeitar grupos do Active Directory

É permitido ao administrador rejeitar grupos do Active Directory que tenham sido importados para o Identity, mas que ele não tem interesse em aceitar. Consulte os itens [Rejeitar um grupo](https://tdn.totvs.com/x/OeEGEQ#Aceitargrupospendentes-Rejeitarumgrupo) ou [Rejeitar vários grupos pendentes](https://tdn.totvs.com/x/OeEGEQ#Aceitargrupospendentes-Rejeitarváriosgrupospendentes) para conferir o passo a passo.
