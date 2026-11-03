---
content_hash: a198c1248131d7f7b061aa4c36e3fb1835347bcad650a9e01a80213cac8308ba
fetched_at: '2026-06-29T00:09:02.912414+00:00'
page_id: '381028669'
product: rm
source: tdn-rm
title: License/Get
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381028669
version: 9
---

# Índice:

---

* Objetivo:
* Configuração:

# Objetivo:

---

Este documento tem como finalidade, demonstrar o utilização da **API Rest HealthCheck** evidenciando os serviços:

* /api/v1/healthcheck/License/Get

# Configuração:

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

![](/download/attachments/149881483/settings.png?version=1&modificationDate=1509720640465&api=v2)
Configuração

![](/download/attachments/190516500/info.png?version=1&modificationDate=1509568958717&api=v2)
Informações Gerais

![](/download/attachments/190516500/programming-code-signs.png?version=1&modificationDate=1509568429032&api=v2)
Serviço **/License/Get**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Objetivo:** Testar o consumo de uma licença de teste  
**Detalhamento:** Para consumir o serviço **/License/Get** utilize a seguinte rota: **/api/v1/healthcheck/license/get**.  
**Exemplo de Utilização:**]]>]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Retorno

![](/download/attachments/190516500/programming-code-signs.png?version=1&modificationDate=1509568429032&api=v2)
Retorno![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Retorno do serviço **/License/Get**.  
**Tipo:** Cadeia de Caracteres (String)

]]>

**Estrutura de retorno [FI002 - Sucesso]:**

falsejs1Retorno (Sucesso)true

**Estrutura de retorno [FW003 - Alerta]:**

falsejs1Retorno (Sucesso)true

**Estrutura de retorno [FE006 - Erro]:**

falsejs1Retorno (Erro)true

**Estrutura de retorno [FE008 - Erro]:**

falsejs1Retorno (Erro)true

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Atributos de Retorno

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Status **(Sucesso e Alertas)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Situação do consumo da licença de teste.  
**Tipo:** String  
**Possíveis Valores:**  
• Licença Consumida  
• Licença Não Consumida  
**Informações relevantes:** O status se refere a situação do consumo da licença de teste. Caso o consumo da licença de teste tenha sido realizada com sucesso o status de Consumida será apresentado, caso contrário o status de Não Consumida será apresentado.

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
ReturnCode **(Sucesso e Alertas)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Código Enviado pelo License Server  
**Tipo:** int  
**Possíveis Valores:**  
• 2014 (Sucesso)  
• -1505 (Alerta - Numero de licenças excedidas)  
• -1507 (Alerta - Licenças em uso)  
• -10001 (Alerta - LSC\_Error - O atributo () não foi enviado)  
Entre muitos outros valores...  
**Informações relevantes:** O ReturnCode se refere ao código retornado pelo License Server ao tentar consumir a licença de teste. Os códigos apresentados indicam a situação do consumo da licença de teste, se ela foi consumida ou não, se algum erro de conexão com o License Server aconteceu e etc....

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Message - Code **(Sucesso, Alertas e Erros)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Código da Mensagem  
**Tipo:** String  
**Possíveis Valores:**  
• FI00X (Informação)  
• FW00X (Alerta)  
• FE00X (Erro)  
**Informações relevantes:** O status se refere ao código da mensagem retornado pela api. Os códigos apresentados podem ser de informação (no caso de sucesso), de alerta (no caso de algum erro de negócio acontecer) e de erro (no caso de alguma exceção não tratada.

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Message - Message **(Sucesso, Alertas e Erros)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Descrição do Código  
**Tipo:** String  
**Possíveis Valores:**  
• Sucesso  
• Alerta  
• Erro  
**Informações relevantes:** O atributo message, nada mais é do que a descrição do código apresentado. O código FI00X indica sucesso ao consumir a api e sucesso ao aplicar corretamente a regra de negócio, o código FW00X indica sucesso ao consumir a api, porém falha na aplicação da regra de negócio e o código FE00X indica falha no consumo da api.

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Message - DetailedMessage **(Sucesso, Alertas e Erros)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Mensagem detalhada  
**Tipo:** String  
**Possíveis Valores:**  
• No caso de sucesso: A licença de teste foi consumida com sucesso!  
• No caso do erro FE008: Falha na tentativa de consumir a licença de teste!  
• No caso dos demais alertas e erros: Variados valores.  
**Informações relevantes:** O atributo detailedMessage trás uma descrição mais amigável do resultado do consumo da api. A mensagem de sucesso é unica e padronizada, enquanto que as mensagens de alerta e de erro podem ser variadas, devido as variadas possibilidades de retorno.

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Message - HelpUrl **(Erros)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Url de Ajuda  
**Tipo:** String  
**Possíveis Valores:**  
• Uma Url qualquer  
**Informações relevantes:** O atributo helpUrl é uma página da internet que explique melhor uma funcionalidade, ou um erro apresentado, afim de ajudar o usuário a entender melhor uma funcionalidade para o correto uso da mesma, ajudá-lo a reportar à Totvs algum erro evidenciado pela api.

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Message - Details **(Sucesso, Alertas e Erros)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Detalhes sobre a mensagem apresentada.  
**Tipo:** Cadeia de Caracteres (String)  
**Possíveis Valores:**  
• Um conjunto qualquer de mensagens.  
**Informações relevantes:** O atributo Details é uma lista de mensagens que corroboram com a mensagem detalhada. Essas mensagens, por exemplo, podem ser o trecho de código onde o erro aconteceu.

]]>
Show = function(divName, imgName){
window["currentElement"] = divName;
if(typeof divName === "string"){
if(document.getElementById(divName).offsetHeight < 2){
$("#" + divName).animate({height: $("#" + divName).get(0).scrollHeight + 7});
$("#" + divName).css("visibility", "visible")
$("#" + imgName).attr('src', '/download/attachments/309398329/remove.png?version=1&modificationDate=1509386912062&api=v2');
$(".HiddenDiv .tab-nav-link").on("click", function(){
window["currentElement"] = $(this).parents().find(".HiddenDiv").attr("id");
});
$(".HiddenDiv .confluence-information-macro").mutate('height',function (element,info){
this.selector.each(function(index, element){
if($(this).parent().attr("id") == window["currentElement"])
$(this).parent().height($(this).outerHeight() + 61);
});
});
}
else{
$("#" + divName).animate({height: "0px"});
$("#" + divName).css("visibility", "hidden")
$("#" + imgName).attr('src', '/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2');
}
}
}
]]>
