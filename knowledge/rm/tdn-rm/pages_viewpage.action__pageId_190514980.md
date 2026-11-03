---
content_hash: b5e434ecd1e9851e289802cae092bf20728ef462067ae946e8b27d40330081bc
fetched_at: '2026-06-29T00:05:59.401695+00:00'
page_id: '190514980'
product: rm
source: tdn-rm
title: 3. Configuração do IDE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=190514980
version: 5
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso

Versão

 Disponível à partir da versão 12.1.6 da linha RM.

Após a instalação do [IDE](http://tdn.totvs.com.br/display/tec/3.+IDE) do TOTVS | HTML Framework, incluir o endereço do repositório WADL dos serviços RESTful dos dataserver RM http://<servidor>:8051/RMSRestDataServer/getAvailableServices.

Repositórios

Criar um novo projeto no TOTVS | Developer Studio e a pasta onde as páginas referentes ao segmento/produto serão publicadas (ex: html-globais). Na pasta criada, deverão ser adicionais os diretórios html e i18n. No diretório 118n deverá ser criado o arquivo de traduções translations.js.

Nas propriedades do projeto que foi criado, deve-se configurar o diretório que será copiado para o servidor web. Nesse exemplo deve-se mapear a pasta html-globais do projeto para o diretório C:\inetpub\wwwroot\html-globais do servidor web.

Web Content Folder
