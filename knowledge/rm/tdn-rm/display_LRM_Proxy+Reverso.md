---
content_hash: 0491c28cbc8e042ec0d95a03743ff8310b08b381d40398889fc8818286628fb4
fetched_at: '2026-06-29T00:06:09.415131+00:00'
page_id: '203754339'
product: rm
source: tdn-rm
title: Proxy Reverso
type: documentation
url: https://tdn.totvs.com/display/LRM/Proxy+Reverso
version: 12
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso

Versão

 Disponível à partir da versão 12.1.8 da linha RM.

# Proxy Reverso

Como os serviços RESTful do RM ficam em um servidor diferente do servidor web utilizado para a publicação das páginas, é necessário redirecionar as solicitações aos serviços RESTful para outro servidor. Isso foi realizado configurando um proxy reverso no IIS.

Para ativar esse comportamento, basta adicionar o arquivo  no diretório root do IIS e instalar os módulos [Application Request Routing](http://www.iis.net/learn/extensions/installing-application-request-routing-(arr)) e [URL Rewrite](http://www.iis.net/downloads/microsoft/url-rewrite) no IIS (ambas instalações podem ser feitas via Web Plataform Installer).

Dessa forma todas as requisições que forem feitas aos serviços localizados em http://*hostname/rmsrestdataserver/rest* e http://*hostname**/rest* serão redirecionadas para o serviço do RM.Host na porta 8051 e não haverá necessidade de se informar a URL completa no factory dos serviços.

**OBS:** Note que o endereço do RM.Host deve ser modificado no web.config caso o mesmo não se encontre no mesmo servidor que o IIS.

## Configurando

1. Faça download do arquivo web.config e o copie para o diretório root do website em que o Frame HTML será publicado.
2. Instale o módulo Application Request Routing e após concluir a instalação, acesse o Gerenciador do IIS, selecione o Server, abra as configurações do módulo Application Request Routing, clique em Server Proxy Settings e depois marque a opção Enable Proxy.
3. Verifique se o módulo URL Rewrite está instalado no IIS. Caso não esteja, instale-o.

## Regras

Atualmente existem duas regras configuradas. A regra **RMSRestDataServer** fará com que todas as requisições feitas ao IIS no endereço [http://hostname/rmsrestdataserver/rest/...,](http://hostname/rmsrestdataserver/rest,) sejam redirecionadas para <http://rmhostaddress:8051/rmsrestdataserver/...> .

Já regra **RMSRest**irá redirecionar todas as requisições feitas em <http://hostname/rest/...> para <http://rmhostaddress:8051/rest/...> .

## Factories - Frame HTML

Ao utilizar o proxy reverso, não será mais necessário informar a URL completa dos serviçoes RESTful do RM.Host na factory dos serviços das páginas.

Sem proxy reversotruejs1Com proxy reversotruejs1

Atualmente e
