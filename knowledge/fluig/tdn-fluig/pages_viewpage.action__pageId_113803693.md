---
content_hash: 95fac45b4db15c84157cfd4f4cdb3967d3ffa6941114c020f2aa0a60f01c879d
fetched_at: '2026-06-28T21:35:17.644090+00:00'
page_id: '113803693'
product: fluig
source: tdn-fluig
title: Construção de Widgets e Layouts
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=113803693
version: 67
---

# Índice

true.\*ndicenone

# Objetivo

O objetivo deste guia é possibilitar ao desenvolvedor criar componentes WCM via Eclipse ou Fluig Studio.

# Vídeos How To

Assista!

Confira os vídeos How To sobre .

Compatibilidade no modo escuro

Este recurso ainda não é compatível com o modo escuro lançado na atualização [Voyager 2.0](https://tdn.totvs.com/x/6HxjN). Para mais detalhes, consulte a documentação em: add link

# Construção de componentes WCM no Eclipse

Para iniciar o desenvolvimento de um componente WCM no Eclipse ou , é necessário acessar a perspectiva Fluig e criar um novo projeto.

iniciar\_devAbrir perspectiva

* Acionar o menu ***Window*** na barra de menu.

* Selecionar ***Perspective*** → ***Open Perspective*** → ***Other*...**.

* Selecionar **Fluig** e acionar **OK**.

**Perspectiva Fluig no Eclipse**

Criar projeto

* Clicar com o botão direito do *mouse* no espaço *Package Explorer*.

* Selecionar ***New*** → **Projeto Fluig**.

* Informar o nome do projeto no campo *Project name*.

* Acionar ***Finish***.

**Criação de um novo projeto Fluig**

### Criação do Widget

Com o ambiente de desenvolvimento preparado, pode ser iniciada a criação do *widget* no projeto conforme os passos a seguir.

criacao\_widgetPasso 1

* Clicar com o botão direito do *mouse* sobre o projeto Fluig criado.

* Selecionar ***New*** → ***Widget***.

Passo 2

* Informar o código do *widget* no campo **Código**. Este campo é uma **chave única** e obrigatório.

O campo Código aceita apenas letras, números e sublinhado.

* Informar o nome do *widget* no campo **Nome**.

* Informar uma breve descrição do *widget* no campo **Descrição**.

* Escolher um dos *templates* disponíveis para o desenvolvimento do *widget* no campo **Template** ou manter o padrão "Nenhum" para não utilizar um modelo de desenvolvimento.

* Acionar ***Next*** para avançar.

Passo 3

* Informar o código, nome e URL para identificação do desenvolvedor do componente (Opcional).

* Informar a categoria do *widget* (Opcional).

As categorias funcionam como filtros para localizar *widgets* mais rapidamente e são listadas no painel esquerdo da janela de seleção de *widgets* exibido ao incluir novos *widgets* em um *slot*.

* Apenas um renderizador é disponibilizado atualmente (FreeMarker).

* Acionar ***Finish*** para concluir a criação do *widget*.

Passo 4

* Concluída a etapa de criação do *widget*, uma estrutura de diretórios será gerada abaixo da pasta "wcm/widget" do projeto.

A descrição dos arquivos gerados está disponível no item Estrutura dos diretórios de *widgets*.

### Estrutura dos diretórios de *widgets* tabelaestruturawidget

| Arquivo/Pasta | Descrição |
| --- | --- |
| [código\_do\_widget] | Nome/Identificador do *widget*. |
| src/main/java | Localização das classes Java, caso exista alguma regra de negócio específica do *widget*. |
| src/main/resources/application.info | Arquivo de configuração do *widget* onde são gravados o código, título e desenvolvedor do *widget*, entre outros dados.  Este arquivo será detalhado nas próximas páginas deste documento. |
| src/main/resources/view.ftl | Arquivo de *template* do FreeMarker que será interpretado durante a renderização do *widget*. |
| src/main/resources/edit.ftl | Arquivo que será interpretado durante a renderização do *widget* em modo de edição. Usado para configurar opções específicas para renderização do *widget*, como por exemplo, filtros de data, cotação do dólar, etc.  Este arquivo é opcional. Caso não exista, será considerado que o *widget* não possui modo de edição, somente visualização. |
| src/main/resources/[código\_do\_widget].properties | Arquivo de *strings* traduzíveis utilizadas pelo *widget*. Deve possuir derivações de acordo com o idioma suportado pelo *widget*.  O padrão será sempre o código do *widget* seguido do sufixo referente à sua linguagem. Por exemplo: um arquivo de tradução para o idioma inglês ficaria “código-do-widget\_EN\_US.properties”. |
| src/main/webapp/icon.png | Ícone utilizado para representar o *widget* no menu lateral da aplicação, ou em qualquer tela que necessite de uma representação visual do componente. Deve possuir a dimensão 55 x 30 *pixels*. |
| src/main/webapp/WEB-INF/web.xml | Descritor padrão de uma aplicação Java para *web*. |
| src/main/webapp/WEB-INF/jboss-web.xml | Descritor específico para o servidor de aplicação. Deve conter obrigatoriamente a propriedade “context-root”. O context-root representa o contexto *web* do *widget* e o recomendado é que o valor seja o próprio código do *widget*. |
| src/main/webapp/resources/css/[código\_do\_widget].css | Folha de estilo do *widget*. |
| src/main/webapp/resources/js/[código\_do\_widget].js | Arquivo JavaScript do *widget* (caso seja necessário). |
| src/main/webapp/resources/images | Pasta específica de imagens do *widget*, caso necessário. |
| src/test/java | Pasta específica para a construção de testes unitários. |

Atenção!

**01.** Não devem ser criadas novas pastas no diretório *"*src/main/resources*"*. O recomendado é que sejam utilizadas as pastas já existentes no projeto.

**02.** Ao criar um *widget*, os itens abaixo devem possuir o mesmo nome. Este nome deve ser **único**, ou seja, não pode ser utilizado em nenhum outro *widget*, pois a duplicidade pode causar problemas durante o *deploy* dos componentes:

* Nome do *widget*.
* Propriedade "context-root" do arquivo jboss-web.xml.
* Propriedade "application.code" do arquivo application.info.

### Exemplo de código JavaScript

javascript').addClass('message').append(this.message);
$div.append($message);
}
});
 ]]>

