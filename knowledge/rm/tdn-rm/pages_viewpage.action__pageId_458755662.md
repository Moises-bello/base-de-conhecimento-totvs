---
content_hash: 3471db6fa3fa051bb68ad4df4817a77af85ef13ac16db04455f49afd1eea05ba
fetched_at: '2026-06-29T00:10:13.752580+00:00'
page_id: '458755662'
product: rm
source: tdn-rm
title: WSDataServer Tabelas Dinâmicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458755662
version: 32
---

# Data Server GlbGDinamData

O documento irá apresentar o funcionamento dos métodos referentes ao wsDataServer focando em tabelas dinâmicas

## Recuperar Todas as Tabelas Dinâmicas

Para recuperar todas as tabelas dinâmicas é necessário indicar no xml que será enviado ao endpoint <http://bhd000002282.bh01.local:8051/wsDataServer/IwsDataServer>:

* DataServerName, no caso **GlbGDinamData (Obrigatório)**
* Filtro **(Obrigatório)**

Exemplo

## Recuperar itens das Tabelas Dinâmicas

Para recuperar todas as tabelas dinâmicas é necessário indicar no xml que será enviado ao endpoint <http://bhd000002282.bh01.local:8051/wsDataServer/IwsDataServer>:

* DataServerName, o usuário deve passar o nome do dataserver com o nome da tabela separado por barra, por exemplo **GlbItemDinamData/PLANATIVO (Obrigatório)**
* Filtro **(Obrigatório)**

Exemplo

## Adicionar um novo item na Tabela Dinâmica

Para adicionar um item é necessário indicar no xml SaveRecord que será enviado ao endpoint [http://localhost:8051/wsDataServer/IwsDataServer](http://bhd000002282.bh01.local:8051/wsDataServer/IwsDataServer):

* DataServerName, o usuário deve passar o nome do dataserver com o nome da tabela separado por barra, adicionado de um array informando o código da coligada e o código da tabela separado por vírgula  
  por exemplo **GlbItemDinamData/GCONSIST/[0,GCODATIV] (Obrigatório)**
* XML, conteúdo dos dados do novo item a ser adicionado.

Exemplo
