---
content_hash: 813abf2e31a989b565b9d86e332a1de5da0fec8831de30c40cdd48efe3987b11
fetched_at: '2026-07-02T19:24:26.756971+00:00'
page_id: '6064428'
product: protheus
source: tdn-tec
title: Como fazer para realizar a aplicação de licenças no c-tree Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6064428
version: 7
---

A instância do c-tree Server deve ser interrompida antes da aplicação de uma nova licença

Para aplicar a licença, utilize o executável fcactvat disponível juntamente do executável do c-tree Server e informe:

* A chave de liberação da FairCom
* Os 6 últimos dígitos do número de série disponibilizado pela FairCom
c-tree Server V8

Para licenças de mais de 128 usuários, é necessário inserir no arquivo de configuração do c-tree Server (ctsrvr.cfg) a chave USERS e a quantidade de usuários definida pela nova licença

Por exemplo, ao aplicar uma licença de 150 usuários, deve ser realizada a configuração abaixo:
