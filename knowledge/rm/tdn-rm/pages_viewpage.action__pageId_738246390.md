---
content_hash: 8be7524ae28bf06ceb00f1226800a129119590f1c201292adeeb38646e9cdbfd
fetched_at: '2026-06-29T00:11:31.509881+00:00'
page_id: '738246390'
product: rm
source: tdn-rm
title: Desativar uso de Resource para tradução de idiomas nos Módulos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=738246390
version: 4
---

# Índice:

---

# Objetivo:

---

Configuração da Tag para desabilitar a tradução de idiomas para os textos de módulos e segmentos no Menu da MDI.

Ao adicionar o valor = true para Tag DisableSegmentAndModuleResource, o menu de módulos e segmentos não utilizará o Resource de idiomas, disponibilizado pelo instalador.

# Configuração:

---

Adicionar a Tag nos arquivos "RM.Host.exe.config", "RM.host.Service.exe.config" dos servidores.

**Exemplo:** <add key=“DisableSegmentAndModuleResource” value=“true” />

A partir da versão 12.1.2302, o RM passa a utilizar os Resources disponibilizados na instalação, para tradução de idiomas dos Menus globais e dos textos de módulos e seguimentos.

Por padrão será sempre utilizado o Resource, caso algum cliente já tenha escolhido realizar a tradução dos textos direto no banco de dados, esta Tag poderá ser utilizada para manter a tradução de idioma ja utilizada.
