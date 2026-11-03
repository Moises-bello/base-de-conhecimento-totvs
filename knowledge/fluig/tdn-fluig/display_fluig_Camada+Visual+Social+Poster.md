---
content_hash: dfa4cb7ea2627fdaf0b2018496972b4b736326ca748b1b2e245b77c0cd6bbb43
fetched_at: '2026-06-28T21:35:18.143986+00:00'
page_id: '150636072'
product: fluig
source: tdn-fluig
title: Camada Visual Social Poster
type: documentation
url: https://tdn.totvs.com/display/fluig/Camada+Visual+Social+Poster
version: 18
---

# Índice

true.\*ndicenone

### Arquivos básicos do widget Social Poster

O *widget* Social Poster é baseado no *framework* de *templates* [FreeMarker](http://freemarker.org/) (.ftl). O FreeMarker é responsável pela camada de visualização, onde sobre ele é escrito todo HTML do componente. Bem como o(s) arquivo(s) de [FreeMarker](http://freemarker.org/), todos os componentes possuem arquivos próprios de CSS (.css) e JavaScript (.js).

Além desses componentes, o *widget* Social Poster utiliza um componente de *template* chamado [Mustache](http://mustache.github.io/), que é uma especificação de *templates* que não utiliza lógica, ou seja, não possui declarações com *if, for, while* etc.; toda sua construção é baseada em *tags*.

### Ação de Publicação

O Social Poster é responsável por absorver todo o conteúdo digitado pelo usuário no Campo de Publicação e enviar para a exibição de uma nova publicação na *Timeline*.

### Ação de Publicação de Usuário

Ação de Publicação de Usuário é o campo de texto onde o usuário digita o conteúdo para publicação. Esse campo de texto está disponível na página inicial.

**Área de publicação de usuário**

### Área de publicação na Comunidade

Na publicação em comunidade, além de publicar conteúdo de texto, é possível anexar imagens, um vídeo, documento ou artigo de acordo com a disponibilidade desses recursos.

**Área de publicação de comunidade**

### Estrutura do widget Social Poster

Veja a seguir a estrutura que compõe o *widget* Social Poster:

xmlNo HTML

{{#socialStateBlocked}}
{{#socialTypeCommunity}}

${i18n.getTranslation('community.disabled')}

{{/socialTypeCommunity}}
{{#socialTypeUser}}

${i18n.getTranslation('user.disabled')}

{{/socialTypeUser}}
{{/socialStateBlocked}}
{{#socialStateActive}}
{{#socialAlias}}
{{#isUserOwnPageOrMember}}

![](/social/api/rest/social/imagetype/{{socialType}}/thumb/{{socialAlias}})




{{#socialTypeCommunity}}
{{/socialTypeCommunity}}



600


{{#socialTypeUser}}
${i18n.getTranslation('public')}
${i18n.getTranslation('follower')}
{{/socialTypeUser}}
{{#notSocialTypeUser}}
{{#socialPrivateContent}}
${i18n.getTranslation('member')}
{{/socialPrivateContent}}
{{#notSocialPrivateContent}}
${i18n.getTranslation('public')}
${i18n.getTranslation('member')}
{{/notSocialPrivateContent}}
{{/notSocialTypeUser}}

{{#socialStateBlocked}}
${i18n.getTranslation('profile.disabled')}
{{/socialStateBlocked}}
{{#notSocialStateBlocked}}
${i18n.getTranslation('publish')}
{{/notSocialStateBlocked}}

{{/isUserOwnPageOrMember}}
{{/socialAlias}}
{{/socialStateActive}}
