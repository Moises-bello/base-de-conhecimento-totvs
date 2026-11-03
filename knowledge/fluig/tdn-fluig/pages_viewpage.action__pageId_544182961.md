---
content_hash: 3e0d44291f382a038233c57426302fcd745ee84c0e91fe932ce50c0d8fd036ed
fetched_at: '2026-06-28T21:35:27.337420+00:00'
page_id: '544182961'
product: fluig
source: tdn-fluig
title: Identity | Credenciais de usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544182961
version: 20
---

# Falando de credenciais de usuário...

---

Nessa seção é possível parametrizar se o uso da senha pessoal será permitido para acesso dos usuários comuns nessa empresa no Identity. Consulte a documentação completa sobre [Senha pessoal](https://tdn.totvs.com/pages/viewpage.action?pageId=274828593) para mais informações.

Também pode-se definir se os usuários comuns podem trocar seu e-mail por meio da opção .

## Habilitar o uso da senha pessoal

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Credenciais de usuário.**

**03**. Marque a opção **Habilitar senha pessoal** para permitir a definição de uma senha pessoal aos usuários da empresa no Identity.

#f2f2f2#f2f2f2

Com esta opção habilitada, a senha pessoal será cadastrada pelo usuário durante o primeiro acesso dele ao Identity. Para usuários importados do Active Directory, o Identity não exige o cadastro da senha pessoal, mas o usuário poderá fazê-lo através da opção .

Multi-contexto

Caso o usuário possua cadastro em mais de uma empresa e tenha utilizado a senha pessoal para autenticar-se no Identity, ao tentar fazer a troca para uma empresa que não permita o login via senha pessoal o acesso será negado e ele deverá autenticar-se utilizando as credenciais de Active Directory da empresa que deseja acessar.

oculto

**Observação interna**

Esse passo a passo foi repassado aos artigos <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360034761353> e  <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360034334353>  
Se for feita alguma alteração, lembrar de alterar nesse artigo!

## Desabilitar o uso da senha pessoal

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Credenciais de usuário.**

**03**. Desmarque a opção **Habilitar senha pessoal** para impedir a definição de uma senha pessoal, aos usuários da empresa no Identity.

#f2f2f2#f2f2f2

Com esta opção desabilitada, o recurso de , em que os usuários cadastram-se manualmente na empresa através de um *link* na página de login, será desativado. Os usuários poderão acessar o Identity apenas com a senha do Active Directory e o Launchpad pessoal será desativado.

No entanto, por questões de segurança, mesmo com esta opção desabilitada os administradores sempre podem autenticar-se no contexto utilizando sua senha pessoal. Esta regra também se aplica ao recurso de troca de contextos.

Multi-contexto

Caso o usuário possua cadastro em mais de uma empresa e tenha utilizado a senha pessoal para autenticar-se no Identity, ao tentar fazer a troca para uma empresa que não permita o login via senha pessoal o acesso será negado e ele deverá autenticar-se utilizando as credenciais de Active Directory da empresa que deseja acessar.

## Habilitar troca de e-mail trocaemail

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Credenciais de usuário.**

**03**. Marque a opção **Habilitar troca de e-mail** para definir que os usuários da empresa poderão realizar a troca de e-mail.

#f2f2f2#f2f2f2

Será apresentada uma mensagem de confirmação ao administrador, informando os seguintes itens:

* O novo endereço de e-mail não é automaticamente substituído nos aplicativos associados ao usuário.
* O novo endereço de e-mail informado pelo usuário deve ser único no Identity.
* A troca de e-mail não é sincronizada com o Active Directory.
* Caso o usuário esteja cadastrado em mais de uma empresa no Identity, a troca de e-mail só será efetuada se essa opção estiver habilitada em todas elas.

**04.** Acione **Habilitar** para permitir a troca de e-mail.

#f2f2f2#f2f2f2

Com isso, a opção de troca de e-mail será habilitada para os usuários comuns no menu . Essa troca pode ser realizada apenas pelo próprio usuário, não por um administrador.

oculto

**Observação interna**

Esse passo a passo foi repassado ao artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360034759753>   
Se for feita alguma alteração, lembrar de alterar nesse artigo!

## Desabilitar a troca de e-mail trocaemail

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Credenciais de usuário.**

**03**. Desmarque a opção **Habilitar troca de e-mail** para impedir os usuários da empresa de realizar a troca de e-mail.

]]>
