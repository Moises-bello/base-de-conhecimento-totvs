---
content_hash: 11fcbb644be1aba12d092981d9ab186a262c91e0e4939120d781fa9267abcac6
fetched_at: '2026-06-29T00:11:16.347035+00:00'
page_id: '666820734'
product: rm
source: tdn-rm
title: Configuração da Tag DisableAntiXSSProtection
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=666820734
version: 2
---

# Índice:

---

# Objetivo:

---

Desativar o tratamento para evitar ataque por injeção, tipo XSS.

Por padrão este tratamento é realizado nas requisições, caso seja identificado uma possível ameaça o dado passado na requisição será removido.

# Configuração:

---

Adicionar a Tag nos arquivos "RM.Host.exe.config", "RM.host.Service.exe.config" dos servidores.

**Exemplo:** <add key=“DisableAntiXSSProtection” value=“true” />

Para desativar, informar o valor "true".
