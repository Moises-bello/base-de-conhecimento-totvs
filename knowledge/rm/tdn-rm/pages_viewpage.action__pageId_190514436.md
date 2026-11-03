---
content_hash: 1c052bc0b16e622486e89e6ee1bc60ab673efdbc80ff83f43730c9e9801d6e24
fetched_at: '2026-06-29T00:05:59.398021+00:00'
page_id: '190514436'
product: rm
source: tdn-rm
title: 2. Configuração do servidor Web
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=190514436
version: 3
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso.

Versão

 Disponível à partir da versão 12.1.6 da linha RM.

Como todos os serviços (backend) serão providos pelo RM Host RM, as páginas web poderão ser publicadas em qualquer servidor web. Neste exemplo o servidor web será configurado no IIS e no TomCat. Como as requisições serão enviadas de domínios diferentes do domínio do RM Host a opção de cross-domain foi habilitada em todas as requisições do serviço IRMSRestDataServer.

Para fazer a configuração do servidor web, deve-se fazer download da aplicação de referência do .

# IIS

* Copiar o diretório html-app da aplicação de referência para o Aplicativo Default Web Site (ex: C:\inetpub\wwwroot).
* Criar uma pasta no Aplicativo Default para a publicação das páginas criadas para o segmento (ex: C:\inetpub\wwwroot\html-globais).

IIS - Exemplo

# TomCat

* Copiar o diretório html-app da aplicação de referência para o diretório webapps do TomCat (ex: C:\apache-tomcat-8.0.21\webapps).
* Criar uma pasta dentro do diretório webapps do TomCat para a publicação das páginas criadas para o segmento (ex: C:\apache-tomcat-8.0.21\webapps\html-globais).

*Opcionalmente podem ser copiados as demais pastas da aplicação de referência para o diretório webapps. Isso habilitará a execução da aplicação exemplo feita em Java* (html-sample)

TomCat - Exemplo

É necessário que os diretórios sejam publicados no root do servidor web utilizado. Por exemplo, não é possível criar um diretório virtual no IIS e copiar a aplicação de referência para o diretório virtual.
