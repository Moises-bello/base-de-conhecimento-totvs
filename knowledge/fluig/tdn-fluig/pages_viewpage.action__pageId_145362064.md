---
content_hash: ebe5ab9027e727cb63e9cc4bec1bc5e8be4ecc3d1c46a14846a3fd086e3c9b49
fetched_at: '2026-06-28T21:35:17.989118+00:00'
page_id: '145362064'
product: fluig
source: tdn-fluig
title: Personalizando o template de e-mail padrão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=145362064
version: 15
---

# Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é orientar a personalização de *templates* e cabeçalhos dos *e-mails* que são enviados pelo TOTVS Fluig Plataforma.

Plataforma TOTVS Fluig em cloud

Caso a plataforma seja hospedada em cloud, para solicitar os arquivos para personalização, é preciso acionar a equipe de Cloud. Eles disponibilizam a pasta do Volume ao cliente e recebem os arquivos alterados, que serão substituídos no ambiente cloud.

# Personalização do template de e-mail

---

Todos os *templates* contidos no diretório **<volume padrão>\templates\tplmail\** podem ser personalizados, contanto que não sejam alteradas e nem removidas as tags padrões de cada *template,* conforme o do exemplo abaixo:

# Desenvolvendo o cabeçalho de e-mails

---

Para clientes que já possuem a plataforma instalada e desejam personalizar o cabeçalho dos *templates* de *e-mail*, é necessário efetuar os passos abaixo:

1. Para alterar a imagem do cabeçalho dos *e-mails*, substitua a imagem **head\_background.gif** existente em: **<volume padrão>\custom\assets\** por outra imagem com o mesmo nome e extensão.

Atenção!

Ressaltamos que no processo de atualizações da plataforma as personalizações realizadas nos *templates* serão perdidas.

É de grande importância realizar um *backup* da pasta **<volume padrão>\templates\tplmail\** para que as personalizações existentes possam ser recuperadas posteriormente.
