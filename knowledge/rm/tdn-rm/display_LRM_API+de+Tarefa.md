---
content_hash: 9c6b59002408df8a983642987efd5078e66db4f448fc2846b22ed28a34d89893
fetched_at: '2026-06-29T00:11:27.268364+00:00'
page_id: '721721138'
product: rm
source: tdn-rm
title: API de Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Tarefa
version: 9
---

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API para inserção, alteração e exclusão de múltiplas tarefas em lote.

# 1 - API de tarefa

---

Esta API permitirá a entrada de valores na tarefa como quantidade, unidade, valor cotado, campos livres e entre outros.

É utilizado nesta API todos os 4 métodos padrões da TOTVS: GET, POST, PUT, DELETE.

## **Inclusão de tarefas em lote:**

Usando a rota "batch" é possível inserir tarefas em lote no mesmo código JSON. Segue um exemplo abaixo utilizando o método POST:

Para acessar a API é necessário ter acesso à Planilha de Atividades nas permissões do usuário.

**Máscara de Url:** <http://localhost:8051/api/construction-projects/v1/activity-tasks>

**Batch**:  <http://localhost:8051/api/construction-projects/v1/activity-tasks/batch>

**Verbo:** POST

falseExemplo de JSon de entradaVer JSON...js1JSONtrue

## 

## **Alteração de tarefas em lote:**

**EndPoint:** <http://localhost:8051/api/construction-projects/v1/activity-tasks/batch>

**Verbo:** PUT

Observação: Devem ser passados todos os campos do registro retornados pelo verbo GET.

## **Exclusão de tarefas em lote:**

**EndPoint:** <http://localhost:8051/api/construction-projects/v1/activity-tasks/batch>

**Verbo:** DELETE

Observação: devem ser passados apenas a chave primária do registro.
