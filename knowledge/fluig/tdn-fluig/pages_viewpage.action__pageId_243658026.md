---
content_hash: 3f45c152b0134f4dd1e1c023241a36e23df3d798e891e843add8deff1e4d878f
fetched_at: '2026-06-28T21:35:23.086651+00:00'
page_id: '243658026'
product: fluig
source: tdn-fluig
title: FORM 002 - Por que ocorre erro ao transferir dados entre formulários com pai
  x filho?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243658026
version: 11
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:  fluig**

**Versão: Todas**

# Ocorrência

Ao mover a tarefa de um subprocesso recebemos o erro abaixo e não podemos mover de um estado para o outro:

 is not in a valid state to be invoking ]]>

# Causa

A situação reportada ocorre pois no formulário pai há um campo do tipo Pai X Filho e na função implementada para copiar os dados do formulário pai para o formulário do subprocesso, não estão sendo adicionadas linhas no novo Pai x Filho. Sendo assim, o fluig tenta incluir dados em campos que não existem.

# Solução

Para corrigir esta situação, deve ser utilizada a função wdkAddChild('[nome-do-paifilho]') antes de definir os valores, [conforme exemplo](http://tdn.totvs.com/x/AhBbCw).
