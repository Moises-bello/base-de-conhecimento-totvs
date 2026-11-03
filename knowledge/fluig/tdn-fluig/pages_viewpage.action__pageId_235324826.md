---
content_hash: d9cdf29747c62ce9eaeb7b641e8275908387a667a4ff0ac7ce982d22baab23a8
fetched_at: '2026-06-28T21:35:22.124349+00:00'
page_id: '235324826'
product: fluig
source: tdn-fluig
title: BPM 026 - Como deixar visíveis os processos no menu Iniciar Solicitações?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235324826
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

Há vários processos criados no menu Configurar Processos do fluig. No entanto, estes processos não são apresentados no menu [Iniciar Solicitações](http://tdn.totvs.com/x/RvLuDQ).

# Causa

Há mecanismo de atribuição na atividade inicial do processo.

# Solução

Para que uma solicitação apareça para um usuário é necessário que este usuário esteja dentro do mecanismo de atribuição da atividade inicial.

Por exemplo, se na atividade inicial foi configurado um mecanismo de atribuição "Por Grupo" e definido o grupo "TI", apenas os usuários que fazem parte do grupo TI serão capazes de visualizar o processo para iniciá-lo.
