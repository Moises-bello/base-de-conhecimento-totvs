---
content_hash: 937665b69785b53443a0a7205e0db98435be413ffe1368ddbbb93474074a8f28
fetched_at: '2026-06-29T00:08:44.767659+00:00'
page_id: '309398329'
product: rm
source: tdn-rm
title: TBC - Web Services Fórmula Visual (Workflow)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309398329
version: 314
---

# Indice:

---

.\*ndice:

# Introdução:

---

       O **Web Service Fórmula Visual** fornece serviços para **executar uma Fórmula Visual** de forma síncrona e assíncrona. O modelo de autenticação utilizado é o **Basic Authentication**.

# Como Funciona:

---

       Estão expostos no **wsFormulaVisual** alguns serviços, onde para consumi-los, é necessário enviar através de uma requisição um envelope **SOAP** passando os parâmetros de cada serviço. 

      O serviço é exposto pelo host conforme documentação abaixo:

Segue abaixo o detalhamento e exemplos de utilização dos serviços em envelope **SOAP**:

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

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
FVWebService
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
RM\_IRMSServer
»
![](/download/attachments/309398329/loop3.png?version=2&modificationDate=1509366835997&api=v2)
CheckServiceActivity

![](/download/attachments/309398329/xml-file.png?version=1&modificationDate=1509371596771&api=v2)
Modelo XML

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
CheckServiceActivity **(Requisição e Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Serviço que permite verificar o status da Atividade. ]]>false.Requestxml1Requesttrue




]]>ResponsexmlResponse










   0,TOTVS Educacional,306,Boletim,Boletim,06/10/2010 15:43:00,597e2978-351d-4629-a2fb-b57432cad210;,0,TOTVS Educacional,30,Contrato,Contrato,06/10/2010 15:43:00,71eff25f-0960-4ab7-bbc9-564044dde0fe;,0,TOTVS Gestão Financeira,312,Boleto Itaú.2.1,Cópia de Cópia de Boleto Itaú,08/04/2016 07:49:00,c9c51350-3cfa-410e-b818-224a013d0296;,0,TOTVS Inteligência de Negócios,316,filtrosNomeados,filtrosNomeados,11/04/2016 10:37:12,d19713e7-eda0-4bf1-8e92-140714240c16;,0,TOTVS Educacional,31,EDUREL002,Listagem de Alunos com foto,06/10/2010 15:43:00,b84b941c-54e5-43c1-996b-3e9eae05e902.......    ]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Parâmetros

Esse método não possui parâmetros

]]>

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
FVWebService
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
RM\_IRMSServer
»
![](/download/attachments/309398329/loop3.png?version=2&modificationDate=1509366835997&api=v2)
Implements

![](/download/attachments/309398329/xml-file.png?version=1&modificationDate=1509371596771&api=v2)
Modelo XML

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
Implements **(Requisição e Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Serviço que permite implementar uma propriedade tipada.]]>false.Requestxml1Requesttrue







]]>ResponsexmlResponse   0,TOTVS Educacional,306,Boletim,Boletim,06/10/2010 15:43:00,597e2978-351d-4629-a2fb-b57432cad210;,0,TOTVS Educacional,30,Contrato,Contrato,06/10/2010 15:43:00,71eff25f-0960-4ab7-bbc9-564044dde0fe;,0,TOTVS Gestão Financeira,312,Boleto Itaú.2.1,Cópia de Cópia de Boleto Itaú,08/04/2016 07:49:00,c9c51350-3cfa-410e-b818-224a013d0296;,0,TOTVS Inteligência de Negócios,316,filtrosNomeados,filtrosNomeados,11/04/2016 10:37:12,d19713e7-eda0-4bf1-8e92-140714240c16;,0,TOTVS Educacional,31,EDUREL002,Listagem de Alunos com foto,06/10/2010 15:43:00,b84b941c-54e5-43c1-996b-3e9eae05e902.......    ]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Parâmetros

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Type **(Opcional)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Tipo

]]>

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
FVWebService
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
RM\_IwsBase
»
![](/download/attachments/309398329/loop3.png?version=2&modificationDate=1509366835997&api=v2)
AutenticaAcesso

