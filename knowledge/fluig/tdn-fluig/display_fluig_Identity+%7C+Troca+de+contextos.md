---
content_hash: 95aca70163d13de6bf24a8c913e34e6d472579f022296cc644fb4cd370824582
fetched_at: '2026-06-28T21:35:26.004686+00:00'
page_id: '329035508'
product: fluig
source: tdn-fluig
title: Identity | Troca de contextos
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Troca+de+contextos
version: 43
---

# Falando de troca de contextos...

---

Quando um usuário é incluído em mais de um contexto no TOTVS Identity, a aplicação permite que ele alterne entre as empresas pelo menu de troca de contextos. Os contextos exibidos para troca pelo menu podem variar conforme o método de autenticação usado pelo usuário para acessar a empresa no Identity:

**:** Todos os contextos, inclusive o Pessoal, são listados para troca pelo menu.

Quem administra a empresa pode desabilitar a utilização da senha pessoal através das configurações de .

**Senha do [Active Directory](https://tdn.totvs.com/x/AptUE) ou via [Desktop SSO](https://tdn.totvs.com/x/A8xUE):** Todos os contextos, exceto o Pessoal, são listados para troca pelo menu. Será necessário informar a senha pessoal ou do Active Directory associado ao contexto que está tentando acessar.

O Identity permite o acesso a apenas uma empresa em cada navegador, o que chamamos de "sessão". Ao trocar de empresa, a sessão na empresa atual é encerrada e uma nova sessão é aberta para o outro contexto.

## Vincular contextos

---

**01.** Ao receber o e-mail de convite do contexto, acionar o *link* **Clique aqui para se juntar a [nome da empresa]**.

#f2f2f2#f2f2f2

O usuário será direcionado para a página de [login](https://tdn.totvs.com/x/bZpUE) do contexto e o campo E-mail estará preenchido automaticamente.

**02.** Informar a senha pessoal ou a senha usada para fazer login na outra empresa para autenticar-se no novo contexto.

**03.** Acionar **Entrar**.

#f2f2f2#f2f2f2

O novo contexto será integrado à conta do usuário no Identity e a troca de contextos será habilitada.

## Trocar contexto (Usuário comum)

---

**01.** Acionar **Perfil** no canto superior direito da página. Os contextos em que o usuário está cadastrado serão listados nesse menu.

**02.** Selecionar o contexto que deseja acessar.

#f2f2f2#f2f2f2

Caso tenha se autenticado no contexto utilizando a senha do Active Directory ou Desktop SSO, ao fazer a troca será preciso digitar a senha pessoal ou do Active Directory da empresa que pretende acessar. Não é solicitado novo login quando logado com senha pessoal.

Se tiver configurado o acesso com autenticação multifator, também será necessário informar o código de verificação gerado no aplicativo .

## Trocar contexto (Administrador)

---

**01.** Acionar **Perfil** no canto superior direito da página.

**02.** Selecionar no menu o contexto que deseja acessar.

#f2f2f2#f2f2f2

Caso tenha se autenticado no contexto utilizando a senha do Active Directory ou Desktop SSO, ao fazer a troca pode ser preciso digitar a senha pessoal ou do Active Directory da empresa que pretende acessar. Não é solicitado novo login quando logado com senha pessoal.

Se tiver configurado o acesso com autenticação multifator, também será necessário informar o código de verificação gerado no aplicativo .

## Trocar contexto pela URL

---

**01.** Digitar na barra de endereços do navegador a URL de outro contexto ao qual pertence e pressionar a tecla Enter.

**02.** Será apresentada a página de confirmação. Para confirmar a troca, acionar **Sim, trocar**. Para retornar ao contexto que estava sendo acessado, acionar **Não, continuar aqui**.

#f2f2f2#f2f2f2

Caso tenha se autenticado no contexto utilizando a senha do Active Directory ou Desktop SSO, ao fazer a troca pode ser preciso digitar a senha pessoal ou do Active Directory da empresa que pretende acessar. Não é solicitado novo login quando logado com senha pessoal.

Se tiver configurado o acesso com autenticação multifator, também será necessário informar o código de verificação gerado no aplicativo .

]]>
