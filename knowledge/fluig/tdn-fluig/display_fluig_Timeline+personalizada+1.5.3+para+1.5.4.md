---
content_hash: c75293b2a48a1217b089e861b0fa3c61903ae805bd69ee74a308cde150b26fcc
fetched_at: '2026-06-28T21:35:19.527596+00:00'
page_id: '211061719'
product: fluig
source: tdn-fluig
title: Timeline personalizada 1.5.3 para 1.5.4
type: documentation
url: https://tdn.totvs.com/display/fluig/Timeline+personalizada+1.5.3+para+1.5.4
version: 13
---

# Índice

true.\*ndicenone

# Objetivo

Este guia é destinado aos desenvolvedores internos e externos do fluig. O objetivo é identificar e mapear todas as diferenças da *Timeline* personalizada entre as versões 1.5.3 e 1.5.4.

Dica

Sugerimos que ao seguir este guia seja utilizado um programa de comparação (diff), que permita visualizadas as diferenças entre as versões 1.5.3 e 1.5.4.

# application.info

Na versão 1.5.4 foi adicionado o novo componente de visualização de artigo, sendo necessário adicionar esta dependência para *widget*.

A linha abaixo, deve ser **ADICIONADA** para a versão 1.5.3:

xmlAtenção!

Não esquecer de substituir o 'X' pela sequência dos componentes já configurados.

# socialtimeline.properties

Na versão 1.5.4 foi adicionada uma chave de tradução e alterada outra, e devem ser **ADICIONADA/ALTERADA** para versão 1.5.3.

Não esquecer de replicar as alterações para os arquivos: socialtimeline\_en\_US.properties, socialtimeline\_es.properties, socialtimeline\_pt\_BR.properties.

Veja abaixo:

**Alterar:**

xml

**Adicionar:**

xml

# view.ftl

Na linha 40 da versão 1.5.4, copiar o código abaixo e **SUBSTITUIR** na versão 1.5.3:

xml]]>

Na linha 94 da versão 1.5.4, copiar o bloco abaixo e **SUBSTITUIR** na versão 1.5.3:

xml

{{#supported}}
{{/supported}}
{{^supported}}
{{/supported}}
[{{numberLikes}}](# "{{i18n.manylike}}")
{{/canLike}}
{{#canComment}}- [{{numberComments}}]({{tenantURI}}{{url}} "{{i18n.manycomment}}")
{{/canComment}}
{{#canNotify}}- {{#watching}}
  {{/watching}}
  {{^watching}}
  {{/watching}}
  [{{numberWatchers}}](# "{{i18n.manywatch}}")
{{/canNotify}}
{{#canShare}}- {{#shared}}
  {{/shared}}
  {{^shared}}
  {{/shared}}
  [{{numberShares}}](# "{{i18n.manywatch}}")
{{/canShare}}
{{#canDenounce}}
{{/canDenounce}}
]]>

Na linha 196 da versão 1.5.4, copiar o bloco abaixo e **SUBSTITUIR** na versão 1.5.3:

xml

{{#supported}}
{{/supported}}
{{^supported}}
{{/supported}}
[{{numberLikes}}](# "{{i18n.manylike}}")
{{/canLike}}
{{#canDenounce}}
{{/canDenounce}}]]>

Na linha 419 da versão 1.5.4, copiar o código abaixo e **SUBSTITUIR** na versão 1.5.3:

xml
<#--ARTIGOS NOVOS, COM IMAGEM DE CAPA-->

{{#hasShareText}}

{{/hasShareText}}
{{#linkedObject.thumbURL}}

{{^hasShareText}} {{/hasShareText}}

[![]({{linkedObject.thumbURL}})]({{tenantURI}}{{linkedObject.url}})

{{/linkedObject.thumbURL}}

## [{{linkedObject.description}}]({{tenantURI}}{{linkedObject.url}})

{{linkedObject.text}}  
[{{i18n.details}}]({{tenantURI}}{{linkedObject.url}})

{{#hasShareText}}

{{/hasShareText}}

]]>

# socialtimeline.js

Na linha 24 da versão 1.5.4, copiar o conteúdo abaixo e **ADICIONAR** na versão 1.5.3:

js

Copiar a linha 88 da versão 1.5.4 e **ADICIONAR** na versão 1.5.3:

js

Copiar as linhas 165 até 189 da versão 1.5.4 e **ADICIONAR** na versão 1.5.3:

js

Copiar as linhas a partir da linha 294 da versão 1.5.4 e **ADICIONAR** na versão 1.5.3:

js

Na a partir da linha 354 da versão 1.5.4, copiar o bloco abaixo e **ADICIONAR** na versão 1.5.3:

js - 1;
},]]>

Copiar a partir da linha 358 da versão 1.5.4 e **SUBSTITUIR** na versão 1.5.3:

js

Copiar a partir da linha 851 da versão 1.5.4, copiar o bloco abaixo e **SUBSTITUIR** na versão 1.5.3:

js

Copiar a partir da linha 1271 da versão 1.5.4, copiar o bloco abaixo e **SUBSTITUIR** na versão 1.5.3:

js
