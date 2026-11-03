---
content_hash: dfcd76c41449516cc14191a2241c25233f031f3904c1f4ee303d01710275cc21
fetched_at: '2026-06-28T21:35:27.357872+00:00'
page_id: '544184349'
product: fluig
source: tdn-fluig
title: Identity | Certificado SAML
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Certificado+SAML
version: 11
---

# Falando de certificado SAML...

---

SAML (*Security Assertion Markup Language*) é um mecanismo de autenticação segura de padrão aberto, baseado em XML para a troca de dados de autenticação e autorização de acesso entre um provedor de identidade (*Identity Provider* ou IDP), que atesta e certifica a identidade dos usuários, e um provedor de serviços (*Service Provider* ou SP).

O Identity suporta o *Single Sign On* (SSO) baseado no SAML 2.0 e a autenticação pode ser iniciada tanto pelo SP quanto pelo IDP.

Por motivos de segurança, uma data de expiração é atribuída ao certificado. A duração atual do certificado é de 10 anos a partir da data de criação do contexto. Ao final desse período, é necessário renová-lo e atualizá-lo nas aplicações SSO.

oculto

**Observação interna:**

O conteúdo dessa página foi replicado ao artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360033487714/>

Se for realizado algum ajuste, lembrar de repassar a esse artigo!

## Obter o certificado SAML

---

**Assista ao vídeo**

**01.** Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Certificado SAML.**

**03**. Acione ***Download* do certificado** para obter o certificado SAML da empresa.

#f2f2f2#f2f2f2

Este certificado pode ser utilizado para configurar a autenticação SAML entre o Identity e outras aplicações que suportem esse padrão, como o .

Os campos **Renovado em** e **Vence em** exibem, respectivamente, a data de renovação (ou criação) do certificado e a data de validade.

## Renovar o certificado SAML

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Certificado SAML.**

**03**. Acione **Renovar certificado**.

#f2f2f2#f2f2f2

Leia atentamente a mensagem de confirmação antes de prosseguir com a renovação.

**04.** Marque a opção **Li e concordo com a renovação do certificado**.

**05.** Acione **Renovar.**

#f2f2f2#f2f2f2

Os campos **Renovado em** e **Vence em** serão atualizados, respectivamente, com a data atual em que o certificado foi renovado e a nova data de validade (10 anos após a renovação). Será necessário atualizar o certificado em todas as aplicações SSO integradas ao contexto.  para mais informações.

]]>
