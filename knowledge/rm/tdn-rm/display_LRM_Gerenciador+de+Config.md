---
content_hash: 76613533eaf601fb138fca53dcc1b033294633a96cb1de248eea43b2d3c85254
fetched_at: '2026-06-29T00:05:57.300482+00:00'
page_id: '172295262'
product: rm
source: tdn-rm
title: Gerenciador de Config
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerenciador+de+Config
version: 174
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

       A funcionalidade **"Gerenciamento de Config"** tem por objetivo simplificar a maneira de administrar os arquivos de configurações das estações de trabalho, utilizando uma única interface. Com a unificação do arquivo de configuração podemos visualizar, incluir, excluir e alterar as configurações de qualquer estação mesmo estando desligada.

A partir da versão 12.1.27, será apresentado um modelo diferente de Config. Global, em JSON.

Atenção

Observação

Para a execução de TLS 1.1 e 1.2 no Windows 7 é necessário adicionar os registros abaixo, visto que são os protocolos de comunicação ativos atualmente e que por padrão não são ativos na versão Windows7:

Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]  
"DisabledByDefault"=dword:00000000

**Arquivo disponível para download:** [Arquivo.reg](https://tdn.totvs.com/download/attachments/215482828/arquivo.reg?version=1&modificationDate=1590091618463&api=v2)

## **02. EXEMPLO DE UTILIZAÇÃO**

### **INSTALADORES**

**Instruções:**  
  
       1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte)  
       2. Faça o login, com seu Email e Senha.  
       3. Na barra de menu superior, clique em DOWNLOAD.  
       4. No boxe “Central de Downloads” pesquise pela versão da biblioteca RM.  
   
       Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download. Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid ou no link da versão selecionada.

       Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
    

Para facilitar na busca do arquivo, utiliza-se o campo “Filtro” da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

**Requisitos:**

* **Linha de Software:** RM
* **Versão:** 12.01.01 e posteriores
* **Data de Liberação:** Outubro/2014
* **Observação:** Para requisitos de software consulte nossa portabilidade: [Portabilidade RM 12.01](http://tdn.totvs.com/display/LRM/PORTABILIDADE?preview=/223163740/240976657/Portabilidade%20e%20Arquitetura%20RM%2012.1.pdf)

### **COMO CONFIGURAR**

       Para utilizar esta configuração é necessário o compartilhamento de uma pasta em rede contendo o arquivo **"Configuracaorm.config"**. Neste arquivo constará o cadastro do aplicativo desejado, utilizando as configurações desejadas para o seu ambiente.                           

| Arquivo Configuracaorm.config | Arquivo exemplo: RM.Host.exe.config |
| --- | --- |
| 150 | 150 |

       Disponibilizado o arquivo em rede torna-se necessário ajustar os arquivos de conexão (RM.Host.exe.config, RM.Host.Service.exe.config) e aplicações (RM.exe.Config, RMBis.exe.config, RMLabore.exe.config etc) em cada estação utilizada.

       Dentro do arquivo de configuração, em cada estação, remova todo o contexto que esteja dentro de **<appSettings>** e substitua por tag **<add key="configpath" value="\\PastaCompartilhadaNaRede" />.** O tag ConfigPath deve ser preenchido com o diretório onde o arquivo **"Configuracaorm.config"**foi compartilhado.

       Abaixo um exemplo de como ficarão os arquivos de configurações em cada estação:

| Máquina que **não utiliza** o Gerenciamento de config | Máquina que **utiliza** o gerenciamento de config |
| --- | --- |
| <?xml version="1.0"?> <configuration> <appSettings> <add key="JobServer3Camadas" value="false" />     <add key="Port" value="8050" />     <add key="Host" value="localhost" />    <add key="LibPath" value="C:\totvs\CorporeRM\RM.Net" /> </appSettings> </configuration> | <?xml version="1.0"?> <configuration> <appSettings> <add key="CONFIGPATH" value="\\PastaCompartilhadaNaRede" /> </appSettings> </configuration> |

       Após realizar estas configurações o ambiente está preparado para utilizar o arquivo unificado de configuração.

Observações: *Caso o arquivo de configuração possua somente permissão de leitura, não será possível inserir novas estações no configurador. Será utilizado então as configurações default do arquivo compartilhado.*

### **COMO FUNCIONA**

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

![](/download/thumbnails/172295262/cogwheel-arrow.png?version=1&modificationDate=1510689248000&api=v2)
Fluxo de Execução **(Gerenciador de .Config)**

![](/download/attachments/172295262/hierarchical-structure.png?version=1&modificationDate=1510689248000&api=v2)
Diagrama do Fluxo de Execução

![](/download/attachments/172295262/frame-landscape.png?version=1&modificationDate=1510689248000&api=v2)
Imagem![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

**Aplicativo:** RM.Host.ServiceManager.exe

]]>

