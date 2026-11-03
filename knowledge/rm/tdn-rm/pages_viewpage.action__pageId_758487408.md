---
content_hash: 2b8001d47ce37a916e043122298b4546892264ad18767926c0841efae44bc83c
fetched_at: '2026-06-29T00:11:33.374951+00:00'
page_id: '758487408'
product: rm
source: tdn-rm
title: API de Perfil do Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=758487408
version: 9
---

2

### Objetivo

API de manipulação de perfis para adicionar/remover perfis á um usuário sendo necessário realizar as operações de Post/Delete nas rotas conforme abaixo.

## 1- Post

**Máscara de Url:**  http://{domínio}:{porta}/api/framework/v1/users/{user}/roles

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**User:** Teste\_01

**Url Utilizada:** <http://localhost:8051/api/framework/v1/users/Teste_01/roles>

### Exemplo de entrada

jsJsontrue

## 2- Delete

**Máscara de Url:**  http://{domínio}:{porta}/api/framework/v1/users/{user}/roles/company/{company}/role/{role}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**User:** Teste\_01

**Company:** 1

**Role:** PERFIL-1

**Url Utilizada:** <http://localhost:8051/api/framework/v1/users/Teste_01/roles/company/1/role/PERFIL-1>

Coligada Zero (0)

É possível remover a associação de um mesmo perfil em todas as coligadas informando o valor Zero (0), na propriedade company.

**Exemplo:** [http://localhost:8051/api/framework/v1/users/Teste\_01/roles/company/0/role/PERFIL-COMUM](http://localhost:8051/api/framework/v1/users/Teste_01/roles/company/1/role/PERFIL-1)
