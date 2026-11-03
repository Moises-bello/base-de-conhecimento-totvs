---
content_hash: ee0a383851578e0790b3cdb7d80aad8cfee48cebbf66123b5c9ca7da05224cac
fetched_at: '2026-06-29T00:08:23.911984+00:00'
page_id: '270098221'
product: rm
source: tdn-rm
title: Ocultar link para alterar senha do usuário no Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270098221
version: 3
---

# Índice

---

.\*ndice:

# Objetivo

---

        O objetivo deste documento é mostrar a configuração a ser feita no portal para ocultar o link 'Alterar senha' para o usuário logado. Essa funcionalidade está disponível a partir da versão 12.1.15, ou a partir do patch 12.1.14.104.

# Introdução

---

       Para ocultar o link 'Alterar senha' no portal basta configurar o parâmetro 'SHOWLINKCHANGEPASSWORD' no web.config com valor = false. (Veja os passos a seguir).

       O valor default desse parâmetro é true, ou seja, por padrão o link 'Alterar senha' será exibido para os usuários do portal:

# Passos para configuração do parâmetro

---

       Localize dentro da pasta CorporeRM do seu ambiente o arquivo WEB.config. Em seguida, adicione a tag abaixo dentro de <appSettings>.xml
]]>

       Adicionado o parâmetro, salve o arquivo e atualize a página do portal. Ao logar novamente, não será exibido o link para alterar a senha do usuário logado.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.15

false

**Processo:** Parâmetro SHOWLINKCHANGEPASSWORD

falsefalse

**Status:** Finalizado

false

**Data:** 26/12/2016

false

**Autores:**

**Douglas Maxwell de Oliveira**
