---
content_hash: bbb0bb072651dbf12279483ffc7004630aed5694ae8f98432e220d47e0b24928
fetched_at: '2026-06-28T21:35:19.125686+00:00'
page_id: '192090791'
product: fluig
source: tdn-fluig
title: SOC - Por que usuário não é adicionado na comunidade?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=192090791
version: 13
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

# Ocorrência

Ao adicionar um usuário ou usuários por grupo diretamente na comunidade é apresentada a mensagem de que o usuário foi adicionado com sucesso. Porém o usuário não vai para a lista de participantes da comunidade.

**Figura 1 - Opções para adicionar usuários na comunidade**

# Causa

Isto ocorre devido à plataforma Fluig fazer uma validação conferindo se o usuário existe no grupo de membros da comunidade antes de inserir. Como o usuário já existe no grupo ele não é adicionado novamente.

# Solução

Acessar o cadastro de grupos no **Painel de Controle**, selecionar o grupo de membros da comunidade com o erro (o nome do grupo será MEMBER\_nome-comunidade) e remover do grupo o usuário que não está sendo adicionado na comunidade. Em seguida volte a comunidade e insira o participante novamente.

# Observações

Os grupos MEMBER e MODERATOR que aparecem no **cadastro de grupos** não devem ser alterados por este menu, a menos que isto tenha sido solicitado pela equipe de Suporte Fluig, pois pode causar erros como o citado nesta FAQ. Além disso, a contagem de participantes na comunidade pode ficar diferente da contagem do grupo.
