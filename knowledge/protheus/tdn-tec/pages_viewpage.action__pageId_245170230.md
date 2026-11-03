---
content_hash: 00ae8ff6ac9b58abd4a419ef80d6a39a2ed580c61064437b8c7fbbafb5a3e44a
fetched_at: '2026-07-02T19:24:20.414933+00:00'
page_id: '245170230'
product: protheus
source: tdn-tec
title: Remoção da opção BrowserEnabled do arquivo smartclient.ini
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=245170230
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Melhoria | A utilização do componente TIBrowser só era possível se no arquivo smartclient.ini fosse incluída a chave BrowserEnabled=1, caso contrário, a url passada na construção deste componente não era respeitada, apresentando apenas uma página em branco (about:blank).  A partir da versão 2.3.5 do SmartClient HTML esta chave não será mais verificada, com isso, sempre será aberta a url indicada na construção do componente. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-453 * Disponível a partir da build 7.00.131227A - 2.3.5 |
