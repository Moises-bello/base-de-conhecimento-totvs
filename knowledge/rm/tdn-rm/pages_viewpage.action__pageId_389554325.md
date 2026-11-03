---
content_hash: 9e1d56f9df27e396e39dd7bfdbbb1ad59b068eb2486e69ecf114c077494580dd
fetched_at: '2026-06-29T00:09:08.553989+00:00'
page_id: '389554325'
product: rm
source: tdn-rm
title: Criação do aplicativo do Facebook
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389554325
version: 53
---

# Índice:

---

.\*ndice:

# Objetivo

---

       A seguir será apresentado o passo-a-passo de como criar um aplicativo do Facebook para ser usado no RM, como provedor de login.

       Para mais informações sobre as opções de login, acesse o .

# Criando um novo aplicativo do Facebook

---

### **1º-** Acesse o website aos desenvolvedores do Facebook ([http://developers.facebook.com](http://developers.facebook.com/)).

Atenção

Para criar um novo aplicativo do Facebook, é necessário que a instituição tenha um cadastro válido na plataforma do Facebook.

### **2**º**-** Acessar o menu **Meus Aplicativos** → **Criar aplicativo**

### **3º-** Selecionar o tipo do Aplicativo

Selecione Nenhum e Avançar

### **4º-** Criar um novo aplicativo Facebook

Informe o **Nome de exibição** (Nome do aplicativo) e o **E-mail de contato** do responsável pelo aplicativo.

No exemplo a seguir usaremos o nome: “TOTVS Login”:

### **5º-**  Selecionar o Produto → Login do Facebook

Neste exemplo escolheremos **Login do Facebook**e em seguida clique em **Configurar:**

### **6º-**  Acessar o menu lateral **Login do Facebook → Configurações**

Nesta etapa, você deverá informar a as **URI’s de redirecionamento do OAuth válidos**. Salve as alterações.

Por exemplo:

