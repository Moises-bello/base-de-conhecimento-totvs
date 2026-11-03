---
content_hash: c39f4306dac24f852c24de010dbe0b07314badafda52ea712f4aba0c630f5d50
fetched_at: '2026-06-28T21:35:23.243196+00:00'
page_id: '244711716'
product: fluig
source: tdn-fluig
title: BPM 059 - Por que a pesquisa pelo responsável do processo "Listar Tarefas"
  não traz nenhum informação?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244711716
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**Fluig

**Versão:** 1.5.9

**Banco de Dados:** MySQL

# Ocorrência

No processo "Listar Tarefas" padrão do produto, na opção adiciona tarefa e procurar o responsável não traz nenhuma informações do que foi digitado para pesquisa.

# Solução

O problema foi solucionado no EP1.5 da versão 1.5.9 para o banco MySQL.   
   
Obs.: O problema continua para o banco SQLserver, onde o campo traz o ID do usuário e não o nome do mesmo.
