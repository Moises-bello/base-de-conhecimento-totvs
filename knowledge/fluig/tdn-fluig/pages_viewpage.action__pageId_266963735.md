---
content_hash: 59d4779f1fbfc333b5c8ec66466ccce171e28db7de4d4c7f3cf458cf18f342fa
fetched_at: '2026-06-28T21:35:23.844458+00:00'
page_id: '266963735'
product: fluig
source: tdn-fluig
title: DES - É possível mudar o prazo de diversas atividades, com a condição de um
  checkbox no formulário?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266963735
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Gostaria de saber se é possível mudar o prazo de conclusão de diversas atividades, com a condição de um *checkbox* no formulário.

# Solução

Você pode implementar os *checkbox*es no formulário e utilizar o método setDueDate:

setDueDate(numProcesso, numThread, "userId", dataConclusao, tempoSeg)

Este método permite alterar o prazo de conclusão para uma determinada atividade do processo, onde:

* numProcesso: número da solicitação;
* numThread: número da thread (normalmente 0, quando não se utiliza atividades paralelas);
* userId: o usuário responsável pela tarefa;
* dataConclusao: a nova data de conclusão;
* tempoSeg: tempo que representa a nova hora de conclusão, calculado em segundos após a meia-noite.

Você pode encontrar exemplos em:
