---
content_hash: 899b242c29a39c301313b9e94b4e5b5f7be843ad1c4100acb4e27ff5f4045eab
fetched_at: '2026-06-28T21:35:19.496504+00:00'
page_id: '208340727'
product: fluig
source: tdn-fluig
title: ESB - Como alterar usuário e senha padrão do TOTVS ESB após a instalação?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208340727
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS ESB

# Ocorrência

Ao instalar o TOTVS ESB, o mesmo vem com um usuário e senha padrão. Como alterar a senha?

# Solução

* Acesse o diretório de instalação do TOTVS ESB e a pasta **conf**;
* Edite o arquivo **users.xml**;
* Procure pela tag **<md5 password>**. Nessa tag a senha fica armazenada.

Importante

A senha informada nesse arquivo deve ser criptografada em **md5**.

Você pode procurar pelo termo "gerador hash md5" na internet para encontrar serviços que possam criptografar a senha.

* Após o procedimento a senha sua senha será alterada.
