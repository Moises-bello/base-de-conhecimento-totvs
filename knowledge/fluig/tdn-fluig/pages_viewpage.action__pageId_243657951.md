---
content_hash: f344c27ba47359fdfb42dbc81e473c02d7b3ce01067d8a7ac08dca491785f7c0
fetched_at: '2026-06-28T21:35:23.082383+00:00'
page_id: '243657951'
product: fluig
source: tdn-fluig
title: ARQ - O que devo verificar quando ocorre o erro 'Authentication unsuccessful'
  no envio de e-mail?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243657951
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

A plataforma não está conseguindo mandar e-mail e no log tem-se o seguinte erro:

powershellEclipseMensagem no arquivo server.log

# Solução

Existem vários problemas que podem causar essa situação:

1. Configuração incorreta de usuário e senha: ;
2. Sua senha expirou: diversos sistemas de e-mail expiram automaticamente a senha após um determinado período. É recomendável a conta definida para o envio de e-mail seja configurada para não ter a senha expirada;
3. Configuração incorreta no servidor de e-mail: normalmente e-mails Exchange possuem uma permissão especial se elas vão enviar e-mail. Verifique com o administrador do servidor de e-mail se as configurações corretas foram estabelecidas para envio de e-mail.
