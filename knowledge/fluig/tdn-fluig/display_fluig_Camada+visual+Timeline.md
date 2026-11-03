---
content_hash: 4dee4b7e71667ede052eea6e859ce98d89a4985b70bb6621090fd50c38574785
fetched_at: '2026-06-28T21:35:17.651459+00:00'
page_id: '113804460'
product: fluig
source: tdn-fluig
title: Camada visual Timeline
type: documentation
url: https://tdn.totvs.com/display/fluig/Camada+visual+Timeline
version: 51
---

# Índice

true.\*ndicenone

## Arquivos básicos da Timeline

Como todos os componentes do TOTVS Fluig Plataforma, a Timeline é desenvolvida baseada no *framework* de *templates* [FreeMarker](http://freemarker.org/) (.ftl). O FreeMarker é responsável pela camada de visualização, onde sobre ele é escrito todo HTML do componente. Bem como o(s) arquivo(s) de [FreeMarker](http://freemarker.org/), todos os componentes possuem arquivos próprios de CSS (.css) e JavaScript (.js).

## Ação de edição

No modo de edição da *timeline* você pode configurar as opções de visualização.

## Ação de visualização

Após gerar uma nova publicação, esse conteúdo é exibido na Timeline em diferentes tipos de visualização:

### Estrutura básica de templates Mustache na timeline

html/xmlNo HTML- {{#postHeader}}

  ##### ...

  {{/postHeader}}
  {{#text}}

  {{{text}}}

  {{/text}}
  {{#variableContent}}
  {{>postContent}}
  {{/variableContent}}

  * ...

  {{#comments}}
  {{>postComments}}
  {{/comments}}
  {{#existsMoreComments}}
  {{>postMoreComments}}
  {{/existsMoreComments}}
]]>

### Tipos de Publicação

Segue abaixo os tipos de Publicação disponíveis na Timeline.

#### Novo Artigo criado

#### Publicação na Comunidade

#### Publicação Compartilhada

#### Publicação com Imagem

#### Publicação com vídeo

#### Publicação com vídeo do YouTube

#### Publicação com Menção e Hashtag

#### Modal para Compartilhamento da Publicação

### Estrutura básica de template Mustache de comentário em uma Publicação

html/xmlNo HTML- [...]({{tenantURI}}/{{user.page}})

  ##### ...

  {{{comment}}}

  * ...
]]>

### Comentário

Segue abaixo o tipo de Comentário de Publicação disponível na Timeline.

#### Comentário de uma Publicação
