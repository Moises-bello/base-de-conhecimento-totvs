---
content_hash: beb9d7a4506a1451bd86b0f926b24f7fbbdd45fa9f03ac098333d55ab830eb55
fetched_at: '2026-06-29T00:09:14.193406+00:00'
page_id: '421385148'
product: rm
source: tdn-rm
title: Ajuste de Hierarquia de Tarefas
type: documentation
url: https://tdn.totvs.com/display/LRM/Ajuste+de+Hierarquia+de+Tarefas
version: 2
---

Através deste assistente é possível identificar as tarefas que estão com a hierarquia incorreta, ou seja, tarefas que não possuem uma tarefa pai, tarefas que estão com a tarefa pai em um nível incorreto, tarefa que é um serviço filha de outra tarefa que é um serviço e obra que não está no nível 1.

**Exemplos**  
Tarefa sem tarefa pai: A tarefa 008.01.01.01 não possui uma tarefa pai. Essa tarefa deveria ser filha da tarefa 008.01.01. Se essa tarefa não existir, ela será criada e o identificador da tarefa pai será ajustado. Caso ela existam Será ajustado o identificador da tarefa pai.  
Tarefa com hierarquia em nível incorreto: Tarefa 008.01.01.02 é filha da tarefa 008. Essa tarefa deveria ser filha da tarefa 008.01.01. Se essa tarefa não existir, ela será criada e o identificador da tarefa pai será ajustado. Caso ela existam Será ajustado o identificador da tarefa pai.  
Tarefa que é serviço filha de outra tarefa que é serviço: Tarefa 008.01.01.03 filha da tarefa 008.01.01.02, sendo que ambas possuem um recurso associado ou valor cotado.  
Obra que não está no nível 1: Tarefa 008.01.01.02 que é uma obra.
