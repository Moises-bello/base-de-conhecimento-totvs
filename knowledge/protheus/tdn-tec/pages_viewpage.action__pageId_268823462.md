---
content_hash: 0923851da118400d8c9c87268ec0776174b49db90f169286475fcac04a4299ff
fetched_at: '2026-07-02T19:24:22.186687+00:00'
page_id: '268823462'
product: protheus
source: tdn-tec
title: Seção [TDS] - TDS Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268823462
version: 2
---

Existe uma configuração para habilitar a aplicação de pacote de atualização em servidor remoto.

`ALLOWAPPLYPATCH=<estações permitidas>`

E uma configuração para habilitar a edição de servidor.

`ALLOWEDIT=<estações permitidas>`

Em ambas as configurações o parâmetro `<estações permitidas>` indica a lista de IPs, separados por vírgula, que podem efetuar a ação correspondente no servidor.

**Obs.**: Caso seja adicionado asterisco (`*`) em `<estações permitidas>` qualquer máquina estará habilitada para efetuar a ação correspondente nesse servidor.