![](/download/attachments/309398329/xml-file.png?version=1&modificationDate=1509371596771&api=v2)
Modelo XML

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
AutenticaAcesso **(Requisição e Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Serviço que permite autenticar o acesso ao servidor, cujo resposta SOAP será enviada.]]>false.Requestxml1Requesttrue




]]>ResponsexmlResponse   0,TOTVS Educacional,306,Boletim,Boletim,06/10/2010 15:43:00,597e2978-351d-4629-a2fb-b57432cad210;,0,TOTVS Educacional,30,Contrato,Contrato,06/10/2010 15:43:00,71eff25f-0960-4ab7-bbc9-564044dde0fe;,0,TOTVS Gestão Financeira,312,Boleto Itaú.2.1,Cópia de Cópia de Boleto Itaú,08/04/2016 07:49:00,c9c51350-3cfa-410e-b818-224a013d0296;,0,TOTVS Inteligência de Negócios,316,filtrosNomeados,filtrosNomeados,11/04/2016 10:37:12,d19713e7-eda0-4bf1-8e92-140714240c16;,0,TOTVS Educacional,31,EDUREL002,Listagem de Alunos com foto,06/10/2010 15:43:00,b84b941c-54e5-43c1-996b-3e9eae05e902.......    ]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Parâmetros

Esse método não possui parâmetros

]]>

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
FVWebService
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
RM\_IwsBase
»
![](/download/attachments/309398329/loop3.png?version=2&modificationDate=1509366835997&api=v2)
CheckServiceActivity

![](/download/attachments/309398329/xml-file.png?version=1&modificationDate=1509371596771&api=v2)
Modelo XML

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
CheckServiceActivity **(Requisição e Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Serviço que permite verificar o status da Atividade.]]>false.Requestxml1Requesttrue




]]>ResponsexmlResponse   0,TOTVS Educacional,306,Boletim,Boletim,06/10/2010 15:43:00,597e2978-351d-4629-a2fb-b57432cad210;,0,TOTVS Educacional,30,Contrato,Contrato,06/10/2010 15:43:00,71eff25f-0960-4ab7-bbc9-564044dde0fe;,0,TOTVS Gestão Financeira,312,Boleto Itaú.2.1,Cópia de Cópia de Boleto Itaú,08/04/2016 07:49:00,c9c51350-3cfa-410e-b818-224a013d0296;,0,TOTVS Inteligência de Negócios,316,filtrosNomeados,filtrosNomeados,11/04/2016 10:37:12,d19713e7-eda0-4bf1-8e92-140714240c16;,0,TOTVS Educacional,31,EDUREL002,Listagem de Alunos com foto,06/10/2010 15:43:00,b84b941c-54e5-43c1-996b-3e9eae05e902.......    ]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Parâmetros

Esse método não possui parâmetros

]]>

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
FVWebService
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
RM\_IwsBase
»
![](/download/attachments/309398329/loop3.png?version=2&modificationDate=1509366835997&api=v2)
Implements

![](/download/attachments/309398329/xml-file.png?version=1&modificationDate=1509371596771&api=v2)
Modelo XML

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
Implements **(Requisição e Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Serviço que permite implementar uma propriedade tipada.]]>false.Requestxml1Requesttrue







]]>ResponsexmlResponse   0,TOTVS Educacional,306,Boletim,Boletim,06/10/2010 15:43:00,597e2978-351d-4629-a2fb-b57432cad210;,0,TOTVS Educacional,30,Contrato,Contrato,06/10/2010 15:43:00,71eff25f-0960-4ab7-bbc9-564044dde0fe;,0,TOTVS Gestão Financeira,312,Boleto Itaú.2.1,Cópia de Cópia de Boleto Itaú,08/04/2016 07:49:00,c9c51350-3cfa-410e-b818-224a013d0296;,0,TOTVS Inteligência de Negócios,316,filtrosNomeados,filtrosNomeados,11/04/2016 10:37:12,d19713e7-eda0-4bf1-8e92-140714240c16;,0,TOTVS Educacional,31,EDUREL002,Listagem de Alunos com foto,06/10/2010 15:43:00,b84b941c-54e5-43c1-996b-3e9eae05e902.......    ]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Parâmetros

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Type **(Opcional)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Tipo

]]>

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
FVWebService
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
RM\_IwsFormulaVisual
»
![](/download/attachments/309398329/loop3.png?version=2&modificationDate=1509366835997&api=v2)
CheckServiceActivity

![](/download/attachments/309398329/xml-file.png?version=1&modificationDate=1509371596771&api=v2)
Modelo XML

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
CheckServiceActivity **(Requisição e Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Serviço que permite verificar o status da Atividade.]]>false.Requestxml1Requesttrue




]]>ResponsexmlResponse   0,TOTVS Educacional,306,Boletim,Boletim,06/10/2010 15:43:00,597e2978-351d-4629-a2fb-b57432cad210;,0,TOTVS Educacional,30,Contrato,Contrato,06/10/2010 15:43:00,71eff25f-0960-4ab7-bbc9-564044dde0fe;,0,TOTVS Gestão Financeira,312,Boleto Itaú.2.1,Cópia de Cópia de Boleto Itaú,08/04/2016 07:49:00,c9c51350-3cfa-410e-b818-224a013d0296;,0,TOTVS Inteligência de Negócios,316,filtrosNomeados,filtrosNomeados,11/04/2016 10:37:12,d19713e7-eda0-4bf1-8e92-140714240c16;,0,TOTVS Educacional,31,EDUREL002,Listagem de Alunos com foto,06/10/2010 15:43:00,b84b941c-54e5-43c1-996b-3e9eae05e902.......    ]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Parâmetros