![](/download/attachments/172295262/tablet.png?version=1&modificationDate=1510691345360&api=v2)
Descrição do Diagrama![](/download/attachments/309398329/add.png?version=1&modificationDate=1509382756808&api=v2)

O fluxo abaixo refere-se à criação e a alteração dos registros no Configurador Global.

]]>

**1) Inicio do Fluxo** **→** CreateFile();

]]>

**Verifica o Registro →** [Nome do Aplicativo] + [Domínio] + [Nome da Máquina]; **EX:** **RM.EXE\_BH01\_TESTE**.

]]>

**Caso o Registro exista** **→**

* Altera o registro com as modificações realizadas.
* Save(); //Salva as alterações no registro.

]]>

**Fim do Fluxo →** Fim do CreateFile();

]]>]]>

**2)** **Inicio do Fluxo** → Verifica o Registro [Nome do Aplicativo] + [Domínio] + "Default"; **EX:** **RM.EXE\_BH01\_DEFAULT**.

]]>

**Caso o Registro exista →** Verifica a tag **CONFIGAUTOGENERATE**.

]]>

**Se estiver com o valor true →**

* Cria o registro[Nome do Aplicativo] + [Domínio] + [Nome da Máquina] **EX:** **RM.EXE\_BH01\_TESTE**.
* Save(); //Salva as alterações no registro.

]]>

**Se estiver com o valor false →**Uma mensagem é enviada ao Usuário.

]]>

**Fim do Fluxo →**Fim do CreateFile();

]]>]]>

**3)** **Inicio do Fluxo →** Verifica o Registro [Nome do Aplicativo - Principal (Sem múltiplos hosts)] + [Domínio] + "Default"; **EX:** **RM.EXE\_BH01\_DEFAULT**.

]]>

**Caso o Registro exista →**

* Cria o registro[Nome do Aplicativo] + [Domínio] + "Default";**EX: RM.EXE\_BH01\_DEFAULT.**
* Save(); //Salva as alterações no registro.
* Verifica a tag **CONFIGAUTOGENERATE**.

]]>

**Se estiver com o valor true →** Cria o registro[Nome do Aplicativo] + [Domínio] + [Nome da Máquina] **EX:** **RM.EXE\_BH01\_TESTE**.

]]>

**Fim do Fluxo →**Fim do CreateFile();

]]>]]>

**4)** **Inicio do Fluxo →** Verifica o Registro [Nome do Aplicativo] + "Todos" + "Default"; **EX:** **RM.EXE\_TODOS\_DEFAULT**.

]]>

**Caso o Registro exista →**

* Cria o registro[Nome do Aplicativo] + [Domínio] + "Default";**EX: RM.EXE\_BH01\_DEFAULT**.
* Save(); //Salva as alterações no registro.
* Verifica a tag **CONFIGAUTOGENERATE**.

]]>

**Se estiver com o valor true →** Cria o registro[Nome do Aplicativo] + [Domínio] + [Nome da Máquina] **EX:** **RM.EXE\_BH01\_TESTE**.

]]>

