---
content_hash: 7666e7fea436d311142a4c0050c390e3c379130c42a69a6b41d36ee64aedcefc
fetched_at: '2026-06-28T21:35:19.350638+00:00'
page_id: '201743983'
product: fluig
source: tdn-fluig
title: Identity | Usuários não estão conseguindo acessar o Identity com a senha do
  Active Directory. Como resolver?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201743983
version: 12
---

**Dúvida**

O contexto do Identity está integrado ao Active Directory (AD) e meus usuários sempre utilizam a senha do AD para se autenticar, porém hoje não estão conseguindo. O que pode estar acontecendo?

**Solução**

O problema deve estar na conexão entre o Identity e o Active Directory, que é realizada através do SmartSync.

Para verificar o status da conexão, siga os seguintes passos:

**01**. Acessar o contexto no Identity com o administrador.

**02**. Acionar o ícone **Configurações** no canto superior direito.

**03**. Acessar a opção [**Active Directory**](https://tdn.totvs.com/x/AptUE).

**04**. Acionar o *link* [**Gerenciar Active Diretories**](https://tdn.totvs.com/x/W55UE).

**05**. Acionar **Atualizar listagem**.

**06**. Verifique o status exibido ao lado dos ADs vinculados.

Se o status do diretório não for **Disponível** tanto para o **SmartSync** quanto para **AD**, entre em contato com a sua equipe de infraestrutura interna para verificar se o servidor em que o SmartSync e/ou o Active Directory está instalado está indisponível. Em caso de dúvidas, consulte a documentação de configuração do [SmartSync](https://tdn.totvs.com/x/VIs0DQ).

Caso o Active Directory esteja indisponível, os usuários podem utilizar a [Senha Pessoal](https://tdn.totvs.com/x/MY1hE), própria do Identity, como paliativo para realizar o acesso.