Esse método não possui parâmetros

]]>

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
FVWebService
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
RM\_IwsFormulaVisual
»
![](/download/attachments/309398329/loop3.png?version=2&modificationDate=1509366835997&api=v2)
Execute

![](/download/attachments/309398329/cogwheel-arrow.png?version=1&modificationDate=1509556752957&api=v2)
Fórmula Visual: Configuração de Atividades

![](/download/attachments/309398329/workflow.png?version=1&modificationDate=1509556254724&api=v2)
Fórmula Visual **"teste\_formula"**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

Foi adicionado uma Atividade de Gerar Exceção **"rmsThrowActivity"**.

]]>]]>

Configuração da Atividade:

]]>

![](/download/attachments/309398329/xml-file.png?version=1&modificationDate=1509371596771&api=v2)
Web Service: Modelo XML

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
Execute **(Requisição e Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Executa uma Fórmula Visual.]]>false.Requestxml1Requesttrue



1
2
[Parâmetro Opcional --> Adicione aqui o contexto de execução da fórmula visual]
[Parâmetro Opcional --> Adicione o xml do dataSet que será utilizado na execução da fórmula visual]
[Parâmetro Opcional --> Adicione o xml dos parâmetros utilizados na execução da fórmula visual]
[Parâmetro Opcional --> Adicione um valor específico que será utilizado na execução da fórmula visual]
]]>ResponsexmlResponse




Mensagem de Erro Customizada: Fórmula executada com sucesso!
Fórmula Visual: 'teste\_formula'.
RM.Lib.Workflow.RMSWorkflowException
]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Web Service: Parâmetros

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
CodColigada **(Obrigatório)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Código da Coligada em que a Fórmula Visual foi criada.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente uma coligada cadastrada na base do **RM**, em conjunto com o **IdFormula**, retornam um **XML** contendo todas as informações dos parâmetros presentes na **Fórmula Visual** demandada.  
**Valor Utilizado na Requisição:** 1

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
IdFormula **(Obrigatório)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Código Identificador da Fórmula Visual.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o número identificador de uma **Fórmula Visual**, em conjunto com o parâmetro **CodColigada** retornam um **XML** contendo todas as informações dos parâmetros presentes na **Fórmula Visual** demandada.  
**Valor Utilizado na Requisição:** 2

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Context **(Opcional)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Contexto do RM.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente o contexto do **RM** em que a **Fórmula Visual** será executada.  
**Valor Utilizado na Requisição:** N/A  
**Exemplo de Utilização:** CODSISTEMA=G,CODUSUARIO=mestre,CODCOLIGADA=1

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
DataSetXML **(Opcional)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Fonte de Dados em formato XML.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico **(XML)** que represente a **fonte de dados (DataSet)** cuja **Fórmula Visual** irá utilizar, seja como fonte principal de dados, seja como fonte de pesquisa, seja como fonte alternativa de dados.  
**Valor Utilizado na Requisição:** N/A  
**Alerta de valores a ser utilizados:** Os valores utilizados devem ser válidos como o exemplo abaixo, ou o campo em branco.
**Exemplo de Utilização:**  

]]>xml1Exemplo de XML de Fonte de Dadostrue

mestre
Usuário Mestre
Acesso02
1
1997-01-01T00:00:00
2015-07-03T14:48:08.447
mestre@totvs.com.br
]]]]>]]>

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
ParametersXML **(Opcional)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Parâmetros da Fórmula Visual em formato XML.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico **(XML)** que represente os **parâmetros** que a **Fórmula Visual** irá utilizar.  
**Valor Utilizado na Requisição:** N/A  
**Alerta de valores a ser utilizados:** Os valores utilizados devem ser válidos como o exemplo abaixo, ou o campo em branco.
**Exemplo de Utilização:**

]]>xml1Exemplo de XML de Fonte de Dadostrue

1

00041
AIRTON SENA JUNIOR
]]]]>]]>

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
OwnerData **(Opcional)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Dados do Usuário.  
**Tipo:** Cadeia de Caracteres (String)
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente dados adicionais diversos a serem utilizados na **Fórmula Visual**.  
**Valor Utilizado na Requisição:** N/A  
**Exemplo de Utilização:** (Qualquer valor, depende de várias vaiáveis, como: DataServer, Serviço de um WebService, etc...)

]]>

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
FVWebService
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
RM\_IwsFormulaVisual
»
![](/download/attachments/309398329/loop3.png?version=2&modificationDate=1509366835997&api=v2)
GetParams

