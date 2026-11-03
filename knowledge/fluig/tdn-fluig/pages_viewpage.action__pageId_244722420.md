---
content_hash: a51888b52b641adae4cfcd67d61e2c8feed2acfb8d3dc47f141252ba107261ec
fetched_at: '2026-06-28T21:35:23.254946+00:00'
page_id: '244722420'
product: fluig
source: tdn-fluig
title: IDE - Como conectar o servidor no Fluig Studio após integrar a plataforma ao
  Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244722420
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma integrado ao TOTVS Identity

# Ocorrência

Realizamos a integração da plataforma com o Identity e após isto passou a ser exibido o erro abaixo ao tentar conectar o Fluig Studio ao servidor da plataforma.

# Causa

Isto ocorre quando o e-mail utilizado para conexão do Fluig Studio está duplicado na base. Neste caso, foi cadastrado o mesmo e-mail para o usuário wcmadmin, da empresa 0. Assim, ao realizar a conexão, a plataforma Fluig encontra o usuário na empresa 0, onde o Identity não está habilitado, e não é possível autenticar.

# Solução

Nenhum e-mail pode estar duplicado na base do Fluig Plataforma ao realizar a integração com o Identity, este é um pré-requisito da configuração. Altere o e-mail do wcmadmin para um e-mail que não esteja cadastrado na plataforma.

Este cenário pode ocorrer em outros recursos da plataforma como por exemplo o Fluig Connect. Portanto, identificando este erro, verifique os e-mails cadastrados seguindo o pré-requisito de configuração da integração.
