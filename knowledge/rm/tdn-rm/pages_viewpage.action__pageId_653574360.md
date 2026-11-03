---
content_hash: fbac1b20a0cb6b965481bb06b531a5a55643c8265a8d203d8679452c83f1fb40
fetched_at: '2026-06-29T00:11:12.490238+00:00'
page_id: '653574360'
product: rm
source: tdn-rm
title: Configuração da Tag TenantPathEnabled
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=653574360
version: 5
---

# Índice:

---

# Objetivo:

---

Tem como objetivo mostrar o funcionamento do path tenantizado.

Ao habilitar a Tag TenantPathEnabled no Host, os métodos que retornam o path do servidor, serão combinados com o Alias, realizando assim a tenantização do path.

Classe RMSFileServerModule

Métodos, GetFileServerPath() e GetFilePath()

Caso ocorra uma chamada sem login ou sem alias definido o path permanece inalterado, retornando o padrão ou o que foi configurado na Tag FileServerPath.

# Configuração:

---

Adicionar a Tag nos arquivos "RM.Host.exe.config", "RM.host.Service.exe.config" dos servidores.

**Exemplo:** <add key=“TenantPathEnabled” value=“True” />

Mais informações, Utilizando o [RMSFileServerModule](https://tdn.totvs.com/display/LRM/Utilizando+a+classe+RMSFileServerModule).

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.34

false

**Processo:** Configuração da Tag TenantPathEnabled

falsefalse

**Status:** Finalizado

false

**Data:** 02/12/2021

false

**Autores:**