![](/download/attachments/309398329/cogwheel-arrow.png?version=1&modificationDate=1509556752957&api=v2)
Fórmula Visual: Configuração de Atividades

![](/download/attachments/309398329/workflow.png?version=1&modificationDate=1509556254724&api=v2)
Fórmula Visual **"teste\_formula"**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

No grid principal da Fórmula Visual, existe um parâmetro **"Definição dos Parâmetros de Execução"**, clique em **[...]**, para definir os parâmetros que serão utilizados na Fórmula Visual .

]]>]]>

Definindo os parâmetros da Fórmula Visual:

]]>]]>

Definindo se deve ou não mostrar o esquema:

]]>]]>

Definindo se a estrutura das colunas com valores padrão será apresentada:

]]>

![](/download/attachments/309398329/xml-file.png?version=1&modificationDate=1509371596771&api=v2)
Modelo XML

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
GetParams **(Requisição e Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Recupera os Parâmetros de uma Fórmula Visual.
]]>false.Requestxml1Requesttrue




1

2
 ]]>Response

Parâmetro "Incluir Novo Registro na Tabela de Parâmetros" marcado.

xmlResponse





0

String
String
]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Parâmetros

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
CodColigada **(Obrigatório)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Código da Coligada em que a Fórmula Visual foi criada.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente uma coligada cadastrada na base do **RM**, em conjunto com o **IdFormula**, retornam um **XML** contendo todas as informações dos parâmetros presentes na **Fórmula Visual** demandada.  
**Valor Utilizado na Requisição:** 1

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
IdFormula **(Obrigatório)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Código Identificador da Fórmula Visual.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o número identificador de uma **Fórmula Visual**, em conjunto com o parâmetro **CodColigada** retornam um **XML** contendo todas as informações dos parâmetros presentes na **Fórmula Visual** demandada.  
**Valor Utilizado na Requisição:** 2

]]>

![](/download/attachments/309398329/folder3.png?version=2&modificationDate=1509366835661&api=v2)
FVWebService
»
![](/download/attachments/309398329/transfer3.png?version=2&modificationDate=1509366835358&api=v2)
RM\_IRMSServer
»
![](/download/attachments/309398329/loop3.png?version=2&modificationDate=1509366835997&api=v2)
Implements

![](/download/attachments/309398329/xml-file.png?version=1&modificationDate=1509371596771&api=v2)
Modelo XML

![](/download/attachments/309398329/programming-code.png?version=1&modificationDate=1509451197195&api=v2)
Implements **(Requisição e Resposta)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Serviço que permite implementar uma propriedade tipada.]]>false.Requestxml1Requesttrue







]]>ResponsexmlResponse   0,TOTVS Educacional,306,Boletim,Boletim,06/10/2010 15:43:00,597e2978-351d-4629-a2fb-b57432cad210;,0,TOTVS Educacional,30,Contrato,Contrato,06/10/2010 15:43:00,71eff25f-0960-4ab7-bbc9-564044dde0fe;,0,TOTVS Gestão Financeira,312,Boleto Itaú.2.1,Cópia de Cópia de Boleto Itaú,08/04/2016 07:49:00,c9c51350-3cfa-410e-b818-224a013d0296;,0,TOTVS Inteligência de Negócios,316,filtrosNomeados,filtrosNomeados,11/04/2016 10:37:12,d19713e7-eda0-4bf1-8e92-140714240c16;,0,TOTVS Educacional,31,EDUREL002,Listagem de Alunos com foto,06/10/2010 15:43:00,b84b941c-54e5-43c1-996b-3e9eae05e902.......    ]]>

![](/download/attachments/309398329/preference.png?version=1&modificationDate=1509369965368&api=v2)
Parâmetros

![](/download/attachments/309398329/cube.png?version=1&modificationDate=1509370590936&api=v2)
Type **(Opcional)**![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Descrição:** Tipo

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
]]>Utilização do Método Get Parameters

Ao utilizar método "Get Parameters" é gerado uma estrutura (esqueleto) para que o usuário utilize-o através do método "Execute", adicionando assim os parâmetros da sua execução."

Utilização de Web Services

Para utilização dos Web Services através do aplicativo **"Totvs Web Service Client"**, **clique [aqui](http://tdn.totvs.com/x/yBdFCg)**.

```

```

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.x

false

**Processo:** Web Services Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:** //27/10/2017

false

**Autores:**
