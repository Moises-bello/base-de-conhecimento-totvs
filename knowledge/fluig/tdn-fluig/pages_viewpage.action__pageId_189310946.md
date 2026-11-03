---
content_hash: abe08781e3f3757b0626e01472451ce5ea224f23073a5fb7b5e8bea6cf3d81e5
fetched_at: '2026-06-28T21:35:19.059226+00:00'
page_id: '189310946'
product: fluig
source: tdn-fluig
title: ECM - Usuários não recebem e-mails sobre aprovação de documentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189310946
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto**: TOTVS Fluig Plataforma

# Ocorrência

Usuários não recebem e-mails referentes a aprovação de documentos.

# Causa

Esse problema pode acontecer porque o envio de e-mails gerais ou especificamente de aprovação de documentos não está habilitado na plataforma.

# Solução

O primeiro passo é verificar se o envio de e-mails está habilitado. Para isso acesse o ambiente com um usuário administrador e:

* Acesse o **Painel de Controle** > agrupador **Pessoas** > **Notificações**. Em atualizações anteriores à 1.6.5 (Liquid), essa tela se encontrava na aba **Colaboração** do **Painel de Controle.**

* Altere o valor para ON no campo "Defina os meios de notificação disponíveis".

Além dessa configuração, o usuário que será o aprovador do documento também precisa manter as opções de recebimento de e-mails habilitadas. Por padrão, todos os e-mails são habilitados para envio, porém o usuário pode alterá-los no seu perfil de acordo com sua necessidade.   
  
Para que ele confira se receberá e-mails de notificação de aprovação peça que ele acesse a plataforma e pare o cursor do mouse sobre o ícone de notificações no alto da tela, clique no ícone de engrenagem e em Notificações.

Na área de Documentos existem as opções de documento aprovado ou em aprovação. Ele deve manter os e-mail referentes a aprovação habilitados.

Caso o problema persista após estas configurações, é recomendável revisar as [configurações de envio de e-mail](http://tdn.totvs.com/x/CAZbDw).
