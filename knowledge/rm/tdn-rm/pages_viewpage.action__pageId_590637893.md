---
content_hash: d85a8c034f400c1097248887e0d483f7113c9bc2325ddc36ebfeed3203b6f8df
fetched_at: '2026-06-29T00:10:56.119077+00:00'
page_id: '590637893'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Consultar Status de Todas as Licenças
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590637893
version: 6
---

A partir da versão 12.1.29, o Dataserver **ImbStatusLicencasTodosAppsData** passou a ficar disponível para ser executado utilizando uma ferramenta de terceiros, como o Soapui. Sua função é a de retornar dados atuais das licenças dos sistemas Portal de Imóveis e PDC, identificando possíveis problemas de consumo.

Segue o exemplo do Dataserver que pode ser utilizado dentro do SoapUI ou outra ferramenta que possibilite a execução de webservices:

ImbStatusLicencasTodosAppsData
1=1
CODCOLIGADA=1;CODSISTEMA=X;CODUSUARIO=mestre
]]>