### Exemplo de código HTML com FreeMarker (view.ftl)

# ${i18n.getTranslation('hello.example.hello')}

${i18n.getTranslation('hello.button.showMessage')}

]]>

### Criação de Layout

Com o ambiente de desenvolvimento preparado, pode ser iniciada a criação do *layout* no projeto conforme os passos a seguir.

create\_layoutPasso 1

* Clicar com o botão direito do *mouse* sobre o projeto Fluig criado.

* Selecionar ***New*** → ***Layout***.

Passo 2

* Informar o código do *layout* no campo **Código**. Este campo é uma chave única e obrigatório.

O campo Código aceita apenas letras, números e sublinhado.

* Informar o nome do *layout* no campo **Nome**.

* Informar uma breve descrição do *layout* no campo **Descrição**.

* Escolher um dos *templates* disponíveis para o desenvolvimento do *layout* no campo **Template** ou manter o padrão "Nenhum" para não utilizar um modelo de desenvolvimento.

* Acionar ***Next*** para avançar.

Passo 3

* Informar o código, nome e URL para identificação do desenvolvedor do componente (Opcional).

* Informar a categoria do *layout* (Opcional).

* Apenas um renderizador é disponibilizado atualmente (FreeMarker).

* Acionar ***Finish*** para concluir a criação do *layout*.

Passo 4

* Concluída a etapa de criação do *layout*, uma estrutura de diretórios será gerada abaixo da pasta "wcm/layout" do projeto.

Observação

A estrutura de pastas e arquivos de um componente *Layout* é praticamente a mesma de um componente *Widget*. A principal diferença encontra-se no caminho src/main/resources/ onde os arquivos view.ftl e edit.ftl são substituídos pelo arquivo layout.ftl.

### Exemplo de código FreeMarker (layout.ftl)

html/xml

[<#if '${imageLogo}'=='true'>
![](${serverContextURL}/resources/images/${pageRender.user.tenantId}/logo_image.png)
<#else>
![](${serverContextURL}/resources/images/logo.png)](home "${i18n.getTranslation('layout.label.pagetitle')}")

<#list (pageRender.getInstancesIds("SlotLogin"))! as id>
${pageRender.renderInstanceNoDecorator(id)}

<#if pageRender.isEditMode()=true>


<#else>

${i18n.getTranslation('wcm.layoutdefault.title')}

## ${pageTitle}

<#list (pageRender.getInstancesIds("SlotC"))! as id>
${pageRender.renderInstanceNoDecorator(id)}

<#list (pageRender.getInstancesIds("SlotB"))! as id>
${pageRender.renderInstanceNoDecorator(id)}

<#list (pageRender.getInstancesIds("SlotA"))! as id>
${pageRender.renderInstance(id)}

]]>Dica

Para compreender melhor os elementos de um código de layout, leia a [sessão de layouts](http://tdn.totvs.com/display/fluig/Layouts).

### Exemplo de código JavaScript

javascript').addClass('message').append(this.message);
$div.append($message);
}
});]]>

### Exemplo de códigos para inclusão de componentes nos layouts (view.ftl)

Os *layouts* customizados do Fluig Plataforma permitem que o desenvolvedor reutilize alguns componentes padrão da plataforma, como o cabeçalho contendo as informações do usuário, campo de busca e notificações globais, rodapé, menu e outros componentes.

Quando o desenvolvedor inicia a criação de um *layout* pelo Eclipse ou Fluig Studio, é possível utilizar alguns exemplos de *layouts* existentes. Em alguns destes *layouts* pré definidos é necessário verificar quais componentes estão presentes e quais foram inseridos, pois algumas vezes é necessário configurar o *slots* no arquivo "src/main/resources/application.info".

Abaixo estão disponíveis alguns exemplos de trechos de código para montagem de componentes no *layout*. Cada um destes códigos possui particularidades e não podem apenas ser incluídos no arquivo view.ftl, pois precisam estar dentro de tags <div> para funcionar de forma correta.

**Inclusão do componente de busca**

* O trecho abaixo deve ser inserido dentro da *tag* <div class="header-grouper-right">, que por sua vez deverá estar dentro da *tag* <div id="wcm\_header" class="wcm-header-background wcm-header">.

* No arquivo src/main/resources/application.info o desenvolvedor deverá incluir: slot.SlotInstantSearch=suggestsearch.

xmlComponente de Busca
<#list (pageRender.getInstancesIds("SlotInstantSearch"))! as id>
${pageRender.renderInstanceNoDecorator(id)}
