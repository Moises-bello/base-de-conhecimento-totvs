---
content_hash: 36477e5c116b95af10fa7c4a5b2f13254affb48e0574d8886513ad0cd3c17a66
fetched_at: '2026-06-28T21:35:19.833745+00:00'
page_id: '223926925'
product: fluig
source: tdn-fluig
title: ARQ - Usuário recebeu um erro de envio de e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223926925
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**  TOTVS Fluig Plataforma

# Ocorrência

Uma atividade foi atribuída para um usuário, o usuário recebeu a notificação de atividade na plataforma, mas não recebeu o e-mail informativo.

Além disso, o usuário que enviou a atividade recebeu um erro de envio de e-mail (Figura 1).

**Figura 1 - Mensagem contendo o erro do servidor de e-mail.**

# Causa

O e-mail recebido pelo usuário que enviou a atividade é uma resposta do servidor de e-mail.

O código SMTP 550 retornado pelo servidor de email geralmente significa que o e-mail do destinatário não existe. Esta é uma descrição genérica desse código, pois depende de como o servidor de e-mail trata os erros. Em alguns casos existem algumas diferenças, como por exemplo o servidor de email tenha ficado *offline*, ou indisponível por algum motivo.

Mas de maneira geral, o código 550 significa que o usuário não existe/não foi encontrado.

# Solução

Verificar no cadastro de usuários se o e-mail do destinatário existe e é válido e também checar a disponibilidade e estabilidade do servidor de e-mail.
