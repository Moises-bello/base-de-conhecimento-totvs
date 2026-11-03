---
content_hash: 691fae26acb2a32c082f486cb0b8edb74d0cf5246fcd8f145bcf24b516275ad1
fetched_at: '2026-06-29T00:05:59.427913+00:00'
page_id: '190516500'
product: rm
source: tdn-rm
title: Get
type: documentation
url: https://tdn.totvs.com/display/LRM/Get
version: 36
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso

Versão

 Disponível à partir da versão 12.1.6 da linha RM.

# Get

Retorna o registro do dataserver representado pelo identificador da URL {id}. O FrameHTML faz a manipulação dos dados considerando que o mesmo possui um campo id como chave. Isso causa limitações no RM visto que a maior parte das chaves primárias do RM são compostas. Para contornar esse problema foi necessário concatenar o valor dos campos da chave primária e um campo chamado id (Caso já exista um campo id na tabela, esse será renomeado no json para "RESTDS\_TEMP\_id").

O id é o resultado da concatenação da chave primária utilizando como separador a string "$\_$". Se for tomado como exemplo a tabela local de estoque e um registro cujos campos CodColigada, CodFilial e CodLoc possuem, respectivamente, os valores 1, 1 e 06, o identificador que será gerado no json de retorno será "1$\_$1$\_$06".

O analista não deve manipular o valor do campo id, uma vez que ele é para uso interno do FrameHTML e do RM Host.

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
]]>

## Exemplo de utilização

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
Restful
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
localhost:8051
»
![](/download/attachments/190516500/copy.png?version=1&modificationDate=1509567801070&api=v2)
1$\_$1$\_$06
»
![](/download/attachments/190516500/programming-code-signs.png?version=1&modificationDate=1509568429032&api=v2)
GET

![](/download/attachments/190516500/info.png?version=1&modificationDate=1509568958717&api=v2)
Informações Gerais

![](/download/attachments/190516500/programming-code-signs.png?version=1&modificationDate=1509568429032&api=v2)
Get **(Method)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**URL**: <http://localhost:8051/rmsrestdataserver/rest/EstLOCData/1$_$1$_$06>]]>

![](/download/attachments/190516500/json.png?version=1&modificationDate=1509569485552&api=v2)
Modelo JSON

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
Get **(Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Retorna o registro do dataserver representado pelo identificador da URL {id}.]]>falsejs1Responsetrue

![](/download/attachments/190516500/binary-code.png?version=1&modificationDate=1509570539048&api=v2)
Exemplos

![](/download/attachments/190516500/new-page-view.png?version=1&modificationDate=1509570210360&api=v2)
SOAP UI **(5.3.0)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

Criar um novo projeto **REST** no **SOAP UI**:

]]>
Após a criação do projeto, o método GET irá ser apresentado, como a imagem abaixo:

]]>
Não se esqueça que a **Autenticação** Basic deverá ser preenchida.

]]>
Ao realizar a requisição o resultado é apresentado como a imagem abaixo:

]]>

![](/download/attachments/190516500/new-page-view.png?version=1&modificationDate=1509570210360&api=v2)
POC **(1.0.0 - Owner)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

Foi criado uma aplicação à parte do **RM** que faz a requisição ao serviço de **Rest** através do método **GET**, e a resposta obtida foi a mesma que a apresentada pelo **SOAP UI**.

]]>]]>

```
O Download da POC pode ser realizado .
```

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
