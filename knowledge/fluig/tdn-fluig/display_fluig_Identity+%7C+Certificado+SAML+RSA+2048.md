---
content_hash: f6de6ff50e88df78d28d59a88793dce15347eb61134132c63cba928b2511e007
fetched_at: '2026-06-28T21:35:28.850983+00:00'
page_id: '698287879'
product: fluig
source: tdn-fluig
title: Identity | Certificado SAML RSA 2048
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Certificado+SAML+RSA+2048
version: 18
---

# Falando do certificado SAML RSA 2048

---

SAML (*Security Assertion Markup Language*) é um mecanismo de autenticação segura de padrão aberto, baseado em XML para a troca de dados de autenticação e autorização de acesso entre um provedor de identidade (*Identity Provider* ou IDP), que atesta e certifica a identidade dos usuários, e um provedor de serviços (*Service Provider* ou SP). Se tratando de segurança, o certificado RSA 2048 se destaca pelo nível de segurança de sua criptografia, contando com uma chave de 2048 bits.

O Identity suporta o *Single Sign On* (SSO) baseado no SAML 2.0 e a autenticação pode ser iniciada tanto pelo SP quanto pelo IDP.

Por motivos de segurança, uma data de expiração é atribuída ao certificado. A duração atual do certificado é de 10 anos a partir da data de criação do contexto. Ao final desse período, é necessário renová-lo e atualizá-lo nas aplicações SSO.

## Criar o certificado SAML RSA 2048 em uma empresa nova ou já existente

---

**Veja o vídeo**

**01.** Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Certificado SAML.**

**03**. Acione a aba **Certificado SAML RSA 2048** e clique no botão **RSA 2048.**

#f2f2f2#f2f2f2

Será apresentada uma página para confirmação do usuário. Leia atentamente a mensagem de confirmação antes de prosseguir com a renovação.

**04.** Marque a opção **Li e concordo com a criação do certificado.**

**05.** Clique em **Criar.**

#f2f2f2#f2f2f2

Após a criação, será apresentado um alerta informando que o certificado foi renovado com sucesso e ficará disponível as opções de  Ao se tratar de uma empresa nova ou já existente, ficará visível a informação que o  e o mesmo será apresentado para ativação.

## Obter o certificado SAML RSA 2048

---

**01.** Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Certificado SAML.**

**03**. Acione a aba **Certificado SAML RSA 2048** e clique em **Download do certificado** para obter o certificado SAML da empresa.

#f2f2f2#f2f2f2

Este certificado pode ser utilizado para configurar a autenticação SAML entre o Identity e outras aplicações que suportem esse padrão, como o .

Os campos **Renovado em** e **Vence em** exibem, respectivamente, a data de renovação (ou criação) do certificado e a data de validade.

## Renovar o certificado SAML RSA 2048

---

**01.** Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Certificado SAML.**

**03**. Acione a aba **Certificado SAML RSA 2048** e clique em **Renovar certificado**.

#f2f2f2#f2f2f2

Leia atentamente a mensagem de confirmação antes de prosseguir com a renovação.

**04.** Marque a opção **Li e concordo com a renovação do certificado.**

**05.** Clique em **Renovar.**

#f2f2f2#f2f2f2

Os campos **Renovado em** e **Vence em** serão atualizados, respectivamente com a data atual em que o certificado foi renovado e a nova data de validade será de 10 anos após a renovação. Será necessário atualizar o certificado em todas as aplicações SSO integradas ao contexto.  para mais informações.

]]>
