---
content_hash: 57e9e1e2eec5448d47b1f215cf37bcdcc9b08fb9aead406a1354329cb02bac2e
fetched_at: '2026-06-28T21:35:18.277404+00:00'
page_id: '155584509'
product: fluig
source: tdn-fluig
title: Layouts
type: documentation
url: https://tdn.totvs.com/display/fluig/Layouts
version: 65
---

## Índice

4true.\*ndicenone

# Sobre Layouts

O layout define a composição de uma página e é composto por múltiplos slots. A quantidade, posição e dimensão desses slots é o que define o corpo de um layout. Dessa forma, o layout é a estrutura de uma página, definindo a distribuição dos widgets que a compõe por meio dos slots.

# Slot

Slots são contêineres definidos que são aptos a comportarem widgets. A quantidade, posição e dimensão desses slots é o que define o corpo de um layout. Sendo assim, o layout é o esqueleto de uma página (sua estrutura), definindo a distribuição dos widgets que a compõem através dos slots.

# Estrutura de Arquivos

Layouts possuem a estrutura de arquivos semelhante à de um widget comum, e também são empacotados em formato “war”. A estrutura de pastas-fonte de um layout é a que segue:

| ``` <codigo-do-layout>  +-- src    +-- main      +-- java (não utilizado, padrão de widgets)      +-- resources        +-- application.info        +-- layout.ftl        +-- <codigo-do-layout>.properties        +-- <codigo-do-layout>_en_US.properties        +-- <codigo-do-layout>_es.properties        +-- <codigo-do-layout>_pt_BR.properties      +-- webapp        +-- META-INF        +-- resources          +-- images            +-- icon.png          +-- css          +-- js        +-- WEB-INF          +-- web.xml          +-- jboss-web.xml    +-- test      +-- java ``` |
| --- |

**Onde:**

| Arquivo / Pasta | Descrição |
| --- | --- |
| **<código-do-layout>** | Nome/Identificador do layout |
| **src/main/resources/application.info** | Arquivo de configuração do layout onde é persistida, entre outras informações, o código do layout, título e desenvolvedor. Este arquivo será mais detalhado nas próximas páginas deste documento. |
| **src/main/resources/layout.ftl** | Arquivo do Freemarker que será interpretado durante a renderização do layout. Contém a configuração dos slots. |
| **src/main/resources/<código-do-layout>.properties** | Arquivo de strings traduzíveis utilizadas pelo layout. Deve possuir derivações de acordo com o idioma suportado pelo layout. |
| **src/main/webapp/WEB-INF/web.xml** | Descritor padrão de uma aplicação Java para web. |
| **src/main/webapp/WEB-INF/jboss-web.xml** | Descritor específico para o servidor de aplicação. Deve conter pelo menos a propriedade “context-root”. O context-root representa o contexto Web do layout e é recomendado que seja o próprio código do layout. |
| **src/main/webapp/resources/css** | Folhas de estilo do layout (caso seja necessário). |
| **src/main/webapp/resources/js** | Arquivos Javascript do layout (caso seja necessário). |
| **src/main/webapp/resources/images/icon.png** | Ícone que representa o layout, é exibido, por exemplo, durante a criação de páginas para que o usuário possa pré-visualizar a distribuição de slots do layout. |

Para o sistema, o que diferencia um layout de um widget comum é a definição da propriedade “application.type = layout” no arquivo descritor “**application.info**”. Este arquivo é um descritor detalhado dos widgets e também dos layouts. É através deste que a aplicação tem conhecimento das propriedades do layout, identificação do desenvolvedor, arquivos necessários para sua renderização, arquivos de linguagem e outras propriedades.

## Arquivo application.info

Abaixo o detalhamento de todas as propriedades do arquivo **application.info**:

| Propriedade | Descrição |
| --- | --- |
| **application.type = <layout>** | O valor layout define que o componente é do tipo layout, existem outras opções como widget e theme. |
| **application.code = <código-do-layout>** | Iidentificador do layout. |
| **application.title = <título-do-layout>** | Título do layout. |
| **application.description = <descrição-do layout>** | Descrição do layout. |
| **application.category = <SYSTEM>** | Categoria do layout. Propriedade utilizada para filtro em determinados funções do sistema, esta propriedade é para uso futuro, atualmente não é utilizada. |
| **application.renderer = <freemarker>** | Indica o tipo de renderizador exigido (atualmente somente o Freemarker é suportado). |
| **application.icon = <icon.png>** | Ícone para representação visual do layout. Caso não informado o sistema assumirá um ícone padrão para sua representação visual. |
| **developer.code = <developer-code>** | Código do desenvolvedor do layout. |
| **developer.name = <TOTVS S.A.>** | Nome do desenvolvedor. |
| **developer.url = <[http://www.totvs.com](http://www.totvs.com/)****>** | URL do desenvolvedor. |
| **layout.file=layout.ftl = <layout.ftl>** | Nome do arquivo a ser renderização. Se não informado, será assumido “layout.ftl”. |
| **locale.file.base.name = <prefixo>** | Nome base do arquivo de tradução que será seguido pelo locale (ex.: prefixo\_PT\_BR e prefixo\_EN\_US). Se não informado, será usado o código do layout. |
| **application.resource.css.1 = </resources/css/<codigo-do-layout>.css>** | Opcional. Nome do arquivo CSS a ser carregado durante a renderização. Podem ser informado vários arquivos, o número no final do nome da propriedade indica a ordem de carga. |
| **application.resource.js.2 = </resources/js/<código-do-javascript>.js>** | Opcional. Nome do arquivo JS a ser carregado durante a renderização. Podem ser informado vários arquivos, o número no final do nome da propriedade indica a ordem de carga. |
| **slot.SlotMenu = <menu>** | Opcional. Entretanto, quando o arquivo .ftl possuir slot de Menu (SlotMenu), é necessário informar qual widget de menu deve ser utilizada. *"menu"* deve ser informado nesse caso. Entenda melhor [aqui](http://tdn.totvs.com/display/fluig/Layouts#Layouts-SobreSlotsNãoEditáveis). |
| **slot.SlotLogin = <sociallogin>** | Opcional. Entretanto, quando o arquivo .ftl possuir slot de Login (SlotLogin), é necessário informar qual widget de login deve ser usada. Apesar de haver mais de um opção para menu, recomendamos a utilização do valor *"sociallogin"* nesse caso. Entenda melhor [aqui](http://tdn.totvs.com/display/fluig/Layouts#Layouts-SobreSlotsNãoEditáveis). |
| **application.resource.css.1=/portal/resources/css/wcm\_responsive\_layout.css** | Arquivo CSS com configurações globais para a padronização de escrita dos layouts. Sempre necessário incluir.  A propriedade estará disponível a partir da **release 1.8.1** do TOTVS Fluig Plataforma. |
| **application.resource.css.2=/resources/css/responsive\_layout.css** | Arquivo CSS padrão para o desenvolvimento da responsividade do layout.  A propriedade estará disponível a partir da **release 1.8.1** do TOTVS Fluig Plataforma. |
| **application.responsiveLayout=true** | Caso o valor seja true, ilustrará que o layout é responsivo no momento do cadastro de páginas.  A propriedade estará disponível a partir da **release 1.8.1** do TOTVS Fluig Plataforma. |
| **application.newBuilder=true** | Se true significa que a página será carregada no novo construtor. Se false significa que a página será carregada no antigo construtor. Entenda melhor **[aqui](https://tdn.totvs.com/x/fYP5DQ)**.  A propriedade estará disponível a partir da **release 1.8.1** do TOTVS Fluig Plataforma. |

## Variáveis Disponíveis no FTL

Os principal arquivo de um projeto de layout é o “**layout.ftl**”. É neste arquivo que será definido, via marcação HTML e Freemarker, a quantidade e disposição dos slots.

Para facilitar o desenvolvimento, alguns métodos da camada de negócio são ofertados pela infra-estrutura do WCM e podem ser acessados via Freemarker. As variáveis disponibilizadas são acessadas através da sintaxe **${nome-da-variável}**em qualquer local do FTL, a seguir uma lista das variáveis disponíveis:

| Variável | Descrição |
| --- | --- |
| serverBaseURL | URL do servidor (sem nenhum contexto). |
| i18n | Objeto com as strings internacionalizadas. |
| themeURI | Contexto do tema (por exemplo: /themedefault). |
| themeURL | URL completa do tema (serverBaseURL + themeURI). |
| pageId | ID da página. |
| layoutId | ID do layout. |
| layoutURI | Contexto do layout (por exemplo: /layoutdefault). |
| layoutURL | URL completa do layout (serverBaseURL + layoutURI). |
| serverContextURL | Contexto do sistema. |
| locale | Objeto com a localização selecionada para o usuário. |
| user | Login do usuário (ou vazio se não está logado). |
| tenantId | ID do Tenant do usuário logado (-1 se não está logado). |
| tenantCode | Código do Tenant do usuário logado (ou vazio se não está logado). |
| pageFriendlyURL | URI da página (formado pelo contexto + código da empresa + código da página). |
| wcmEnums | Variável de acesso aos enum’s da aplicação. |
| wcm | Objeto com os serviços disponibilizados pelo SDK do WCM. |
| pageRender | Objeto que também disponibiliza serviços do SDK. |
| fluigVersion | Versão do TOTVS Fluig Plataforma. |

O objeto “**pageRender**” disponibiliza os seguintes métodos do SDK:

| Método | Descrição |
| --- | --- |
| **PageVO getPage()** | Retorna um objeto do tipo VO com todas as informações da página corrente, como sua página pai (caso exista), páginas filhas, layout e tema, entre outras propriedades. |
| **List<PageVO> listPageBreadcrumb()** | Retorna uma lista de páginas ordenadas em modo de navegação estrutural, possibilitando a localização da página atual em meio estrutura de páginas do sistema. |
| **void renderInstance(long instanceId)** | Método que inicia a renderização de um widget utilizando o FTL “decoration.ftl”, ou seja, irá renderizar o widget e seu título no slot onde foi invocado o método. |
| **void renderInstanceNoDecorator(long instanceId)** | Método que inicia a renderização de um widget utilizando o FTL “nodecoration.ftl”, ou seja, irá renderizar o widget sem a barra de título, no slot onde foi invocado o método. |
| **boolean isUserLogged()** | Retorna se existe um usuário logado através do VO da página. |
| **UserVO getUser()** | Retorna objeto VO do usuário corrente contendo informações como nome, email e código do Tenant entre outras propriedades.  As informações de grupos e papéis do usuário não são apresentadas neste objeto e o uso deste tipo de informação para validações no desenvolvimento de widgets não é recomendado, pois afeta o desempenho do carregamento das páginas. |
| **List<Long> getInstancesIds(Slog slot)** | Retorna uma lista com ID de todas os widgets contidas no “slot” informado. |
| **List<Long> getInstancesByCode(String code)** | Retorna o ID de instância de todas os widgets com o código informado “code” contidas na página. |
| **boolean hasPermission(long instanceId, String permission)** | Verifica se o widget com o “instanceId” informado possui uma determinada permissão, conforme a “permission” desejada. |
| **boolean hasViewPermission(long instanceId)** | Verifica se o usuário logado possui permissão de visualização do widget. |
| **boolean hasEditPermission(long instanceId)** | Verifica se o usuário logado possui permissão de edição para a instancia (“instanceId”) em questão. |
| **String getHomePage()** | Retorna a URL de acesso a página inicial (home). |
| **boolean isUserLoggedInOAuthWithConsumerKey(String consumerKey)** | Identifica se um usuário logado possui um token válido para o chave de consumo (“consumerKey”) informada. |
| **List<WidgetVO> listAllowedWidgetsByUser()** | Retorna a lista de Widgets as quais o usuário possuí permissão de visualização. |
| **Long getTenantId()** | Retorna o ID do Tenant do usuário corrente. |
| **pageRender.isPreviewMode()** | Diz se a página está em modo preview ou não true|false. |
| **pageRender.isEditMode()** | Diz se a página está em modo edição ou não true|false. |

## Macros para o uso no FTL dos layouts:

Arquivo que disponibiliza as macros para o layout: "**<#import "/wcm.ftl" as wcm />**".

| Método | Descrição |
| --- | --- |
| **<@wcm.previewPageAlert />** | Alerta no topo da página informando que a página está em modo de pré-visualização. |
| **<@wcm.header />** | Widget de cabeçalho da página (independente do tema). |
| **<@wcm.menu />** | Widget de menu da página  (independente do tema). |
| **<@wcm.editHeader />** | Widget de cabeçalho da página no modo de edição. |
| **<@wcm.widgetsList />** | Widget que faz a listagem de widgets disponíveis para serem adicionadas em uma página. |
| **<@wcm.renderSlot id="SlotA" editableSlot="true" isResponsiveSlot="true" />** | Macro padrão para renderização de um slot. (se o parâmetro isResponsiveSlot for true, implementa o visual novo com as ações novas em uma widget). |
| **<@wcm.footer layoutuserlabel="wcm.layoutdefaultecmdashboard.user" />** | Widget padrão para o rodapé da página. |

# Fluxograma de Renderização

Toda página renderizada no WCM possui o mesmo fluxo para sua construção. O primeiro arquivo chamado no processo de renderização é o “**master.ftl**”, onde são informados os metadados da página. O arquivo **master** invoca o método “**pageRender.renderTheme()**”, responsável pela renderização do tema, que por sua vez irá chamar a renderização do layout, onde posteriormente serão renderizadas os widgets que compõem a tela, concluindo a construção da página.

O fluxograma a seguir exemplifica o processo de renderização de uma página:

# Criando um Layout

É possível criar um layout a partir do Fluig Studio. O tutorial com o passo-a-passo encontra-se [aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=113803693#ConstruçãodecomponentesWCMnoFluigStudio-CriaçãodeLayout)

* Uma vez finalizando o tutorial, o Studio preparará um ambiente semelhante a esse:

* Ou, no caso de ter-se optado por um layout vazio, aparecerá o seguinte conteúdo:

* Para criar um slot, nesse caso, pode-se usar o Snippet "Slot de um Layout" disponível nos exemplos de código do Studio.
* Entenda o impacto na forma como você cria o layout na sessão sobre [mudança no layout de uma página](http://tdn.totvs.com/pages/viewpage.action?pageId=185745580)

# Código do Layout

Apesar de a estrutura fornecida pelos templates do Studio não serem obrigatórios, é aconselhável o uso de alguns elementos essenciais quando do desenvolvimento de um layout a partir da estaca zero, como por exemplo:

samples11.8.1 e superioresxmlEclipse
<#-- Variaveis globais para os layouts -->
<#import "/layout-globals.ftl" as globals />
<#if pageRender.isPreviewMode() = true>
<@wcm.previewPageAlert />
<@wcm.deviceTogglePreview />

<#if pageRender.isEditMode() = false>
<@wcm.header authenticated=pageRender.isUserLogged()?c />
<@wcm.menu />

<#if pageRender.isEditMode()=true>
<@wcm.editHeader />
<@wcm.widgetsList />

<@wcm.renderSlot id="SlotC" editableSlot="true" decorator="false" isResponsiveSlot="true" />

<#if fluigThemeCode != "responsive\_theme">
<@wcm.footer layoutuserlabel="wcm.layoutdefault.user" />

]]>21.8.0 e inferioresxmlEclipse
<@wcm.header public="true"/>

<@wcm.menu />

<@wcm.footer layoutuserlabel="wcm.layoutdefault.user" />

]]>

# Código do Slot

O código de um slot é composto dos seguintes elementos:

xml
<@wcm.renderSlot id="Slot001" decorator="false" editableSlot="false" isResponsiveSlot="true" />

]]>

**Sobre o  primeiro elemento "div":**

xml ...

]]>
