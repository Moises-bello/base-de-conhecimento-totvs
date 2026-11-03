---
content_hash: bd8b22905cbecd178492a196e23a0b22d908369c4f2affb361d4567d0e744188
fetched_at: '2026-06-28T21:35:24.718318+00:00'
page_id: '271182916'
product: fluig
source: tdn-fluig
title: Eventos Sociais
type: documentation
url: https://tdn.totvs.com/display/fluig/Eventos+Sociais
version: 27
---

true.\*ndicenone

## Conhecendo e utilizando eventos sociais

---

Veja a seguir o vídeo *How to* demonstrando a utilização de eventos sociais.

854480

## Eventos

---

### beforeSocialShare

Este evento é disparado sempre antes da efetivação do compartilhamento de um objeto social.

Observação

Pode-se alterar a mensagem de compartilhamento passando uma String para o método setText( <valor> ) do objeto "share".

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| share | objeto de socialização | [SocialShareEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialShareEventVO) |

****Exemplo de Implementação****

jstrue

### afterSocialShare

Esse evento é disparado sempre após a efetivação de um compartilhamento.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| share | objeto de socialização | [SocialShareEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialShareEventVO) |

****Exemplo de Implementação****

jstrue

### beforeSocialComment

Esse evento é disparado sempre antes da efetivação de um comentário.

Observação

Pode-se alterar a mensagem de compartilhamento passando uma String para o método setText( <valor> ) do objeto "comment".

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| comment | objeto de comentário | [SocialCommentEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommentEventVO) |

****Exemplo de Implementação****

jstrue

### afterSocialComment

Esse evento é disparado sempre após a efetivação de um comentário.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| comment | objeto de comentário | [SocialCommentEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommentEventVO) |

**Exemplo de Implementação**

jstrue

### beforeSocialPost

Esse evento é disparado sempre antes da efetivação de um post.

Observação

Pode-se alterar o conteúdo da publicação passando uma String para o método setText( <valor> ) do objeto "post".

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| post | Objeto que representa a publicação | [SocialPostEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialPostEventVO) |

**Exemplo de Implementação**

jstrue -1) {
post.setText(post.getText().replace( " fluid ", " fluig "));
}
var sociables = post.getSociables();
for (var i = 0; i < sociables.size(); i++) {
var sociable = sociables.get(i);
log.info("sociable id: " + sociable.getId());
}
}]]>

### afterSocialPost

Esse evento é disparado sempre após a efetivação de um comentário.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| post | objeto de post | [SocialPostEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialPostEventVO) |

**Exemplo de Implementação**

jstrue -1) {
log.info(post.getUser() + " has published a content.");
}
}]]>

### beforeSocialPostRemove

Esse evento é disparado sempre antes da efetivação de uma remoção de um post.

**Exemplo de Implementação**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| post | objeto de post | [SocialPostEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialPostEventVO) |

**Exemplo de Implementação**

jstrue -1) {
throw "You cannot remove a post marked as important.";
}
}]]>

### afterSocialPostRemove

Esse evento é disparado sempre após a efetivação de uma remoção de um post.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| post | objeto de post | [SocialPostEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialPostEventVO) |

**Exemplo de Implementação**

jstrue

### beforeSocialDenounce

O evento é disparado quando um *Sociable* é denunciado porém antes que a ação seja efetivada.

**Exemplo de uso:**

* Em uma comunidade em que as publicações não podem ser denunciadas pode-se utilizar este evento para bloquear a ação de denúncia.
* Pode-se limitar a quantidade de denúncias que um usuário pode efetuar por dia para evitar que alguma pessoa mal intencionada denuncie todas as publicações.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` denounce ``` | objeto de post | [SocialDenounceEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialDenounceEventVO) |

**Exemplo de Implementação**

jstrue -1) {
throw "You cannot denounce posts about CIPA.";
}
}]]>

### afterSocialDenounce

O evento é disparado após a efetivação de uma ação de denúncia de um *sociable*.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` denounce ``` | objeto de post | [SocialDenounceEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialDenounceEventVO) |

**Exemplo Prático:**

Registrar em log as denúncias efetuadas para auditoria.

**Exemplo de Implementação**

jstrue

### beforeSocialLike

O evento é disparado antes de ser efetivada uma ação de "curtir" de um *sociable*.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` like ``` | Objeto com dados do sociable curtido | [SocialLikeEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialLikeEventVO) |

**Exemplo de Implementação**

jstrue -1) {
throw "You can not like a post that has this type of comment.";
}
}]]>

### afterSocialLike

O evento é disparado após a efetivação de uma ação de "curtir" de um *sociable*.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` like ``` | Objeto com dados do sociable curtido | [SocialLikeEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialLikeEventVO) |

**Exemplo Prático:**

Registrar em log para auditoria todas as publicações curtidas.

**Exemplo de Implementação**

jstrue

### beforeSocialUnlike

O evento é disparado antes de ser efetivada uma ação de "descurtir" de um *sociable*.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` unlike ``` | Objeto com dados do sociable descurtido | [SocialLikeEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialLikeEventVO) |

**Exemplo de Implementação**

jstrue

### afterSocialUnlike

O evento é disparado após a efetivação de uma ação de "descurtir" de um *sociable*.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` unlike ``` | Objeto com dados do sociable descurtido | [SocialLikeEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialLikeEventVO) |

**Exemplo Prático:**

Registrar em log para auditoria todas as publicações que deixaram de ser apoiadas.

**Exemplo de Implementação**

jstrue

### beforeSocialCommentRemove

O evento é disparado antes da efetivação da remoção de um comentário de um *sociable*.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` comment ``` | Objeto que contém as informações do comentário | [SocialCommentEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommentEventVO) |

**Exemplo Prático:**

Evitar que usuários removam seus comentários em uma publicação de campanha interna da empresa.

**Exemplo de Implementação**

jstrue -1) {
throw "You cannot change your guess.";
}
}]]>

### afterSocialCommentRemove

O evento é disparado após a efetivação da ação de remover o comentário de um *sociable*.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` comment ``` | Objeto que contém as informações do comentário | [SocialCommentEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommentEventVO) |

**Exemplo Prático:**

Registrar em log para auditoria todos os comentários com a hashtag "protesto".

**Exemplo de Implementação**

jstrue -1) {
log.info(comment.getUser() + " has removed the comment " + comment.getText() + " of the sociable " + comment.getSociable().getId());
}
}]]>

### beforeSocialCommentEdit

Esse evento é disparado sempre antes da edição de um comentário.

**Estrutura do Evento**

jsEstrutura do Evento

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` comment ``` | Objeto que contém as informações do comentário | [SocialCommentEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommentEventVO) |

**Exemplo de Implementação**

js

### afterSocialCommentEdit

Esse evento é disparado sempre após a edição de um comentário.

**Estrutura do Evento**

js

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` comment ``` | Objeto que contém as informações do comentário | [SocialCommentEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommentEventVO) |

**Exemplo de Implementação**

js

### beforeSocialPostEdit

Esse evento é disparado sempre antes da edição de um post.

**Estrutura do Evento**

jsEstrutura do Evento

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| post | objeto de post |  |

**Exemplo de Implementação**

js

### afterSocialPostEdit

Esse evento é disparado sempre após a edição de um post.

**Estrutura do Evento**

js

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| post | objeto de post |  |

**Exemplo de Implementação**

js

### beforeCommunityParticipation

O evento é disparado antes da efetivação da participação em uma comunidade.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` relation ``` | Objeto que contém as informações de participação | [SocialCommunityRelationEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommunityRelationEventVO) |

**Exemplo de Implementação**

jstrue

### afterCommunityParticipation

O evento é disparado após a efetivação da participação em uma comunidade.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` relation ``` | Objeto que contém as informações de participação | [SocialCommunityRelationEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommunityRelationEventVO) |

**Exemplo de Implementação**

jstrue

### beforeCommunityLeave

O evento é disparado antes da efetivação da exclusão de participação em uma comunidade.

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` relation ``` | Objeto que contém as informações de participação | [SocialCommunityRelationEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommunityRelationEventVO) |

**Exemplo de Implementação**

jstrue

### afterCommunityLeave

O evento é disparado após a efetivação da exclusão de participação em uma comunidade.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` relation ``` | Objeto que contém as informações de participação | [SocialCommunityRelationEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialCommunityRelationEventVO) |

**Exemplo de Implementação**

jstrue

### beforeSocialFollow

O evento é disparado antes da efetivação de seguir uma pessoa.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` follow ``` | Objeto que contém as informações de seguir | [SocialFollowEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialFollowEventVO) |

**Exemplo de Implementação**

jstrue

### afterSocialFollow

O evento é disparado após a efetivação de seguir uma pessoa.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` follow ``` | Objeto que contém as informações de seguir | [SocialFollowEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialFollowEventVO) |

**Exemplo de Implementação**

jstrue

### beforeSocialUnfollow

O evento é disparado antes da efetivação de deixar de seguir uma pessoa.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` follow ``` | Objeto que contém as informações de seguir | [SocialFollowEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialFollowEventVO) |

**Exemplo de Implementação**

jstrue

### afterSocialUnfollow

O evento é disparado após a efetivação de deixar de seguir uma pessoa.

**Estrutura do Evento**

jstrue

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` follow ``` | Objeto que contém as informações de seguir | [SocialFollowEventVO](http://tdn.totvs.com/display/public/fluig/Desenvolvimento%20de%20Eventos?null#DesenvolvimentodeEventos-SocialFollowEventVO) |

**Exemplo de Implementação**

jstrue

### beforeSocialPictureChange

O evento é disparado antes da imagem de um usuário/comunidade ser alterada.

**Estrutura do Evento**

js

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` vo ``` | Objeto contendo os dados da imagem a ser alterada |  |

**Exemplo de Implementação**

js

### afterSocialPictureChange

O evento é disparado após a efetivação da troca de imagem do perfil de um usuário/comunidade.

**Estrutura do Evento**

js

**Parâmetros da função**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| ``` vo ``` | Objeto contendo os dados da imagem a ser alterada |  |

**Exemplo de Implementação**

js
