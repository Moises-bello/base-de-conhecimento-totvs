---
content_hash: 16f48e75f11747109841659341cdcf731b24602173014245ac2574ba285aeb71
fetched_at: '2026-06-28T21:35:18.772637+00:00'
page_id: '185732957'
product: fluig
source: tdn-fluig
title: Estrutura de páginas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185732957
version: 39
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar os elementos que constituem a estrutura de uma página no TOTVS Fluig Plataforma.

# Elementos de uma Página

O Fluig Plataforma é constituído de páginas e essas possuem os seguintes elementos: *Layout*, *Slots* e *Widgets*.

Uma página é constituída de um *layout*, que por sua vez possui *slots* que definem o posicionamento e a disposição dentro do *layout* onde os *widgets* são inseridos. Toda página permite definir o o modo de visualização como pública ou privada.

# Página privada

Para determinar que uma página esteja acessível apenas aos usuários autenticados na plataforma, ao criá-la ou editá-la basta selecionar a opção "AUTHENTICATED" no campo "Autorização". Desta maneira, somente usuários autenticados terão acesso a esta página.

Caso um usuário acesse uma página cuja autorização seja *Authenticated* sem estar autenticado, ele será redirecionado para a página de login. Somente após a autenticação ele poderá visualizar a página solicitada.

**Criação de páginas - Autorização: AUTHENTICATED**

Como fica a URL?

Considerando os seguintes dados:

| Elemento | Valor |
| --- | --- |
| Nome do servidor | meuserver.com.br |
| Porta utilizada pelo Fluig server | **8080** |
| Código da empresa corrente | **001** |

A URL desta página ficará assim: <http://meuserver.com.br:8080/portal/p/001/campanha_agasalho>

Onde:

| Elemento | Descrição |
| --- | --- |
| /portal | Valor fixo da plataforma. |
| /p | Indicativo de página privada. |
| campanha\_agasalho | É o campo "Identificador único" do cadastro de página. |

# Página pública

Para determinar que uma página seja acessada também por usuários que não estejam autenticados, ao criá-la ou editá-la, basta selecionar a opção "PUBLIC" no campo "Autorização". Desta maneira, usuários visitantes e autenticados conseguem visualizar a página pública.

Dica!

Para criar páginas públicas, em vez de utilizar esse recurso, você pode utilizar o recurso [Pages Beta](http://tdn.totvs.com/x/qwqVGQ), que oferece diversos *templates* e componentes que facilitam a configuração das suas páginas.

**Criação de páginas - Autorização: PUBLIC**

Como fica a URL?

Considerando os seguintes dados:

| Elemento | Valor |
| --- | --- |
| Nome do servidor | [meuserver.com.br](http://meuserver.com.br) |
| Porta utilizada pelo Fluig server | **8080** |
| Código da empresa corrente | **001** |

A URL desta página ficará assim: [http://meuserver.com.br:8080/portal/001/campanha\_agasalho](http://meuserver.com.br:8080/portal/p/001/campanha_agasalho)

Onde:

| Elemento | Descrição |
| --- | --- |
| /portal | Valor fixo da plataforma |
| campanha\_agasalho | É o campo "Identificador único" do cadastro de página. |

A ausência do elemento **"/p"** indica que o acesso a essa página será público, ou seja, sem autenticação.

# PathParam

A plataforma Fluig permite que uma página contenha parâmetros em sua URL de forma que seja possível recuperá-los em um *layout* ou qualquer *widget* inserido na página. Cada parâmetro é nomeado pelo formato "p" seguido da sua ordem na URL, por exemplo, "p1", "p2", "p3", etc. É possível recuperar cada parâmetro na URL diretamente no seu *template* Freemarker.

Por exemplo: [http://meufluig.com/portal/p/meutenant/reservadesala/sala73/08:00/12:00](http://meufluig.com/portal/p/meutenant/minhapagina/meuparametro1/meuparametro2/meuparametro3)

| URL | Descrição | Variável no template Freemarker |
| --- | --- | --- |
| [http://meufluig.com/portal/p/meutenant/reservadesala](http://meufluig.com/portal/p/meutenant/minhapagina/meuparametro1/meuparametro2/meuparametro3) | Endereço da página com identificador único "reservadesala" | - |
| sala73 | Valor do parâmetro "p1" | *${p1}* |
| 08:00 | Valor do parâmetro "p2" | *${p2}* |
| 12:00 | Valor do parâmetro "p3" | *${p3}* |

Dica Freemarker

Para evitar erros na renderização do *template* Freemarker, deve-se [fornecer um valor padrão](http://freemarker.org/docs/dgui_template_exp.html#dgui_template_exp_missing_default) caso o PathParam não esteja presente na URL de acesso.

Exemplo: *${p1|"sala01"}*

# Definir comportamento distinto para um *widget* em páginas públicas ou autenticadas

É possível desenvolver um *widget* para que ele se comporte de forma diferente quando estiver em um contexto privado *(***com** "/p" na URL*)* ou público *(***sem** "/p" na URL*).* Para esses casos, pode-se utilizar os seguintes comandos:

No arquivo **\*.js**:

js

No arquivo **\*.ftl**:

xml

<#else>
]]>

# *Layout*

Toda página da plataforma Fluig é constituída por um *layout* que define a estrutura dela o que diz respeito ao posicionamento e ao tamanho dos *slots*.

Para saber mais acesse o guia sobre .

# *Slots*

Os *slots* servem para organizar os *widgets* dentro de um *layout*. Eles são áreas pré-definidas dentro do *layout* onde os *widgets* podem ser distribuídos na ordem desejada para atender a cada necessidade.

Para saber mais acesse o guia sobre *[Slots](http://tdn.totvs.com/display/fluig/Layouts#Layouts-Slot).*

# *Widgets*

Dentro de uma página os *widgets* são os componentes concretos, que podem exibir e consultar informações, variando de componente para componente.

Para saber mais acesse o guia sobre .
