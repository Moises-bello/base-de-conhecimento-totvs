---
content_hash: d6603be9904be479277c913c2ea02bae4c73e3bbee3b17ed0f3511fe63cb95ef
fetched_at: '2026-06-28T21:35:19.953941+00:00'
page_id: '224448709'
product: fluig
source: tdn-fluig
title: DES - Tratamento de exceção no evento beforeStateLeave
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224448709
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Em um processo usamos o evento *beforeStateLeave* para executar um dataset que envia dados a um *web service*. O que precisamos é que, caso haja algum erro na execução deste método, o sistema não deixe movimentar a solicitação e apresente um erro.   
  
Porém, hoje o erro é apresentado somente no log e o *throw* não funciona em eventos de processo. Como fazemos neste caso?

# Solução

Existem alguns eventos de processos que não permitem a execução do *throw*. Isto ocorre devido ao tempo de execução do próprio evento.

Neste caso, é recomendado o envio dos dados no evento *beforeTaskSave*, que é executado antes da tarefa ser salva / movimentada, pois neste evento, é possível utilizar o *throw*.

# Observações

A documentação sobre o tratamento de exceções pode ser consultada em [Desenvolvimento de Workflow.](http://tdn.totvs.com/display/public/fluig/Desenvolvimento+de+Workflow#DesenvolvimentodeWorkflow-Tratamentodeexceções)
