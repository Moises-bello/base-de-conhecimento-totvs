---
content_hash: 4da4a8b06d707afc5906291bb3a806fe911ea033ebc60d572f045015fce09ed7
fetched_at: '2026-06-28T21:35:22.591598+00:00'
page_id: '237398691'
product: fluig
source: tdn-fluig
title: ARQ - Notificações via e-mail não estão sendo enviadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237398691
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

**Versão:** 1.5.x e 1.6

# Ocorrência

Notificações via e-mail mesmo após configurado, não estão sendo realizados.

# Causa

Servidor de e-mail configurado sem inserir os dados de autenticação do servidor SMTP.

# Solução

1. Acessar a plataforma com o usuário wcmadmin e acessar WCM > Empresas > Editar > E-mail.
2. Configurar o e-mail com os dados de autenticação do servidor STMP, conforme a documentação de
3. Reiniciar o serviço do fluig.

# Observação

Ao preencher os dados nas configurações de e-mail da empresa via wcmadmin, a plataforma irá sobrescrever o XML automaticamente após a reinicialização do serviço.
