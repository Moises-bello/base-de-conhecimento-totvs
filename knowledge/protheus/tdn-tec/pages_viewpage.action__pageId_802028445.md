---
content_hash: 94a9a3ca4f8e59ebb603b0180857e9c34c6f13e8a715d07d5547d6de3679aa2a
fetched_at: '2026-07-02T19:24:28.633579+00:00'
page_id: '802028445'
product: protheus
source: tdn-tec
title: Correção - Conexão ao SmartERP (MacOS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=802028445
version: 1
---

|  |  |
| --- | --- |
| Situação | Conectar em um servidor no smartERP com o MacOS estava demorando muito mais do que deveria |
| Ocorrência | Problema ocorre apenas em endereço http (SmartERP) |
| Correção | Devido ao endereço ser HTTP(s) e na maioria das vezes sem informação da porta explicitamente (internamente virava porta -1), fazia com que o MacOS demorasse muito mais para reportar uma falha. |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-4377 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.2.1 |
