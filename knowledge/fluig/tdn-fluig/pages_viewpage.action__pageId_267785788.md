---
content_hash: 1ca9e2700f457d4891c94827ea14586a936f03741e0a4774c524b3a30d91a172
fetched_at: '2026-06-28T21:35:23.865919+00:00'
page_id: '267785788'
product: fluig
source: tdn-fluig
title: BPM 074 - Usuário integrador da plataforma consegue assumir as atividades de
  um processo em nome do usuário que foi designado como responsável?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267785788
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto: fluig**

**Versão:** 1.6.1

# Ocorrência

Recentemente foi lançamento uma nota a respeito de uma atualização do Fluig 1.6.1 relativo a segurança. Essa nota informa que:

"Utilizando o método takeProcessTask do serviço ECMWorkflowEngineService, um administrador da plataforma consegue assumir as atividades de um processo em nome do usuário que foi designado como responsável."

Nossa empresa utiliza webservices integrado ao Protheus para interagir com as atividades do Fluig. Nessa integração criamos um usuário "integrador" que "chumbamos" nos parâmetros do webservice "takeProcessTask" para realizar tais chamadas.

Nossa dúvida é que, de acordo com essa nota não poderemos mais usar esse formato?

Seremos obrigados a utilizar os parâmetros (username e password) do usuário que vai assumir a tarefa?

# Solução

É necessário que esse usuário com papel "integrador" tenha o papel de administrador para fazer a autenticação, no webservice você pode ter um grupo e assumir com um usuário que faz parte

deste pool, ao autenticar com o usuário administrador (requisito) você consegue assumir a tarefa deste usuário.