* + Para o portal do aluno de teste, nós poderíamos informar um endereço baseado em “localhost”, pois o Portal do Aluno de exemplo encontra-se na mesma máquina em que é feito a configuração (definimos o endereço: <http://localhost:8080/web/app/edu/PortalEducacional/>).
  + Para o portal que está configurado com SSL informe o endereço correto de redirecionamento. (Neste exemplo usamos: <https://testeframe.com.br/RM12122/Login.aspx> ou <http://localhost/Corpore.Net/Login.aspx>)
  + Antes, para configurar o aplicativo do Facebook para login na MDI, neste campo era necessário informar o endereço: <https://www.facebook.com/connect/login_success.html>. Esta funcionalidade não é mais necessária, e inclusive, não é mais permitida pelo facebook nas versões atuais do OAuth.Ainda nessa tela, marque a opção **Login do OAuth no navegador incorporado** e salve as alterações:

### **7º-**  Clique no menu lateral na opção **Configurações → Básico**.

Nesta página é obrigatório preencher a URL da Política de Privacidade (Ex.: [https://pt-br.facebook.com/msqrd/privacy](https://www.google.com/url?q=https://pt-br.facebook.com/msqrd/privacy&sa=D&source=hangouts&ust=1561056914720000&usg=AFQjCNGdNBrvPHJcM2wWpaWG0R6zvP75-Q)), a categoria do aplicativo e salvar as alterações.

Poderá ser informado **Domínio do aplicativo,** opcional;  Pode ocorrer de ao preencher este campo e salvar as alterações ele permaneça vazio, isto não vai gerar problema, pode prosseguir.

Também é possível definir configurações adicionais, como: Logo da empresa, URL da política de privacidade, URL de Termos de Serviço e etc (que são opcionais para o funcionamento do serviço desejado, mas recomendável que a instituição faça seu preenchimento.)

### **8º-** ID e Chave Secreta do Aplicativo

Após definir todas as configurações necessárias para funcionamento do aplicativo de Login via Facebook, precisaremos de alguns dados para fazermos a configuração do aplicativo com o sistema RM.

Para isso, permaneça na tela de **Configurações → Básico**, onde estão as informações necessárias para fazer essa integração.

Anote os dados destacados conforme a imagem abaixo, clique em Mostrar.

Importante

Não se deve marcar a configuração "Exigir chave secreta do Aplicativo".

---

/\* @license ! jQuery-mutate - v0.0.2 -
\* Licensed under the MIT license
\* http://www.opensource.org/licenses/mit-license.php
\* Date: 2015-04-19 \*/
!function(t){mutate\_event\_stack=[{name:"width",handler:function(a){var e=t(a);return e.data("mutate-width")||e.data("mutate-width",e.width()),e.data("mutate-width")&&e.width()!=e.data("mutate-width")?(e.data("mutate-width",e.width()),!0):!1}},{name:"height",handler:function(a){var e=t(a);return e.data("mutate-height")||e.data("mutate-height",e.height()),e.data("mutate-height")&&e.height()!=e.data("mutate-height")?(e.data("mutate-height",e.height()),!0):void 0}},{name:"top",handler:function(a){var e=t(a);return e.data("mutate-top")||e.data("mutate-top",e.css("top")),e.data("mutate-top")&&e.css("top")!=e.data("mutate-top")?(e.data("mutate-top",e.css("top")),!0):void 0}},{name:"bottom",handler:function(a){var e=t(a);return e.data("mutate-bottom")||e.data("mutate-bottom",e.css("bottom")),e.data("mutate-bottom")&&e.css("bottom")!=e.data("mutate-bottom")?(e.data("mutate-bottom",e.css("bottom")),!0):void 0}},{name:"right",handler:function(a){var e=t(a);return e.data("mutate-right")||e.data("mutate-right",e.css("right")),e.data("mutate-right")&&e.css("right")!=e.data("mutate-right")?(e.data("mutate-right",e.css("right")),!0):void 0}},{name:"left",handler:function(a){var e=t(a);return e.data("mutate-left")||e.data("mutate-left",e.css("left")),e.data("mutate-left")&&e.css("left")!=e.data("mutate-left")?(e.data("mutate-left",e.css("left")),!0):void 0}},{name:"hide",handler:function(a){var e=t(a),r=e.is(":hidden"),d=void 0==e.data("prev-hidden")?r:e.data("prev-hidden");return e.data("prev-hidden",r),r&&r!=d?!0:void 0}},{name:"show",handler:function(a){var e=t(a),r=e.is(":visible"),d=void 0==e.data("prev-visible")?r:e.data("prev-visible");return e.data("prev-visible",r),r&&r!=d?!0:void 0}},{name:"scrollHeight",handler:function(a){var e=t(a);return e.data("prev-scrollHeight")||e.data("prev-scrollHeight",e[0].scrollHeight),e.data("prev-scrollHeight")&&e[0].scrollHeight!=e.data("prev-scrollHeight")?(e.data("prev-scrollHeight",e[0].scrollHeight),!0):void 0}},{name:"scrollWidth",handler:function(a){var e=t(a);return e.data("prev-scrollWidth")||e.data("prev-scrollWidth",e[0].scrollWidth),e.data("prev-scrollWidth")&&e[0].scrollWidth!=e.data("prev-scrollWidth")?(e.data("prev-scrollWidth",e[0].scrollWidth),!0):void 0}},{name:"scrollTop",handler:function(a){var e=t(a);return e.data("prev-scrollTop")||e.data("prev-scrollTop",e[0].scrollTop()),e.data("prev-scrollTop")&&e[0].scrollTop()!=e.data("prev-scrollTop")?(e.data("prev-scrollTop",e[0].scrollTop()),!0):void 0}},{name:"scrollLeft",handler:function(a){var e=t(a);return e.data("prev-scrollLeft")||e.data("prev-scrollLeft",e[0].scrollLeft()),e.data("prev-scrollLeft")&&e[0].scrollLeft()!=e.data("prev-scrollLeft")?(e.data("prev-scrollLeft",e[0].scrollLeft()),!0):void 0}}]}(jQuery);
]]>]]>
.expand-container{
margin-top:5px !important;
font-weight: normal !important;
}
.expand-control{
margin-bottom: 5px !important;
}
pre{
white-space: inherit !important;
}
table tr:nth-child(odd), table tr:nth-child(odd) > \*{
background: transparent !important;
border: 0 !important;
}
.pdl .codeContent .gutter{
border-right: 1px solid #ccc !important;
}
.wiki-content .innerCell {
overflow-y: hidden;
}
.HiddenDiv .confluence-information-macro {
width: calc(100% - 25px);
background: #fff !important;
border: 0 !important;
-moz-border-radius: 0px !important;
-webkit-border-radius: 0px !important;
border-radius: 0px !important;
color: #333;
margin: 10px 0 1em 0;
min-height: 20px;
padding: 10px;
position: relative;
}
.HiddenDiv .confluence-information-macro .confluence-information-macro pre{
display: none;
}
.HiddenDiv .wiki-content a:link, .HiddenDiv .wiki-content a, .HiddenDiv .tab-nav-link, .HiddenDiv .current{
color: #000 !important;
}
.wiki-content a:link {
color: #000 !important;
}
.lastDiv + pre{
font-family: inherit;
}
.white-container{
-moz-box-shadow: 2px 2px 2px #aaa;
-webkit-box-shadow: 2px 2px 2px #aaa;
box-shadow: 2px 2px 2px #aaa;
}
.confluence-embedded-file-wrapper .confluence-embedded-image{
max-width: 100% !important;
max-height: 100%;
}
]]>

![](/download/attachments/389554325/palette-samples.png?version=1&modificationDate=1534773337960&api=v2)
Exemplos

![](/download/attachments/389554325/palette-samples.png?version=1&modificationDate=1534773337960&api=v2)
Exemplo 1

![](/download/attachments/389554325/facebook-app-symbol.png?version=1&modificationDate=1534774490307&api=v2)
Configuração do App do Facebook no RM![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

]]>]]>

 e veja mais sobre a configuração dos aplicativos no RM
