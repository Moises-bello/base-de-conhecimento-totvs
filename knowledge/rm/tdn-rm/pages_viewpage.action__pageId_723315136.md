---
content_hash: aba65501d9cfa1e534ae66f5c46fb24c8bddd74cc83b456a592ce647f0d83cf7
fetched_at: '2026-06-29T00:11:27.399273+00:00'
page_id: '723315136'
product: rm
source: tdn-rm
title: Redirecionamento de Requisições IIS para o Host
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=723315136
version: 20
---

## Objetivo

O objetivo deste documento é trazer orientações para utilizar os serviços TBC via Host do RM, sem expor publicamente todo o Host do RM.

Será descrito abaixo uma abordagem utilizando o IIS com os serviços de Proxy Reverso e URL Rewrite.

Serão demonstrados exemplos de Sites e Aplicativos o gerenciador do IIS que não refletem necessariamente como um ambiente de produção.

## Instalando Extensões no IIS

Será necessário instalar dois pacotes adicionais ao IIS.

* **Application Request Routing (Proxy Reverso)**  
  Poder ser instalado por este link, <https://www.iis.net/downloads/microsoft/application-request-routing>  
    
  Após a instalação, no gerenciador do IIS será apresentado um novo recurso.  
  Application Request Rounting Cache

* **URL Rewrite**  
  Pode ser instalado por este link, <https://iis-umbraco.azurewebsites.net/downloads/microsoft/url-rewrite>  
    
  Após a instalação será apresentado este novo recurso.  
  URL Rewrite

## Configurando o Proxy Reverso

Vamos ativar o recurso, Application Request Rounting Cache.  
Selecione o item Raiz na Aba Conexões.  
Realize um duplo clique sobre o ícone do recurso, após selecione na aba Ações, Server Proxy Settings.  
  
  
Marque o item Enable proxy, para habilitar o recurso.  
Após selecione Aplicar para gravar as alterações.

## Configurando o URL Rewrite

Para ativar este recurso, selecione na Aba Conexões o Site/Aplicativo que deverá ser configurado, conforme o seu ambiente.  
Realize um duplo clique no Recurso.  
Após selecione na aba Ações, Add Rule(s)...  
  
  
Selecionar a opção, Black rule, Regra em branco.

As regras serão adicionadas para cada serviço TBC utilizado.

Exemplo abaixo de uma regra para o serviço de Consultas SQL, **wsConsultaSQL**

1) Defina um nome para a regra.  
2) Informe uma expressão RegEx, conforme exemplo que corresponda com a Url de requisição.

Para este exemplo usamos a URL de requisição: **http://localhost/totvsbussinesconnector/wsConsultaSQL/IwsConsultaSQL**  
     Onde **http://localhost/totvsbussinesconnector** é o Site/Aplicativo configurado no IIS.  
     E o endpoint que informa o serviço TBC, **/wsConsultaSQL/IwsConsultaSQL**  
E para a regra o Pattern: ^wsConsultaSQL(/.+)?$

3) Selecione o tipo de Ação, Rewrite

4) Em Rewrite URL, informe a Url para o Host RM, para o serviço **wsConsultaSQL**     O parâmetro {R:1} vai repassar toda a parte do endpoint da requisição que será correspondido com o Pattern RegEx.  
5) Marque a opção, Stop processing.... para interromper o processamento das próximas regras.

UrlRewritePara este exemplo a URL de requisição deverá ser reescrita conforme a regra definida.

O resultado esperado para esta regra é a nova URL reescrita: **http://localhost:8051/wsConsultaSQL/IwsConsultaSQL**

Onde, **http://localhost:8051/wsConsultaSQL** é a parte fixa da URL informada.

E **IwsConsultaSQL**, é a parte repassada pela regra, vindo da URL original de requisição.

Dessa forma é reescrita uma nova URL para realizar a requisição via HOST RM.

Exemplo de uma regra para o serviço, **wsDataServer**.  
Para a URL de requisição: **http://localhost/totvsbussinesconnector/wsDataServer/IwsDataServer**  
A regra abaixo deverá reescrever para: **http://localhost:8051/wsDataServer/IwsDataServer**

## Configurando o RM.Host.exe.config

Devemos então adicionar a tag *ServicesBaseUrl* ao configurador do *host*:

xml]]>

## Expondo o serviço online

Para expor os serviços online, deve-se trocar a configuração feita total em **localhost** por uma que utiliza o IP ou *hostname* desejado. Assim, os redirecionamentos serão feitos para a máquina desejada.

## Exemplo utilizando o SOAP-UI

Para ilustrar de forma prática como as requisições podem ser realizadas, sem expor o Host RM, vamos demonstrar através do aplicativo SOAP-UI.

Partindo do pressuposto que o ambiente e o IIS, estejam configurados conforme os procedimentos já descritos neste documento.

**1) Criando um novo projeto no SOAP-UI**

Como as requisições estão sendo reescritas do IIS para o Host, devem ser verificadas a Url da Action, WebMethods e o XML, que devem estar conforme as configurações descritas em:

http://localhost:8051/wspageindex/

**2) Exemplo de Consulta SQL**

Requisição realizada da consulta SQL chamada "DiaFolga", por URL via IIS.

Neste caso a regra URL Rewrite, reescreveu e direcionou para o Host RM, localhost:0851, de forma transparente.

Veja que nesta requisição a URL não aponta para o Host (localhost:8051), mas para o IIS http://localhost/totvsbussinesconnector

O endpoint utilizado não deve conter por exemplo "wsConsultaSQL.**asmx**", mas "wsConsultaSQL/IwsConsultaSQL", seguindo a regra definida no

SoapActionImportante realizar a configuração do Header, SOAPAction, para o valor correspondente ao serviço requisitado, neste caso, <http://www.totvs.com/IwsConsultaSQL/RealizarConsultaSQL>

É um configuração necessária para auxiliar o IIS a filtrar e redirecionar corretamente a mensagem.

Mais informações, <https://www.w3.org/TR/2000/NOTE-SOAP-20000508>

**3) Exemplo de Leitura de dados de um usuário**

Requisição realizada para o DataServer GlbUsuarioData, por URL via IIS.

Da mesma forma do exemplo anterior a Url foi reescrita e direcionada para o Host RM.

Importante que o Header, SOAPAction também esteja configurado, .
