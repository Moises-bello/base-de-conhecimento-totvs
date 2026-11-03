---
content_hash: 5686be7e59ffe8c630b40c26a7d1125d317ad997483edb5186bc96bf3495fab7
fetched_at: '2026-06-28T21:35:24.230698+00:00'
page_id: '269068084'
product: fluig
source: tdn-fluig
title: SOC - Como receber notificações de documentos publicados em uma comunidade?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269068084
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

# Ocorrência

Quando um post é publicado em uma comunidade todos os usuários estão recebendo notificação e e-mail, porém quando um documento é publicado ninguém é notificado. Por que isso acontece e como resolver?

# Causa

As notificações da plataforma, push ou e-mail sobre as novas publicações em comunidades são enviadas quando a opção **Notificação de publicação na comunidade** está marcada na aba **Colaboração**na tela **Configurar notificações** (do Painel de Controle) e em **Configuração de Notificações** (na central de notificações do usuário) .

**Figura 1 - Configuração de notificação de novas publicações no Painel de Controle**

**Figura 2 - Configuração de notificação de novas publicações no perfil do usuário**

Quando a comunidade permite a publicação de documentos e um usuário faz um post adicionando um documento, todos que possuírem a notificação de publicação habilitada receberão um aviso. Se o documento é publicado diretamente na aba Documentos, a notificação é enviada apenas se as notificações de Documentos estiverem devidamente configuradas.

Confira abaixo como configurar essa notificação.

# Solução

0.5falsesamplesfadetrue1Passo 1 - Configurar notificações

Com um usuário administrador do fluig acesse **Painel de Controle > Colaboração > Notificações > aba Documentos**;

Ative a notificação por e-mail do item **Documento publicado com o assunto que acompanho**.

**Figura 3 - Configuração de notificações no Painel de Controle**

2Passo 2 - Configurar Assunto

Agora configure o assunto que poderá ser utilizado nos documentos.

Acesse **Painel de Controle > Documentos > Assuntos**. Acione **Adicionar** para incluir um novo.

**Figura 4 - Configurar Assunto**

3Passo 3 - Criar novo Assunto

Na tela de novo assunto preencha o campo **Nome**.

Se quiser que os usuários sejam notificados também quando um documento for atualizado ou removido marque as opções **Notifica atualização** e **Notifica eliminação**.

Defina para quem o assunto é destinado. Escolha **Todos Usuários** ou clique em **Adicionar** para escolher entre os grupos de usuários já cadastrados na plataforma.

Se o assunto precisar ser obrigatório, marque a opção **Obrigatório** ao lado do grupo correspondente.

Quando o assunto é obrigatório, ele será automaticamente configurado no perfil dos usuários do grupo como assunto que eles acompanham. Isso significa que eles não podem alterar manualmente essa configuração e deixar de acompanhar esse assunto.

Caso o assunto não seja obrigatório, usuários que pertencem aos grupos selecionados pelo administrador poderão habilitar o assunto através da opção Editar perfil (vide Passo 4).

**Figura 5 - Criar novo Assunto obrigatório**

4Passo 4 - Editar perfil do usuário

No [perfil do usuário](http://tdn.totvs.com/display/HF/Editar+perfil) serão exibidos todos os Assuntos que ele tem permissão para acompanhar. Porém é necessário que o próprio usuário selecione de quais assuntos disponíveis ele deseja receber notificações, conforme apresentado na tela a baixo:

Quando o assunto é obrigatório, ele será automaticamente configurado no perfil dos usuários do grupo como assunto selecionado que eles acompanham.

Isso significa que eles não podem alterar manualmente essa configuração e deixar de receber notificações desse assunto.

Na imagem abaixo mostramos um exemplo de configuração de "Assuntos que acompanho" sendo eles:

* Assuntos disponíveis: que podem ter as notificações habilitadas pelo usuário;
* Assuntos selecionados: habilitados pelo usuário para receber notificações.

**Figura 6 - Edição do perfil do usuários para Assuntos que acompanho**

5Passo 5 - Publicar documento

Durante a publicação de um documento tanto na tela Documentos quanto na aba Documentos de uma comunidade, o usuário poderá configurar o Assunto do mesmo.

Se existir apenas um assunto cadastrado na plataforma ele será selecionado automaticamente, caso contrário o usuário precisa escolher qual deseja.

É importante lembrar de marcar a opção **Notificar?** para que as notificações desse documento sejam enviadas.

Para que os campos **Notificar?** e **Assunto** estejam preenchidos automaticamente, basta configurar as propriedades herdadas da pasta onde eles serão publicados. [Saiba mais aqui](http://tdn.totvs.com/x/afvuDQ).

Na imagem abaixo mostramos um exemplo de publicação de documento quando existe um assunto a mais cadastrado e as propriedades herdadas da pasta não estão configuradas.

**Figura 6 - Publicação de documento para o assunto desejado**

5Passo 5 - Visualização da notificação

Quando o documento for publicado o usuário receberá um e-mail e notificação conforme as imagens abaixo.

**Figura 7 - Notificação recebida por e-mail**

**Figura 8 - Notificação da plataforma**