**Fim do Fluxo →**Fim do CreateFile();

]]>]]>

**5)** **Inicio do Fluxo →** Verifica o Registro [Nome do Aplicativo - Principal (Sem múltiplos hosts)] + "Todos" + "Default"; **EX:** **RM.EXE\_TODOS\_DEFAULT**.

]]>

**Caso o Registro exista →**

* Cria o registro[Nome do Aplicativo] + [Domínio] + "Default";**EX: RM.EXE\_BH01\_DEFAULT**.
* Save(); //Salva as alterações no registro.
* Verifica a tag **CONFIGAUTOGENERATE**.

]]>

**Se estiver com o valor true →** Cria o registro[Nome do Aplicativo] + [Domínio] + [Nome da Máquina] **EX:** **RM.EXE\_BH01\_TESTE**.

]]>

**Fim do Fluxo →**Fim do CreateFile();

]]>]]>

**6)** **Inicio do Fluxo →** Verifica o Registro "RM" + "Todos" + "Default"; **EX:** **RM\_TODOS\_DEFAULT**.

]]>

**Caso o Registro exista →**

* Cria o registro[Nome do Aplicativo] + [Domínio] + "Default";**EX: RM.EXE\_BH01\_DEFAULT**.
* Save(); //Salva as alterações no registro.
* Verifica a tag **CONFIGAUTOGENERATE**.

]]>

**Se estiver com o valor true →** Cria o registro[Nome do Aplicativo] + [Domínio] + [Nome da Máquina] **EX:** **RM.EXE\_BH01\_TESTE**.

]]>

**Se estiver com o valor false →** Levanta uma exceção ao Usuário **(REGISTERNOTFOUND)**.

]]>

**Fim do Fluxo →**Fim do CreateFile();

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

O arquivo "**Configuracaorm.config**" armazenará as configurações de cada aplicativo. Para cada primeiro acesso, será inserido um novo registro com as configurações **padrões** referente à aplicação acessada.

falseRegistrosRegistro PadrãoRegistro PadrãoRegistro Padrão

       É necessário que o arquivo "**Configuracaorm.config**" possua um registro padrão contendo as configurações desejadas, para cada aplicativo a ser utilizado.

   *Exemplo:*

     Para o aplicativo RM.exe, executado no domínio BH01, será respeitada a seguinte identificação:

**RM.exe****\_BH01****\_****DEFAULT**onde default será o padrão de configuração para todos os novos registros de aplicativos **RM.exe** que estiverem do domínio **BH01**, respeitando a nomenclatura da opção Novo Registro.

***Exemplo de Registro Padrão:***

xml







]]>Observações: *Se não for necessário criar novos registros para cada estação basta alterar o valor da tag <add key="CONFIGAUTOGENERATE" value="True" />, de: "True" para: "False" no Registro padrão.*Observações:

*Lembrando que o CONFIGAUTOGENERATE cria um novo registro baseado nas estações de trabalho, outros registros podem ser criados independente da tag estar "true" ou "false", como um exemplo, o registro RM.EXE.BH01.DEFAULT.*

*Alterar o valor do CONFIGAUTOGENERATE, aplica-se apenas aos registros baseados nas estações de trabalho. Por exemplo, alterando o valor de "true" para "false" fará com que apenas os registros das estações de trabalho não sejam criados.*

Novo RegistroNovo RegistroNovo Registro

    O **novo** registro será inserido levando em consideração as configurações do **Registro Padrão** e respeitando a seguinte identificação:

**Nome do aplicativo** + **\_** + **Domínio do usuário** + **\_** + **Nome da máquina**

   Exemplo*:*

* Nome do aplicativo: RM.EXE
* Domínio do usuário: BH01
* Nome da máquina: Teste

***Como ficará o novo registro no arquivo:***

xml







]]>Observações: *Caso o arquivo de configuração possua permissão de somente leitura, não será possível inserir novas estações no configurador, sendo utilizado as configurações existentes no arquivo.*false

**Versão:** 12.01.XX
