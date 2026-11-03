---
content_hash: 60934bfc493276304fe0d386b2e2f3a738604001f65154ec6f8bac5c82428028
fetched_at: '2026-06-28T21:35:19.875322+00:00'
page_id: '224113691'
product: fluig
source: tdn-fluig
title: Desenvolvimento de widgets mobile
type: documentation
url: https://tdn.totvs.com/display/fluig/Desenvolvimento+de+widgets+mobile
version: 24
---

# Índice

true.\*ndicenone

# Widgets Mobile

No Fluig, agora é possível visualizar widgets por meio das páginas, a partir de aplicativos móveis. Porém existem algumas particularidades que precisam ser lembradas para que o usuário tenha uma boa experiência com este recurso.

Todas as interfaces devem ser desenvolvidas nativamente, com exceção da visualização dos widgets da página que será renderizada pelo *webview* nativo da plataforma.

Qualquer tipo de autenticação requerido pela widget é de inteira responsabilidade do servidor do Fluig (SSO, por exemplo), o Mobile é apenas responsável por mostrar o HTML retornado pelo servidor no *webview*.

A visualização de páginas e widgets *offline* não é suportada no aplicativo Fluig Mobile.

### Recomendações para o desenvolvimento de widgets:

1. **HTML Responsivo:** Hoje no mercado existem variados tamanhos de telas e resoluções, por isso qualquer html desenvolvido para Mobile deve ser responsivo, ou seja, deve se ajustar a qualquer tamanho de tela.
2. **Estética:** A aparência visual e design da widget devem ser atraentes para os usuários, conseguimos isso através de CSS, para isso recomendamos a utilização do [Fluig style guide](http://style.fluig.com).
3. **Usabilidade:** A widget deve ser fácil de usar, contendo apenas o conteúdo necessário para usuário.
4. **Área de toque:** Os elementos do html devem estar bem posicionados de forma que facilite a área de toque, pois hoje existem dispositivos que as telas são muito pequenas.
5. **Posicionamento das ações:**As ações mais importantes devem estar posicionadas onde o usuário consegue alcançar facilmente, conforme a figura:
6. **Converter widgets já existentes para Mobile :**Para agilizar o desenvolvimento focado em mobile e web é necessário utilizar frameworks que tratam a responsividade, recomendamos a utilização do [Fluig Style Guide](https://style.fluig.com/).
7. **Elementos Suportados:** Widgets Mobile suportam os tipos:  
   1. text
   2. textArea
   3. radio
   4. select
   5. combobox
   6. checkbox.
   7. email (3)
   8. tel (3)
   9. range (3)
   10. date (3)
   11. time (1)(3)
   12. week (2)(3)
   13. number
   14. hidden
   15. password

(1) Existe um bug no Android Lollipop (5.0) que inviabiliza o uso do tipo *time*. Para mais informações, [clique aqui](https://code.google.com/p/chromium/issues/detail?id=434695).  
(2) O campo *week* não é suportado pelo iOS.

Não está homologada a implementação de evento que utilizem Swipe.

# Desenvolvendo widgets com suporte a exibição no Fluig Mobile

Cada uma das plataformas utiliza um browser diferente para a renderização de HTML. Esta informação deve ser considerada durante o desenvolvimento para evitar problemas de compatibilidade com os arquivos JavaScript/CSS. A tabela abaixo apresenta a versão mínima dos browsers de cada plataforma que deve ser considerada durante o desenvolvimento:

| Versão mínima da plataforma | Versão mínima do browser |
| --- | --- |
| Android 4.0 (Ice Cream Sandwich) | Webkit 534.30 |
| iOS 7 | Mobile Safari 9537.53 |

Para o desenvolvimento de *widgets* com suporte a dispositivos mobile deve ser adicionado a propriedade **application.mobileapp** no arquivo *[application.info](http://application.info) com o valor **true**.*

Esta propriedade será processada e persistida na base de dados durante o processo de *deploy*do *widget*.

xmlapplication.infotrue

A variável booleana **mobileAppMode** no template do FreeMarker determina se a widget está sendo renderizada através de uma requisição do aplicativo mobile. O Fluig irá verificar o *header* User-Agent da requisição e caso seja oriundo do aplicativo mobile o valor da variável **mobileAppMode** será `true`. Através desta variável é possível modificar o comportamento da widget quando renderizada pelo aplicativo mobile. O valor da variável **mobileAppMode** também está disponível via JavaScript através do método **WCMAPI.isMobileAppMode()**.

js

# API Pública

Está disponível o [serviço na API Pública para realizar a consulta de páginas do Fluig](https://api.fluig.com/resource_PageRest.html#path__2.0_pages_findPages.html). Esta consulta retornará somente as páginas que o usuário tenha permissão de visualização. O retorno do serviço será paginado com uma lista de PageVOs contendo as informações das páginas, entre elas a URL de acesso, URL do ícone, páginas filhas (quando houverem) e se está disponível para o aplicativo mobile. Será possível informar os seguintes filtros:

* **parentPageCode**: Código da página pai. Quando informado, retorna somente as páginas filhas da página informada.

* **isMobile**: Caso informado `true` retorna somente as páginas disponíveis para o aplicativo mobile.

* **pageIndex:**Caso informado, será o *index* da página a ser exibida

* **pageSize:**Caso informado, definirá a quantidade de registros por página.

* **searchLevel:**Caso informado, busca hierarquicamente as páginas filhas .

* **internalPages:**Caso informado true, a consulta de páginas resultará somente em paginas internas da plataforma.

* **filter**: String para filtrar o dados em caso de busca.

## Widgets com exibição de *iframe* em *webviews* do iOS

O aplicativo do Fluig, em alguns casos, utiliza *webviews* para visualização de páginas. Os *webviews* utilizam como base o navegador padrão do dispositivo, como por exemplo, o Safari quando o dispositivo em questão utiliza o sistema iOS (iPads e iPhones).

Quando o navegador Safari de um dispositivo com sistema iOS encontra um *iframe* dentro da página, ele ajusta a largura do iframe tomando como base a largura do conteúdo exibido dentro do *iframe*, e ignora qualquer parâmetro de largura definido pelo desenvolvedor. Esse comportamento só acontece no navegador Safari (e, portanto, em *webviews* que utilizam o Safari como base) de dispositivos com o sistema iOS.

Para contornar esse comportamento, é necessário desenvolver uma técnica de CSS que ajustará o *iframe* com largura de 100% e altura de 100%, sendo essa altura necessária para compensar a ausência de *scroll* no *iframe*, um parâmetro necessário para o funcionamento da técnica de CSS.

xmlCSS para iframes no Safari do iOS ]]>
