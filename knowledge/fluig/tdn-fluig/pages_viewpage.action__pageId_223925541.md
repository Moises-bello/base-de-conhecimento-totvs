---
content_hash: d2ce9ded6184cd47a82311c054ed7e00a0228f22d4b589ad8bbca3f2a72faad3
fetched_at: '2026-06-28T21:35:19.828543+00:00'
page_id: '223925541'
product: fluig
source: tdn-fluig
title: IDE - Mensagem "Exception extracting SAML" ao acessar aplicativo Fluig pelo
  Launchpad
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223925541
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma integrado ao TOTVS Identity

# Ocorrência

Após configurar a integração da plataforma ao Identity, e apesar de o teste de conexão apontar que a mesma está correta, ao clicar no aplicativo do Fluig é aberta a tela de login da plataforma com o erro abaixo:

# Causa

Este erro é gerado devido uma configuração incorreta no aplicativo Fluig no Identity.

# Solução

Na aba **Entrar** da configurações do aplicativo Fluig no Identity, os campos devem ser informados obrigatoriamente da seguinte maneira:

* **Modo de login**: SAML
* **Credencial**: Definido pelo usuário
* **Domínio**: http://[endereço\_fluig]:[porta]/portal/idp
* **Mapeamento Id de usuário**: E-mail do usuário

Consulte a documentação completa em .
