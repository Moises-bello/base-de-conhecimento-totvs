---
content_hash: 6fd27b3974ffb2ff5e19866b36be82624729f2951ec1c12b41ac99054e2a27b9
fetched_at: '2026-06-28T21:35:23.338271+00:00'
page_id: '244742883'
product: fluig
source: tdn-fluig
title: BPM 062 -  É possível restringir a permissão de cancelar solicitações?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244742883
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Gostaria de restringir a permissão de cancelar solicitações para o usuário que inicializou a mesma.

# Solução

Não é possível restringir o cancelamento de solicitação para o usuário que a abriu.

Pelo comportamento padrão do produto, o usuário que iniciou uma solicitação sempre terá permissão para realizar cancelamento. Contudo, através do desenvolvimento sobre a plataforma, é possível bloquear a ação de cancelamento utilizando o evento beforeCancelProcess. Este evento é ativado antes do cancelamento de uma solicitação.

É necessário incluir uma validação neste evento para definir se o usuário poderá ou não cancelar a solicitação e, caso o objetivo seja não permitir o cancelamento, utilizar um *throw***.**

Em [Desenvolvimento de Workflow](http://tdn.totvs.com/pages/viewpage.action?pageId=270921008) há mais detalhes sobre como utilizar o beforeCancelProcess.

No fluig Help há informações sobre o [cancelamento de solicitações](http://tdn.totvs.com/pages/releaseview.action?pageId=233763398).
